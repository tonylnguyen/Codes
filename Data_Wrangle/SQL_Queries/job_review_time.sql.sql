WITH data_labeller AS (
    SELECT
        actor_name,
        location_name,
        (review_time_ms) / (1000) AS review_time_s,
        event,
        key_id,
        CAST(FROM_UNIXTIME(time_stamp) AS DATE) AS time_stamp,
        date
    FROM table_1
    WHERE
        source_id IN (
            968357241,
            147258369,
            963852741,
            789456123,
            3521654987,
            987654321,
            123456789
        )
        AND ds >= '<DATEID-15>'
        AND event IN ('completed')
)
SELECT
    date,
    actor_name,
    location_name,
    COUNT(DISTINCT key_id) AS total_jobs_labelled,
    ROUND((3600 / AVG(review_time_s)), 2) AS avg_labelled_per_hour,
    SUM(review_time_s) / 3600.0 AS total_review_time,
    AVG(review_time_s) AS average_review_time_s
FROM label
GROUP BY
    1, 2, 3
ORDER BY
    1 DESC
