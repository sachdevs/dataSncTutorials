import tweepy
from loginDet import consumer_key, consumer_secret, access_token, access_token_secret
import warnings
import matplotlib

warnings.filterwarnings("ignore")

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

class StreamListener(tweepy.StreamListener):
    def on_status(self, status):
        print(status.text).encode('utf-8')
    def on_error(self, status_code):
        if status_code == 420:
            #returning False in on_data disconnects the stream
            return False
        print status_code.encode('utf-8')

streamListener = StreamListener()
stream = tweepy.Stream(auth=api.auth, listener=streamListener)
(stream.filter(track=[u'basketball'])).encode('utf-8')
