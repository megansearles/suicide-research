# Apparently exists_friendship is not a thing anymore, so this method doesn't work

import tweepy
import time

ckey = '96OUx6IbHfzuJyaazJmWRxw9a'
csecret = 'QB8LoQt5j16WI3O8PizftTCAWmdWEeWrtWInC7b2HqsYrCoEAh'
atoken = '793827708-95t9kQbxwXHSCvNq8tomLa0pOyE2JEtGfWxMlVcM'
asecret = 'VQ66vgFL5lQURvEc5WCJ7tafxAD1wCxvzXwgRWtRHZa5b'

auth = tweepy.OAuthHandler(ckey,csecret)
auth.set_access_token(atoken,asecret)

api = tweepy.API(auth)

init_user = api.get_user('lothlorienluna')
init_screen = str(init_user.screen_name)
init_id = init_user.id

init_follower_count = init_user.followers_count
init_friend_count = init_user.friends_count
init_list = []


if init_friend_count < init_follower_count:
	for page in tweepy.Cursor(api.friends_ids, screen_name=init_screen).pages():
		init_list.extend(page)
		time.sleep(60)
else:
	for page in tweepy.Cursor(api.followers_ids, screen_name=init_screen).pages():
		init_list.extend(page)
		time.sleep(60)

mutual_list = []
if init_friend_count < init_follower_count: 
	#Then init_list is full of people init_id follows, so init_id will be user_b
	for secondary in init_list:
		if api.exists_friendship(secondary,init_id):
			mutual_list.append(secondary)
else:
	#Then init_list is full of people who follow init_id, so init_id will be user_a
	for secondary in init_list:
		if api.exists_friendship(init_id,secondary):
			mutual_list.append(secondary)

print mutual_list