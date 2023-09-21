-- lists all genres of the show Dexter.
SELECT g.name
FROM tv_genres AS g
INNER JOIN tv_show_genres AS tv_g
ON g.id = tv_g.genre_id
INNER JOIN tv_shows AS tv_s
ON tv_s.id = tv_g.show_id
WHERE tv_s.title = "DEXTER"
ORDER BY g.name;
