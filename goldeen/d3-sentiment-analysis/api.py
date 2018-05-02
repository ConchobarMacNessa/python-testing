import tweepy
from textblob import TextBlob
import csv
import config

execfile("config.py")

auth = tweepy.OAuthHandler(ENV.TWITTER_KEY, ENV.TWITTER_SECRET)
auth.set_access_token(ENV.ACCESS_TOKEN, ENV.ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

public_tweets = api.search("brexit")

for tweet in public_tweets:
    analysis = TextBlob(tweet.text)
    value = "negative" if analysis.sentiment.polarity < 0 else "positive" if analysis.sentiment.polarity > 0 else "neutral"
    with open("./csv/twitter/test.csv", "a") as f:
        writer = csv.writer(f)
        writer.writerow([tweet.text.encode("utf-8"), value])
