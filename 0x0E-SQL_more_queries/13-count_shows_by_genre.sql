-- Script to list all genres from hbtn_0d_tvshows and display number of shows in each
-- Display <TV Show genre> - <Number of shows linked to genre>
SELECT tv_genres.name AS "genre", COUNT(tv_show_genres.show_id) AS number_of_shows
	FROM tv_genres INNER JOIN tv_show_genres
	ON tv_genres.id = tv_show_genres.genre_id
	GROUP BY genre
	ORDER BY number_of_shows DESC;
