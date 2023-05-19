package shocktoberScrape

import (
	"encoding/json"
	"net/http"
	"sort"
	"strings"
	"sync"

	"github.com/gocolly/colly"
	"go.uber.org/zap"
)

var sugarLog *zap.SugaredLogger
const urlscrape = "https://letterboxd.com/ajax/poster" //first part of url for getting full info on film
const urlEnd = "std/125x187/"                          // second part of url for getting full info on film
const site = "https://letterboxd.com"


type filmFromList struct {
	Name     string `json:"film_name"`
	Position int    `json:"list_position"`
	Slug     string `json:"list_url"`
}

func init(){
	logger, _ := zap.NewProduction()
	defer logger.Sync() // flushes buffer, if any
	sugarLog = logger.Sugar()

}

func ListHandler(w http.ResponseWriter, r *http.Request) {
	enableCors(&w)
	query := r.URL.Query()
	list := query.Get("list")
	if list == "" {
		http.Error(w, "no list", http.StatusBadRequest)
		return
	}

	listname := strings.ToLower(list)

	sugarLog.Infoln(listname)

	filmFromList := scapeList(listname)

	filmFromListAsJson, err := json.Marshal(filmFromList)
	if err != nil {
		http.Error(w, "Error Converting to json", http.StatusInternalServerError)
		return
	}
	w.Write(filmFromListAsJson)

}

func scapeList(listPartialUrl string) []filmFromList {
	url := ""
	listOfFilms := []filmFromList{}
	ch := make(chan filmFromList)

	if strings.Contains(listPartialUrl, "/list/") {
		url = site + "/" + listPartialUrl
	} else {
		strslice := strings.Split(listPartialUrl, "/") //strslice[0] is user name strslice[1] is listname
		url = site + "/" + strslice[0] + "/list/" + strslice[1]

	}

	sugarLog.Infoln("starting scrape")

	go scrapeListValues(url, ch)

	for value := range ch {
		listOfFilms = append(listOfFilms, value)

	}

	sort.SliceStable(listOfFilms, func(i, j int) bool {
		return listOfFilms[i].Position < listOfFilms[j].Position
	})

	return listOfFilms
}

func scrapeListValues(url string, ch chan filmFromList) {
	wg := sync.WaitGroup{}
	c := colly.NewCollector(
		colly.Async(true),
	)
	c.Limit(&colly.LimitRule{DomainGlob: "*", Parallelism: 100})
	c.OnHTML("ul.film-list", func(e *colly.HTMLElement) { //primary scarer to get url of each film that contian full information
		e.ForEach(".poster-container", func(i int, ein *colly.HTMLElement) {
			wg.Add(1)
			run := func() {
				name := ein.ChildAttr("img", "alt")
				slug := ein.ChildAttr(".film-poster", "data-film-slug")
				film := filmFromList{
					Name:     name,
					Slug:     slug,
					Position: i,
				}
				sugarLog.Infoln(film)
				ch <- film
				wg.Done()
			}
			go run()
		})

	})
	c.Visit(url)
	c.Wait()
	wg.Wait()
	close(ch)
}