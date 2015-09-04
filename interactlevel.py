import tweepy
import time
import numpy
import os
import sys
sys.path.append('..')
import m_auth	# This is the file with my authentication info. You can just fill in your own

time.clock() # Starts timer for testing purposes

ckey = m_auth.ckey
csecret = m_auth.csecret
atoken = m_auth.atoken
asecret = m_auth.asecret

auth = tweepy.OAuthHandler(ckey,csecret)
auth.set_access_token(atoken,asecret)

api = tweepy.API(auth)

#To-Do:	Give numeric values to four features
#			1) replies to mutual from main user
#			2) replies to main user from mutual
#			3) favorites of mutual's tweets by main user
#			4) favorites of main user's tweets by mutual
#		Add features to array
#		Write array to a csv file so we can analyze the data
	
init_user = api.get_user('lothlorienluna') # Get main user's information. Could probably be made to prompt for a user and then run program
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
	time.sleep(5)
	max = recent_tweet[0].id 
	for x in xrange(3):
		new_tweets = api.user_timeline(user_id=user_in, count=200, max_id=max)
		list_in.extend(new_tweets)
		max = list_in[-1].id - 1
		time.sleep(5)
	for tweet in list_in:
		if tweet.in_reply_to_user_id is None: 
			list_in.remove(tweet)

# Calculates feature, and adds it to the array			
def addPercentage(my_array,mutual_list,list_in,column):
	total = len(list_in)
	for mutual in mutual_list:
		occurences = list_in.count(mutual)
		if total != 0:
			percentage = occurences/float(total)
		else: 
			percentage = 0
		for i in xrange(len(mutual_list)):
			if my_array[i,0] == mutual:
				my_array[i,column] = percentage

# Builds initial list, removes protected users, because can't access their followers/following
init_list = []
buildList(init_list, init_id)
to_remove1 = []
for item in init_list:
	user = api.get_user(user_id=item)
	if user.protected is True:
		to_remove1.append(item)
	time.sleep(5)
for item in to_remove1:
	init_list.remove(item)
	
print "check 1" 
print time.clock()

#Builds list of each follower/friend's following/friends to see if main user is in the list			
mutual_list = []
for secondary in init_list:
	secondary_list = []
	buildList(secondary_list, secondary)
	if init_id in secondary_list:
		mutual_list.append(secondary)
		
print "check 2"
print time.clock()
		
# This is the array I'll keep the information about each mutual in, i.e. their id + the four features
# Need to rename it with something more descriptive
my_array = numpy.zeros((len(mutual_list),5))

# Adds every mutual to the array
for i in xrange(len(mutual_list)):
	my_array[i,0] = mutual_list[i]
		
init_tweets = []
pullReplies(init_id, init_tweets)

# Gets replies to mutuals specifically
init_replies = []
for tweet in init_tweets:
	if tweet.in_reply_to_user_id in mutual_list: 
		init_replies.append(tweet.in_reply_to_user_id)

print "check 3"	
print time.clock()	
		
# Gets rid of Nones
to_remove2 = []
for item in init_replies:
	if item is None:
		to_remove2.append(item)
for item in to_remove2:
	init_replies.remove(item)
	
addPercentage(my_array,mutual_list,init_replies,1)

# Gets replies from mutuals to main user, adds those mutuals to list
mutual_replies = []
placeholder = [init_id]
for secondary in mutual_list:
	sec_tweets = []
	pullReplies(secondary, sec_tweets)
	for tweet in sec_tweets:
		if tweet.in_reply_to_user_id in placeholder: 
			mutual_replies.append(secondary)
			
print "check 4"
print time.clock()

addPercentage(my_array,mutual_list,mutual_replies,2)
	
init_faves = api.favorites(user_id=init_id,count=200)
time.sleep(60)
init_fave_ids = []	
for fave in init_faves:
	if fave.user.id in mutual_list: 
		init_fave_ids.append(fave.user.id)
		
addPercentage(my_array,mutual_list,init_fave_ids,3)

print "check 5"
print time.clock()

mutual_fave_ids = []
for secondary in mutual_list:
	sec_faves = api.favorites(user_id=secondary,count=200)
	for fave in sec_faves:
		if fave.user.id in placeholder: 
			mutual_fave_ids.append(secondary)
	time.sleep(60)
	
addPercentage(my_array,mutual_list,mutual_fave_ids,4)

print "check 6"
print time.clock()

numpy.savetxt('lothlorienluna.csv',my_array,delimiter=',',newline='\n')