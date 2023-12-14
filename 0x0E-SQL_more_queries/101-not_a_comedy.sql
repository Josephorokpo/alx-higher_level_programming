-- Lists all shows without the genre Comedy in the database hbtn_0d_tvshows.
-- The tv_genres table contains only one record where name = Comedy (but the id can be different)
-- Each record should display: tv_shows.title
-- Results must be sorted in ascending order by the show title
SELECT `title`
FROM `tv_shows` AS t
LEFT JOIN `tv_show_genres` AS s ON s.`show_id` = t.`id`
LEFT JOIN `tv_genres` AS g ON g.`id` = s.`genre_id`
WHERE NOT EXISTS (
    SELECT 1
    FROM `tv_show_genres` AS sub_s
    INNER JOIN `tv_genres` AS sub_g ON sub_g.`id` = sub_s.`genre_id`
    WHERE sub_s.`show_id` = t.`id` AND sub_g.`name` = 'Comedy'
)
ORDER BY `title`;
