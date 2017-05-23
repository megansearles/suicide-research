import tweepy
import time
import sys
sys.path.append('..')
import m_auth 

time.clock() # Starts timer for testing purposes

ckey = m_auth.ckey
csecret = m_auth.csecret
atoken = m_auth.atoken
asecret = m_auth.asecret

auth = tweepy.OAuthHandler(ckey,csecret)
auth.set_access_token(atoken,asecret)

api = tweepy.API(auth)

init_user = api.get_user('lothlorienluna') 
time.sleep(5)

# Stores id, follower count, and friend count for an initial user
init_id = init_user.id
init_follower_count = init_user.followers_count
init_friend_count = init_user.friends_count

# Gets the list of friends for a user
def get_friends(id_in):
    friend_list = []
    for page in tweepy.Cursor(api.friends_ids, user_id=id_in).pages():
        friend_list.extend(page)
        time.sleep(60)
    return friend_list

# Gets 600 most recent tweets for a user
def get_tweets(id_in):
    tweets_list = []
    recent_tweet = api.user_timeline(user_id=id_in, count=1)
    time.sleep(5)
    if recent_tweet != []:
        max_tweet = recent_tweet[0].id
        for x in range(3):
            new_tweets = api.user_timeline(user_id=id_in, count=200, max_id=max_tweet)
            tweets_list.extend(new_tweets)
            max_tweet = tweets_list[-1].id-1
            time.sleep(5)
    return tweets_list

def tweets_per_day(id_in):
    all_tweets = get_tweets(id_in)
    for tweet in all_tweets:
        tw_date = time.strftime('%Y-%m-%d', time.strptime(str(tweet.created_at), '%Y-%m-%d %H:%M:%S'))
    # Still need to count total number of days in range
    # Then count number of occurances for each unique date
    # Then average over total days

def bond_bridge(id_in):
    bonding = 0
    init_friends = get_friends(id_in)
    for friend in init_friends:
        if api.show_friendship(source_id=id_in, target_id=friend)[0].followed_by:
            bonding += 1
        time.sleep(5)
    bridging = api.get_user(id_in).friends_count - bonding
    time.sleep(5)
    return [bonding, bridging]

print init_friend_count
print bond_bridge(init_id)
