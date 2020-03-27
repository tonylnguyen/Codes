-- This query is used to pull data that has been classified by a labeller and
-- measure their accuracy by comparing their decisions to the auditor's label.

with auditor as (
    SELECT
      job_id AS job_id,
      key_id,
      actor_name AS reviewer_name,
      date,
      job_source,
      json_array_get(JSON_EXTRACT(decision_data, '$.tags'), 0) AS tags_1,
      json_array_get(JSON_EXTRACT(decision_data, '$.tags'), 1) AS tags_2,
    FROM table_auditor
    WHERE
      ds >= '<DATEID-7>'
      AND event IN ('complete')
      AND queue_id IN (123456789, 987564231)
    GROUP BY
      1, 2, 3, 4, 5, 6, 7
),
labelers as (
    SELECT
      job_id AS job_id,
      key_id,
      actor_name AS reviewer_name,
      case when office_location is null then 'location_1' else 'location_2' end as office,
      date,
      job_source,
      json_array_get(JSON_EXTRACT(decision_data, '$.tags'), 0) AS tags_1,
      json_array_get(JSON_EXTRACT(decision_data, '$.tags'), 1) AS tags_2,
    FROM table_labeler
    WHERE
      ds >= '<DATEID-7>'
      AND event IN ('complete')
      AND queue_id IN (184849631858170, 563379610717361)
    GROUP BY
      1, 2, 3, 4, 5, 6, 7, 8)

SELECT
  auditor.date AS DATE,
  labelers.key_id AS key_id,
  labelers.office as Office,
  CONCAT('''', CAST(labelers.job_source AS VARCHAR)) AS labelers_job_source,
  labelers.reviewer_name AS labeler_name,
  labelers.reviewer_name AS auditor_name,
  labelers.tags_1 AS Rep_label1,
  auditor.tags_1 AS QA_label1,
  CASE
    WHEN auditor.tags_1 <> labelers.tags_1 THEN 'F'
    ELSE 'T'
  END AS Level_1_Match,
  labelers.tags_2 AS Rep_label2,
  auditor.tags_2 AS QA_label2,
  CASE
    WHEN auditor.tags_2 <> labelers.tags_2 THEN 'F'
    ELSE 'T'
  END AS Level_2_Match
From auditor
join labelers
  ON auditor.key_id = b.key_id
WHERE
  auditor.tags_1 <> labelers.tags_1
  OR auditor.tags_2 <> labelers.tags_2
ORDER BY
  auditor.DATE
