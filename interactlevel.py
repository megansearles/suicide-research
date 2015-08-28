import tweepy
import time
import numpy

# Note: comments on content that was in checkinteract are in that program

ckey = '96OUx6IbHfzuJyaazJmWRxw9a'
csecret = 'QB8LoQt5j16WI3O8PizftTCAWmdWEeWrtWInC7b2HqsYrCoEAh'
atoken = '793827708-95t9kQbxwXHSCvNq8tomLa0pOyE2JEtGfWxMlVcM'
asecret = 'VQ66vgFL5lQURvEc5WCJ7tafxAD1wCxvzXwgRWtRHZa5b'

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
	
init_user = api.get_user('lothlorienluna') 
init_id = init_user.id

init_follower_count = init_user.followers_count
init_friend_count = init_user.friends_count

def buildList(list_in,id_in):
	if init_friend_count < init_follower_count:
		for page in tweepy.Cursor(api.friends_ids, user_id=id_in).pages():
			list_in.extend(page)
	else:
		for page in tweepy.Cursor(api.followers_ids, user_id=id_in).pages():
			list_in.extend(page)

def pullReplies(user_in, list_in):
	recent_tweet = api.user_timeline(user_id=user_in, count=1)
	max = recent_tweet[0].id 
	for x in xrange(3):
		new_tweets = api.user_timeline(user_id=user_in, count=200, max_id=max)
		list_in.extend(new_tweets)
		max = list_in[-1].id - 1
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
	
init_list = []
buildList(init_list, init_id)
time.sleep(60)
for item in init_list:
	user = api.get_user(user_id=item)
	if user.protected is True:
		init_list.remove(item)
	time.sleep(5)
			
mutual_list = []
mutual_replies = []
mutual_fave_ids = []
placeholder = [init_id]
for secondary in init_list:
	secondary_list = []
	buildList(secondary_list, secondary)
	if init_id in secondary_list:
		mutual_list.append(secondary)
	if secondary in mutual_list:
		# Mutual replies
		sec_tweets = []
		pullReplies(secondary, sec_tweets)
		for tweet in sec_tweets:
			if tweet.in_reply_to_user_id in placeholder: 
				mutual_replies.append(secondary)
		# Mutual faves
		sec_faves = api.favorites(user_id=secondary,count=200)
		for fave in sec_faves:
			if fave.user.id in placeholder: 
				mutual_fave_ids.append(secondary)
	time.sleep(60)
		
init_tweets = []
pullReplies(init_id, init_tweets)

init_replies = []
for tweet in init_tweets:
	if tweet.in_reply_to_user_id in mutual_list: 
		init_replies.append(tweet.in_reply_to_user_id)
# Gets rid of Nones
for item in init_replies:
	if item is None:
		init_replies.remove(item)
		
init_faves = api.favorites(user_id=init_id,count=200)
init_fave_ids = []	
for fave in init_faves:
	if fave.user.id in mutual_list: 
		init_fave_ids.append(fave.user.id)
		
# This is the array I'll keep the information about each mutual in, i.e. their id + the four features
# Need to rename it with something more descriptive
my_array = numpy.zeros((len(mutual_list),5))

# Adds every mutual to the array
for i in xrange(len(mutual_list)):
	my_array[i,0] = mutual_list[i]
		
addPercentage(my_array,mutual_list,init_replies,1)
			
addPercentage(my_array,mutual_list,mutual_replies,2)
		
addPercentage(my_array,mutual_list,init_fave_ids,3)
	
addPercentage(my_array,mutual_list,mutual_fave_ids,4)

numpy.savetxt('lothlorienluna.csv',my_array,delimiter=',',newline='\n')