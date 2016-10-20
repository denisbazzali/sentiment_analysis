from textblob import TextBlob
import tweepy
import csv

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


def categorize(polarity):
    if polarity <= -0.20:
        return 'Negative'
    if polarity >= 0.20:
        return 'Positive'
    return 'Neutral'


with open('tweets.csv', "w", newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
    writer.writerow(("Username", "Tweet", "Polarity", "Classification"))
    for tweet in public_tweets:
        username = tweet.user.screen_name
        polarity = TextBlob(tweet.text).sentiment.polarity
        label = categorize(polarity)
        writer.writerow((username, tweet.text, polarity, label))