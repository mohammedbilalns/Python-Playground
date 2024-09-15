
import tweepy
from textblob import TextBlob

consumer_key = "pWIW3LTFn3ifZ4TVwmdx3hXVy"
consumer_secret = "lnwUldFYSNWXNcnuojHtE2MIOEO0osAJU21kOxxnoZFWnkaZFf"

access_token = "AAAAAAAAAAAAAAAAAAAAAJ4fsAEAAAAAQ%2BSi3X9Fdwl8ooO5VIcotYAPIm8%3DRStkfYtR22LqwyrKVv7oll6MkODFjAaH3iOjAcB5JHzgxpUmHe"
access_token_secret = "9GUxSUQ7s5dgLaG09Aq04DsSz1WBNjZlIuPzuCnl6uDom"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search_tweets("babari")

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
