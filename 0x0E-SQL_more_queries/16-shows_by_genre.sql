-- Script to list all shows and all genres linked to that show from hbtn_0d_tvshows
-- Display all the shows and genres
SELECT tv_shows.title AS title, tv_genres.name AS name
  FROM tv_shows
  LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
  LEFT JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id
  ORDER BY title, name;
