import json

with open('12May2016.json') as data_file:
    for line in data_file:    
        data = json.loads(line)

        tweet_id = data["id"]
        tweet_id_str = data["id_str"]
        text = data["text"]
        created_at = data["created_at"]
        user_id = data["user"]["id"]

        try:
            in_reply_to_screen_name = data["in_reply_to_screen_name"]
            in_reply_to_status_id_str = data["in_reply_to_status_id_str"]
            in_reply_to_status_id = data["in_reply_to_status_id"]
            in_reply_to_user_id_str = data["in_reply_to_user_id_str"]
            in_reply_to_user_id = data["in_reply_to_user_id"]
        except KeyError:
            in_reply_to_screen_name = "Null"
            in_reply_to_status_id_str = "Null"
            in_reply_to_status_id = 0
            in_reply_to_user_id_str = "Null"
            in_reply_to_user_id = 0
        coordinates = data["coordinates"]["coordinates"]
#TypeError: 'NoneType' object has no attribute '__getitem__'
        print coordinates
#        place_id = ["place"]["id"]
