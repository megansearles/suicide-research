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
for secondary in init_list:
	secondary_list = []
	if init_friend_count < init_follower_count:
		for page in tweepy.Cursor(api.friends_ids, user_id=secondary).pages():
			secondary_list.extend(page)
			time.sleep(60)
	else:
		for page in tweepy.Cursor(api.followers_ids, user_id=secondary).pages():
			secondary_list.extend(page)
			time.sleep(60)
	if init_id in secondary_list:
		mutual_list.append(secondary)
		
