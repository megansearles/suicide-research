import json

with open('12May2016.json') as data_file:
    for line in data_file:    
        data = json.loads(line)
        try:
            tweet_id = 0
            tweet_id_str = 0
            text = 0
            in_reply_to_screen_name = 0
            in_reply_to_status_id_str = 0
            in_reply_to_status_id = 0
            in_reply_to_user_id_str = 0
            in_reply_to_user_id = 0
            filter_level = 0
            retweeted = 0
            retweet_count = 0
            
        except KeyError:
            tweet_id = -1
