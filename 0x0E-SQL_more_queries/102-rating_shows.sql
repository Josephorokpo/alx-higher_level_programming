-- Lists all shows from hbtn_0d_tvshows_rate by their rating.
-- Each record should display: tv_shows.title - rating sum
-- Results must be sorted in descending order by the rating
SELECT t.`title`, SUM(r.`rate`) AS `rating`
FROM `tv_shows` AS t
INNER JOIN `tv_show_ratings` AS r ON t.`id` = r.`show_id`
GROUP BY t.`title`
ORDER BY `rating` DESC;
