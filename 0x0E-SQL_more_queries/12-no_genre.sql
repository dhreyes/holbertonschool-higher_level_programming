-- Script to list all shows contained in hbtn_0d_tvshows without a genre
-- Display tv_shows.title - tv_show_genres.genre_id, sorted in asc
SELECT tv_shows.title, tv_show_genres.genre_id
	FROM tv_shows LEFT JOIN tv_show_genres
	ON tv_shows.id = tv_show_genres.show.id
	WHERE tv_show_genres.genre_id IS NULL
	ORDER BY tv_shows.title, tv_show_genres.genre_id;
