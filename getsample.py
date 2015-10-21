import tweepy
import time
import numpy
import sys
sys.path.append('..')
import m_auth	# This is the file with my authentication info. You can just fill in your own		

ckey = m_auth.ckey
csecret = m_auth.csecret
atoken = m_auth.atoken
asecret = m_auth.asecret

auth = tweepy.OAuthHandler(ckey,csecret)
auth.set_access_token(atoken,asecret)

api = tweepy.API(auth)

#To-Do:	Pull 1,000 user ids from a number of sources
#		Maybe 250 friends each from 4 users that would be representative
#		Remove protected users
#		Skip repeats
# 		Use @alexcaplow, @jimmyfallon, @emma_jen, and @CodyNolden
# 		Take 275 to account for protected users and repeats

sample_users = []

def pullFriends(sn_in):
	newfriends = api.friends_ids(screen_name = sn_in, count = 275)
	sample_users.extend(newfriends)
	time.sleep(60)

pullFriends("alexcaplow")
pullFriends("jimmyfallon")
pullFriends("emma_jen")	
pullFriends("CodyNolden")

print len(sample_users)

sample_users = list(set(sample_users))

print len(sample_users)

to_remove = []
split_array = numpy.array_split(sample_users, 11)
for arr in split_array:
	items = arr.tolist()
	users = api.lookup_users(user_ids=items)
	for user in users:
		if user.protected is True:
			to_remove.append(user.id)
	time.sleep(5)
for item in to_remove:
	sample_users.remove(item)
	
print len(sample_users)