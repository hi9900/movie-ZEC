export type WatchStatus = 'OnTime' | 'Late' | 'Not'

export type FilmWatch = {
	day: string,
	filmName: string
}

export type UserFilmWatch = {
	[userName: string]: FilmWatch[]
}

export type ListFilm = {
	film_name: string,
	list_position: number,
	list_url: string
}

export type Film = {
	name: string, 
	slug: string
}