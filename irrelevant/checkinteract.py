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
#		  (Write a function to do these things, so you can reuse it)
#		Set a minimum for something to gauge interaction level
#		  Or: set up a ranking system
#		Maybe look at faves and RTs?

init_user = api.get_user('ashlaraee002') # Get main user's information. Could probably be made to prompt for a user and then run program
init_id = init_user.id

init_follower_count = init_user.followers_count
init_friend_count = init_user.friends_count

# Creates a list of followers or friends of a user, depending on which has less items
def buildList(list_in,id_in):
	if init_friend_count < init_follower_count:
		for page in tweepy.Cursor(api.friends_ids, user_id=id_in).pages():
			list_in.extend(page)
			time.sleep(60)
	else:
		for page in tweepy.Cursor(api.followers_ids, user_id=id_in).pages():
			list_in.extend(page)
			time.sleep(60)

# Gets 600 most recent tweets, then removes all but the replies
def pullReplies(user_in, list_in):
	recent_tweet = api.user_timeline(user_id=user_in, count=1)
	max = recent_tweet[0].id 
	for x in xrange(3):
		new_tweets = api.user_timeline(user_id=user_in, count=200, max_id=max)
		list_in.extend(new_tweets)
		max = list_in[-1].id - 1
		time.sleep(5)
	for tweet in list_in:
		# Note: Doesn't remove all Nones for some reason, but can be filtered out later by other means
		if tweet.in_reply_to_user_id is None: 
			list_in.remove(tweet)
	
init_list = []
buildList(init_list, init_id)
# Removes protected users, because can't access their followers/following
for item in init_list:
	user = api.get_user(user_id=item)
	if user.protected is True:
		init_list.remove(item)
	time.sleep(5)
			
mutual_list = []
#Builds list of each follower/friend's following/friends to see if main user is in the list
for secondary in init_list:
	secondary_list = []
	buildList(secondary_list, secondary)
	if init_id in secondary_list:
		mutual_list.append(secondary)
		
init_tweets = []
pullReplies(init_id, init_tweets)

init_replies = []
for tweet in init_tweets:
	# If the reply is to a mutual and is not already in the list, then it is added to the list of mutuals the main user replies to
	if tweet.in_reply_to_user_id in mutual_list and tweet.in_reply_to_user_id not in init_replies:
		init_replies.append(tweet.in_reply_to_user_id)
	
# Checks if secondary user also replies to main user - Should there be something more?
# Didn't work with commented out section, so I fixed it up in a more roundabout way
mutual_replies = []
placeholder = [init_id]
for secondary in init_replies:
	sec_tweets = []
	pullReplies(secondary, sec_tweets)
	for tweet in sec_tweets:
		if tweet.in_reply_to_user_id in placeholder and secondary not in mutual_replies:
			mutual_replies.append(secondary)
	#answer = any(tweet.in_reply_to_user_id is init_id for tweet in sec_tweets)
	#if answer:
	#	mutual_replies.append(secondary)
	
init_faves = api.favorites(user_id=init_id,count=200)
time.sleep(60)
init_fave_ids = []	
for fave in init_faves:
	if fave.user.id in mutual_list and fave.user.id not in init_fave_ids:
		init_fave_ids.append(fave.user.id)

mutual_fave_ids = []
for secondary in init_fave_ids:
	sec_faves = api.favorites(user_id=secondary,count=200)
	for fave in sec_faves:
		if fave.user.id in placeholder and secondary not in mutual_fave_ids:
			mutual_fave_ids.append(secondary)
	time.sleep(60)


