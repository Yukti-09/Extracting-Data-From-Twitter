import tweepy
import time
from tweepy import OAuthHandler
import pandas as pd   

twitter_keys = {
'consumer_key': '',
'consumer_secret': '',
'access_token_key': '',
'access_token_secret': ''
}

auth = OAuthHandler(twitter_keys['consumer_key'], twitter_keys['consumer_secret'])
auth.set_access_token(twitter_keys['access_token_key'], twitter_keys['access_token_secret'])

api = tweepy.API(auth)

username = 'jack'
count = 150
try:     


 tweets = tweepy.Cursor(api.user_timeline,id=username).items(count)
 

 tweets_list = [[tweet.created_at, tweet.id, tweet.text] for tweet in tweets]

 tweets_df = pd.DataFrame(tweets_list)
except BaseException as e:
      print('failed on_status,',str(e))
      time.sleep(3)

for tweet in tweets_list:
	print(tweet)
