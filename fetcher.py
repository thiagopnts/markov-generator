import tweepy
import os

auth = tweepy.OAuthHandler(os.environ['CONSUMER_KEY'], os.environ['CONSUMER_SECRET'])
auth.set_access_token(os.environ['ACCESS_TOKEN'], os.environ['ACCESS_TOKEN_SECRET'])
 
api = tweepy.API(auth)
tweets = open('tweets.txt', 'w')
tweets.writelines([status.text.encode('utf-8') for status in api.user_timeline('thiagopnts', count=5000)])
tweets.close()

