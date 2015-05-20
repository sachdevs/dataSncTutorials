import tweepy
from loginDetails import consumer_key, consumer_secret, access_token, access_token_secret
import warnings
import matplotlib

warnings.filterwarnings("ignore")

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print tweet.text.encode('utf-8')

print '\n\n\n'

user = api.get_user('twitter')

print user.screen_name
print user.followers_count
for friend in user.friends():
   print friend.screen_name