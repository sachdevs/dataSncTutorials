import tweepy
from loginDet import consumer_key, consumer_secret, access_token, access_token_secret
import warnings
import matplotlib

warnings.filterwarnings("ignore")

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

afinn = {}
file = open('AFINN-111.txt')

for line in file:
    key, value = line.split('\t')
    val = (int)(value.replace("\n", ""))
    afinn[key] = val

def sentimentCalc(tweet):
    arr = tweet.split(" ")
    sent = 0
    for word in arr:
        if word in afinn:
            sent += afinn[word]
    return sent


class StreamListener(tweepy.StreamListener):
    def on_status(self, status):
        out = (str)(sentimentCalc((status.text).encode('utf-8')))
        print out
        print (status.text).encode('utf-8')
        f = open('data.txt', 'a')
        f.write(out+'\n')

    def on_error(self, status_code):
        if status_code == 420:
            #returning False in on_data disconnects the stream
            return False
        print status_code.encode('utf-8')

streamListener = StreamListener()
stream = tweepy.Stream(auth=api.auth, listener=streamListener)
(stream.filter(track=['rap'], languages=["en"])).encode('utf-8')
#track=[u'obama'], locations=[-180,-90,180,90],