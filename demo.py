from textblob import TextBlob
import tweepy
import csv
import json


consumer_key = ''
consumer_secret = ''

access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#public_tweets = api.search('Trump')


file = open('today.txt', 'a')

class CustomStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        print(status.text)

    def on_data(self, data):
        json_data = json.loads(data)
        # file.write(str(json_data['text']))
        writeCSV(str(json_data['text']))

sapi = tweepy.streaming.Stream(auth, CustomStreamListener())
sapi.filter(track=['Trump'])

# for tweet in public_tweets:
#     print(tweet.text)
#     analysis = TextBlob(tweet.text)
#     print(analysis.sentiment)


# def categorize(polarity):
#     if polarity <= -0.20:
#         return 'Negative'
#     if polarity >= 0.20:
#         return 'Positive'
#     return 'Neutral'
#
#
def writeCSV(tweet):
    with open('trump.csv', "w", newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
        writer