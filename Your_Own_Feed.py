import tweepy
from tweepy import OAuthHandler

twitter_keys = {
'consumer_key': '',
'consumer_secret': '',
'access_token_key': '',
'access_token_secret': ''
}

auth = OAuthHandler(twitter_keys['consumer_key'], twitter_keys['consumer_secret'])
auth.set_access_token(twitter_keys['access_token_key'], twitter_keys['access_token_secret'])
api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
   print(tweet.text)