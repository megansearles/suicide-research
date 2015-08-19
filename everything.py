import tweepy
import time

ckey = '96OUx6IbHfzuJyaazJmWRxw9a'
csecret = 'QB8LoQt5j16WI3O8PizftTCAWmdWEeWrtWInC7b2HqsYrCoEAh'
atoken = '793827708-95t9kQbxwXHSCvNq8tomLa0pOyE2JEtGfWxMlVcM'
asecret = 'VQ66vgFL5lQURvEc5WCJ7tafxAD1wCxvzXwgRWtRHZa5b'

auth = tweepy.OAuthHandler(ckey,csecret)
auth.set_access_token(atoken,asecret)

api = tweepy.API(auth)

#To-Do:	Pull main user's tweets 
#		Remove those tweets that are not replies
#		Make a list of the user ids of those the replies are to
#		Remove those who are not mutuals
#		See if they also have replies to the main user
#		(Write a function to do these things, so you can reuse it)
#		Set a minimum for something to gauge interaction level
#		Maybe look at faves and RTs?

init_user = api.get_user('TweetThis3000')
init_id = init_user.id

init_follower_count = init_user.followers_count
init_friend_count = init_user.friends_count

def buildList(list_in,id_in):
	if init_friend_count < init_follower_count:
		for page in tweepy.Cursor(api.friends_ids, user_id=id_in).pages():
			list_in.extend(page)
			time.sleep(60)
	else:
		for page in tweepy.Cursor(api.followers_ids, user_id=id_in).pages():
			list_in.extend(page)
			time.sleep(60)

def pullReplies(user_in, list_in):
	recent_tweet = api.user_timeline(user_id=user_in, count=1)
	max = recent_tweet[0].id 
	for x in xrange(3):
		new_tweets = api.user_timeline(user_id=user_in, count=200, max_id=max)
		list_in.extend(new_tweets)
		max = list_in[-1].id - 1
		time.sleep(5)
	for tweet in list_in:
		if tweet.in_reply_to_user_id is None:
			list_in.remove(tweet)
	
init_list = []
buildList(init_list, init_id)
for item in init_list:
	user = api.get_user(user_id=item)
	if user.protected is True:
		init_list.remove(item)
	time.sleep(5)
			
mutual_list = []
for secondary in init_list:
	secondary_list = []
	buildList(secondary_list, secondary)
	if init_id in secondary_list:
		mutual_list.append(secondary)
		
init_tweets = []
pullReplies(init_id, init_tweets)

mutual_replies = []
for tweet in init_tweets:
	if tweet.in_reply_to_user_id in mutual_list and tweet.in_reply_to_user_id not in mutual_replies:
		mutual_replies.append(tweet.in_reply_to_screen_name)

for item in mutual_replies:
	print str(item)