package shocktoberScrape

import (
	"encoding/json"
	"fmt"
	"net/http"
	"strconv"
	"sync"

	"github.com/gocolly/colly"
	"go.uber.org/zap"
)

var sugar *zap.SugaredLogger

type filmDiaryEntryWithUser struct {
	Day string
	Name string
	User string
}

type filmDiaryEntry struct {
	Day string `json:"day"`
	Name string `json:"filmName"`
}

type channelValueSend struct {
	FilmEntry filmDiaryEntryWithUser
	Done bool 
}

func init(){
	logger, _ := zap.NewProduction()
	defer logger.Sync() // flushes buffer, if any
	sugar = logger.Sugar()

}

func Handler(w http.ResponseWriter, r *http.Request) {
	
	enableCors(&w)
	query := r.URL.Query() //Get URL Params(type map)
	user, ok := query["user"]
	if !ok || len(user) == 0 {
		http.Error(w, "no users", http.StatusBadRequest)
		return
	}
	sugar.Infoln(user)
	month, ok := query["month"]
	if !ok || len(user) == 0 {
		http.Error(w, "no month", http.StatusBadRequest)
		return
	}
	year, ok := query["year"]
	if !ok || len(user) == 0 {
		http.Error(w, "no year", http.StatusBadRequest)
		return
	}
	monthAsString, _ := strconv.Atoi(month[0])
	yearAsString, _ := strconv.Atoi(year[0])

	
	userMap := scrapeUserMonth(user,monthAsString,yearAsString)

	userMapAsJson, err := json.Marshal(userMap)
	if err != nil {
		http.Error(w, "no year", http.StatusBadRequest)
		return
	}

	w.Write(userMapAsJson)

}
//https://letterboxd.com/holopollock/films/diary/for/2022/09/
func scrapeUserMonth(users []string, month int, year int) map[string][]filmDiaryEntry {
	userMap := map[string][]filmDiaryEntry{}
	ch := make(chan channelValueSend)
	numberOfUsers := len(users)
	sugar.Infoln("running")
	for _, user := range users {
		go scrapeUser("https://letterboxd.com/"+user+"/films/diary/for/"+strconv.Itoa(year)+"/"+fmt.Sprintf("%02d", month),ch, user)
	}

	for channelValue := range ch {
		if channelValue.Done {
			numberOfUsers--
			if numberOfUsers == 0 {
				break
			}
			continue
		}
		filmEntry := channelValue.FilmEntry
		filmList, exists := userMap[filmEntry.User]
		if exists {
			filmList = append(filmList, filmDiaryEntry{Day: filmEntry.Day, Name: filmEntry.Name})
			userMap[filmEntry.User] = filmList	
		} else {
			userMap[filmEntry.User] = []filmDiaryEntry{{Day: filmEntry.Day, Name: filmEntry.Name}}
		}
	}
	sugar.Infoln(userMap)
	return userMap
}

func scrapeUser(url string, ch chan channelValueSend, user string) {
	wg := sync.WaitGroup{}
	c := colly.NewCollector(
		colly.Async(true),
	)
	c.Limit(&colly.LimitRule{DomainGlob: "*", Parallelism: 1000})

	c.OnHTML(".diary-entry-row", func(e *colly.HTMLElement) {
		sugar.Infoln("scraping")
		wg.Add(1)
		run := func() {
			date:= e.ChildText(".diary-day a")
			name := e.ChildText(".td-film-details h3.headline-3 a")
			
			film := filmDiaryEntryWithUser{
				Day: date,
				Name: name,
				User: user,
			}
			ch <- channelValueSend{FilmEntry: film, Done: false}
			wg.Done()
		}
		go run()
	})


	c.OnHTML("div.paginate-nextprev", func(e *colly.HTMLElement) {
		nextPage := e.ChildAttr("a.next", "href")
		e.Request.Visit(e.Request.AbsoluteURL(nextPage))
	})

	sugar.Infoln("staring scrape at " + url)

	c.Visit(url)
	c.Wait()
	wg.Wait()
	ch <- channelValueSend{Done: true}
}

func enableCors(w *http.ResponseWriter) {
	(*w).Header().Set("Access-Control-Allow-Origin", "*")
}
