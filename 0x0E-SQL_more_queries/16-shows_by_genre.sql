-- lists all shows, and all genres linked to that show,
-- from the database hbtn_0d_tvshows.
SELECT tv_s.title, g.name
FROM tv_shows AS tv_s
LEFT JOIN tv_show_genres AS tv_g
ON tv_s.id = tv_g.show_id
LEFT JOIN tv_genres AS g
ON tv_g.genre_id = g.id
ORDER BY tv_s.title, g.name;
