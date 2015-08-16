import mutualfind
import tweepy
import time

#To-Do:	Pull main user's tweets 
#		Remove those tweets that are not replies
#		Make a list of the user ids of those the replies are to
#		Remove those who are not mutuals
#		See if they also have replies to the main user
#		(Write a function to do these things, so you can reuse it)
#		Set a minimum for something to gauge interaction level
#		Maybe look at faves and RTs?

# -----------------------------------------------------------------------

# Pulls the main user's 600 most recent tweets, then removes those that are not replies
# Note: not totally effective, still keeps some "in_reply_to_whatever=None"s
# Should not be a huge problem since we weed out not mutuals later, and None falls under that category
def pullReplies(user_in, list_in):
	user = mutualfind.api.get_user(user_in)
	recent_tweet = mutualfind.api.user_timeline(user_id=user.id, count=1)
	max = recent_tweet[0].id 
	for x in xrange(3):
		new_tweets = mutualfind.api.user_timeline(user_id=user.id, count=200, max_id=max)
		list_in.extend(new_tweets)
		max = list_in[-1].id - 1
		time.sleep(5)
	for tweet in list_in:
		if tweet.in_reply_to_user_id is None:
			list_in.remove(tweet)
			
# Makes list of mutuals who there are replies to
def checkMutual(list_in, list_out):
	for tweet in list_in:
		if tweet.in_reply_to_user_id in mutualfind.mutual_list and tweet.in_reply_to_user_id not in list_out:
			list_out.append(tweet.in_reply_to_screen_name)
	print str(list_out)
		
init_tweets = []
mutual_replies = []
pullReplies(mutualfind.init_id, init_tweets)
checkMutual(init_tweets, mutual_replies)


