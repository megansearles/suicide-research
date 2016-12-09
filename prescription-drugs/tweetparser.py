import json

unique_users = []

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
        try:
            coordinates = data["coordinates"]["coordinates"]
        except TypeError:
            coordinates = "Null"
        try:
            place_id = data["place"]["id"]
        except TypeError:
            place_id = "Null"
        
        if user_id not in unique_users:
            user_id_str = data["user"]["id_str"]
            protected = data["user"]["protected"]
            screen_name = data["user"]["screen_name"]
            verified = data["user"]["verified"]
            statuses_count = data["user"]["statuses_count"]
            try:
                description = data["description"]
            except KeyError:
                description = "Null"
            try:
                location = data["user"]["location"]
            except KeyError:
                location = "Null"
            unique_users.append(user_id)
