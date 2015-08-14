import mutualfind
import time

#To-Do:	Pull main user's tweets 
#		Remove those tweets that are not replies
#		Make a list of the user ids of those the replies are to
#		Remove those who are not mutuals
#		See if they also have replies to the main user
#		(Write a function to do these things, so you can reuse it)
#		Set a minimum for something to gauge interaction level
#		Maybe look at faves and RTs?

def pullReplies(user_in):
	user = mutualfind.api.get_user(user_in)
	init_tweets = []
	recent_tweet = mutualfind.api.user_timeline(user_id=user.id, count=1)
	max = recent_tweet[0].id 
	for x in xrange(3):
		new_tweets = mutualfind.api.user_timeline(user_id=user.id, count=200, max_id=max)
		init_tweets.extend(new_tweets)
		max = init_tweets[-1].id - 1
		time.sleep(5)
	print init_tweets[0:3]	

pullReplies("thesquareroots5")

