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

#To-Do: Get list of features for each user in sample_users
#       Features include:
#        From User objects:
#          Number of followers
#          Number of following
#          Total number of favorites
#          Total number of tweets
#        From Tweet objects:
#          Percentage of last 200 tweets that are replies
#          Percentage of last 200 tweets that are retweets
#          Percentage of last 200 tweets that have been favorited by others
#          Percentage of last 200 tweets that have been retweeted by others
#          Average number of favorites for last 200 tweets
#          Average number of retweets for last 200 tweets

sample_users = numpy.loadtxt('sample_users.csv', delimiter=',')

split_array = numpy.array_split(sample_users, 10)
for arr in split_array:
    items = arr.tolist()
    users = api.lookup_users(user_ids=items)
    for user in users:
        print user # Delete when put actual content
        # Fill in with actions to add features from User objects
    time.sleep(5)
    
for user in sample_users:
    tweets = api.user_timeline(id = user, count = 200)
    # Fill in with actions to add features from Tweet objects
    time.sleep(5)

