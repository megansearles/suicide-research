# -*- coding: utf-8 -*-

import json
import MySQLdb
import sys
sys.path.append('../..')
import auth
import glob

user = auth.user
host = auth.host
password = auth.password
database = auth.database

cnx = MySQLdb.connect(user=user, host=host, passwd=password, db=database, use_unicode=True)
cursor = cnx.cursor()

cnx.set_character_set('utf8mb4')
cursor.execute("SET NAMES utf8mb4")
cursor.execute("SET CHARACTER SET utf8mb4")
cursor.execute("SET character_set_connection=utf8mb4")

add_geo = ("INSERT INTO geo "
           "(tweet_id, coord_type, longitude, latitude) "
           "VALUES (%s, %s, %s, %s)")

add_tweet = ("INSERT INTO tweets "
             "(tweet_id, tweet_id_str, text, in_reply_to_screen_name, in_reply_to_status_id, in_reply_to_status_id_str, in_reply_to_user_id, in_reply_to_user_id_str, retweet_count, favorite_count, created_at, place_id, user_id) "
             "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")

add_user = ("INSERT INTO users "
            "(user_id, user_id_str, protected, screen_name, verified, statuses_count, description, location) "
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")

unique_users = []
file_number = 0
file_name = "file-" + str(file_number) + ".txt"
file_count = len(glob.glob("file-*.txt"))

for n in range(file_count):
    row_number = 1
    with open(file_name) as data_file:
        for line in data_file:    
            data = json.loads(line)

            tweet_id = data["id"]
            tweet_id_str = data["id_str"]
            text = data["text"]
            created_at = data["created_at"]
            user_id = data["user"]["id"]
            retweet_count = data["retweet_count"]

            f = open('last_id', 'w')
            f.write(str(tweet_id))
            f.close()

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
                favorite_count = data["favorite_count"]
            except KeyError:
                favorite_count = "Null"
            try:
                longitude = data["coordinates"]["coordinates"][0]
                latitude = data["coordinates"]["coordinates"][1]
                coord_type = data["coordinates"]["type"]
            except TypeError:
                longitude = 0
                latitude = 0
                coord_type = "Null"
            try:
                place_id = data["place"]["id"]
            except TypeError:
                place_id = "Null"

            if coord_type != "Null" or longitude != 0 or latitude != 0:
                data_geo = (tweet_id, coord_type, longitude, latitude)
                cursor.execute(add_geo, data_geo)

            data_tweet = (tweet_id, tweet_id_str, text, in_reply_to_screen_name, in_reply_to_status_id, in_reply_to_status_id_str, in_reply_to_user_id, in_reply_to_user_id_str, retweet_count, favorite_count, created_at, place_id, user_id)
            cursor.execute(add_tweet, data_tweet)
        
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

                data_user = (user_id, user_id_str, protected, screen_name, verified, statuses_count, description, location)
                cursor.execute(add_user, data_user)

            f = open('row_number', 'w')
            f.write(str(row_number))
            f.close()
            row_number += 1

    f = open('file_number', 'w')
    f.write(str(file_number))
    f.close()
    file_number += 1
    file_name = "file-" + str(file_number) + ".txt"

cnx.commit()
cursor.close()
cnx.close()
