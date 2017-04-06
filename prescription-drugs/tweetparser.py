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
           "(tweet_id, longitude, latitude, country, state, county, city) "
           "VALUES (%s, %s, %s, %s, %s, %s, %s)")

add_tweet = ("INSERT INTO tweets "
             "(tweet_id, tweet_id_str, text, in_reply_to_screen_name, in_reply_to_status_id, in_reply_to_status_id_str, in_reply_to_user_id, in_reply_to_user_id_str, retweet_count, favorite_count, created_at, user_id) "
             "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")

add_user = ("INSERT INTO users "
            "(user_id, user_id_str, protected, screen_name, verified, statuses_count, description, location) "
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")

unique_users = []
file_number = 0
file_name = "carmen-" + str(file_number) + ".txt"
file_count = len(glob.glob("file-*.txt"))

for n in range(file_count):
    row_number = 1
    with open(file_name) as data_file:
        for line in data_file:    
            data = json.loads(line)
            try:
                tweet_id = data["id"]
                tweet_id_str = data["id_str"]
            except KeyError:
                continue
            try:
                text = data["text"]
            except KeyError:
                continue
            created_at = data["created_at"]
            try:
                user_id = data["user"]["id"]
            except KeyError:
                continue
            try:
                retweet_count = data["retweet_count"]
            except KeyError:
                retweet_count = 0

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
                longitude = data["location"]["longitude"]
                latitude = data["location"]["latitude"]
            except KeyError:
                longitude = 0
                latitude = 0
            try:
                country = data["location"]["country"]
            except KeyError:
                country = "Null"
            try:
                state = data["location"]["state"]
            except KeyError:
                state = "Null"
            try:
                county = data["location"]["county"]
            except KeyError:
                county = "Null"
            try:
                city = data["location"]["city"]
            except KeyError:
                city = "Null"

            if longitude != 0 or latitude != 0:
                data_geo = (tweet_id, longitude, latitude, country, state, county, city)
                cursor.execute(add_geo, data_geo)

            data_tweet = (tweet_id, tweet_id_str, text, in_reply_to_screen_name, in_reply_to_status_id, in_reply_to_status_id_str, in_reply_to_user_id, in_reply_to_user_id_str, retweet_count, favorite_count, created_at, user_id)
            cursor.execute(add_tweet, data_tweet)
        
            if user_id not in unique_users:
                try:
                    user_id_str = data["user"]["id_str"]
                except KeyError:
                    user_id_str = str(user_id)
                protected = data["user"]["protected"]
                screen_name = data["user"]["screen_name"]
                try:
                    verified = data["user"]["verified"]
                except KeyError:
                    verified = 0
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
    file_name = "carmen-" + str(file_number) + ".txt"

cnx.commit()
cursor.close()
cnx.close()
