-- lists all Comedy shows in the database hbtn_0d_tvshows.
SELECT tv_s.title
FROM tv_shows AS tv_s
INNER JOIN tv_show_genres AS tv_g
ON tv_s.id = tv_g.show_id
INNER JOIN tv_genres AS g
ON g.id = tv_g.genre_id
WHERE g.name = "Comedy"
ORDER BY tv_s.title;
