-- show show by genre id

SELECT ts.title, tsg.genre_id FROM tv_shows AS ts INNER JOIN tv_show_genres AS tsg ON tsg.show_id = ts.id ORDER BY ts.title, tsg.genre_id;
