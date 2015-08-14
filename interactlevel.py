# Don't forget to add mutualfind stuff back in later, at every instance of api
# import mutualfind
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

# Pulls the main user's 600 most recent tweets, then removes those that are not replies
def pullReplies(user_in, list_in):
	user = api.get_user(user_in)
	recent_tweet = api.user_timeline(user_id=user.id, count=1)
	max = recent_tweet[0].id 
	for x in xrange(3):
		new_tweets = api.user_timeline(user_id=user.id, count=200, max_id=max)
		list_in.extend(new_tweets)
		max = list_in[-1].id - 1
		time.sleep(5)
	for tweet in list_in:
		if tweet.in_reply_to_user_id is None:
			list_in.remove(tweet)
		
init_tweets = []
pullReplies("thesquareroots5", init_tweets)

for tweet in init_tweets:
	#print tweet.in_reply_to_screen_name
	print tweet
	
#Edit so you know what's up later:
# For some reason it's not getting rid of all the tweets that have "in_reply_to... = Null"
# It's keeping the retweets of my and natalie's tweets