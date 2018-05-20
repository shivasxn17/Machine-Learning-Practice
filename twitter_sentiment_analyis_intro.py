# create twitter app
# pip install tweepy , textblob
import tweepy
from textblob import TextBlob as tb
import csv

# keys to access twitter app
consumer_key = ''
consumer_secret = ''

access_token = ''
access_token_secret = ''

# twitter API access
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)
api = tweepy.API(auth)

trump_tweets = api.search('Election')

tweet_dataset = open("datasets/tweet_dataset.csv",'w')

with tweet_dataset:
    analysis_sentiments = []
    writer = csv.writer(tweet_dataset)
    for tweet in trump_tweets:
    	analysis = tb(tweet.text)
    	writer.writerow([tweet.text,analysis.sentiment])

print('dataset ready')
