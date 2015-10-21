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