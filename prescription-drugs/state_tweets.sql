CREATE TABLE state_ids LIKE tweet_ids;

INSERT INTO state_ids SELECT tweet_id FROM geo_copy WHERE country LIKE "United States" AND state LIKE "Alabama";

CREATE TABLE Alabama LIKE tweets_copy;

INSERT INTO Alabama SELECT * FROM tweets_copy WHERE tweet_id IN (SELECT DISTINCT tweet_id FROM state_ids);

DROP TABLE state_ids;
