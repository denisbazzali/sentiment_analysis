from textblob import TextBlob
import tweepy

consumer_key = 'n9yef3PmnYD6Yr7YTnODXswW4'
consumer_secret = 'uLCkrM62ucxpbqVwEAH5sWkcnIwWsMgvjT9uzDrNn3FkjRAYVM'

access_token = '287121416-6G1bB8c5X9c6NMTQwRTkacPgGtRmdV7JU8tOCPYq'
access_token_secret = 'KxSfTVDIVkKtho8jbZguiUG3HXbluQENg6qw38xIPrjJC'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.search('Trump')

for tweet in public_tweets:
    print(tweet.text)
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)