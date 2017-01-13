SET NAMES utf8mb4;

CREATE DATABASE prescription_drugs CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;

use prescription_drugs

CREATE TABLE geo (
  tweet_id VARCHAR(191),
  coord_type VARCHAR(191),
  longitude BIGINT(20),
  latitude BIGINT(20)
) DEFAULT CHARSET = utf8mb4;

CREATE TABLE tweets (
  tweet_id VARCHAR(191),
  tweet_id_str VARCHAR(191),
  text VARCHAR(191),
  in_reply_to_screen_name VARCHAR(191),
  in_reply_to_status_id BIGINT(20),
  in_reply_to_status_id_str VARCHAR(191),
  in_reply_to_user_id BIGINT(20),
  in_reply_to_user_id_str VARCHAR(191),
  retweet_count BIGINT(20),
  favorite_count BIGINT(20),
  created_at VARCHAR(191),
  place_id VARCHAR(191),
  user_id VARCHAR(191)
) DEFAULT CHARSET = utf8mb4;

CREATE TABLE users (
  user_id VARCHAR(191),
  user_id_str VARCHAR(191),
  protected TINYINT(1),
  screen_name VARCHAR(191),
  verified TINYINT(1),
  statuses_count BIGINT(20),
  description VARCHAR(191),
  location VARCHAR(191)
) DEFAULT CHARSET = utf8mb4;

SET CHARACTER_SET_CLIENT = utf8mb4;
SET CHARACTER_SET_RESULTS = utf8mb4;
SET COLLATION_CONNECTION = utf8mb4_unicode_ci;
