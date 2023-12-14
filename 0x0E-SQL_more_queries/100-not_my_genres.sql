-- Uses the hbtn_0d_tvshows database to list all genres not linked to the show Dexter
-- The tv_shows table contains only one record where title = Dexter (but the id can be different)
-- Each record should display: tv_genres.name
-- Results must be sorted in ascending order by the genre name
SELECT `name`
FROM `tv_genres` AS g
WHERE NOT EXISTS (
    SELECT 1
    FROM `tv_show_genres` AS s
    INNER JOIN `tv_shows` AS t ON s.`show_id` = t.`id`
    WHERE g.`id` = s.`genre_id` AND t.`title` = 'Dexter'
)
ORDER BY g.`name`;
