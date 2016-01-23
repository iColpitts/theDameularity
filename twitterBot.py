import tweepy, datetime, sys
import random
import twitterKeys
 
class TwitterAPI:
    def __init__(self):
        auth = tweepy.OAuthHandler(twitterKeys.consumer_key, twitterKeys.consumer_secret)
        auth.set_access_token(twitterKeys.access_token, twitterKeys.access_token_secret)
        self.api = tweepy.API(auth)
 
    def tweet(self, message):
        self.api.update_status(status=message)



firstList = open('pulpNovels.txt','r')
secondList = open('finish.txt', 'r')

first = firstList.readlines()
second = secondList.readlines()
first = [n.replace('\n', '') for n in first]
firstList.close()
secondList.close()

tweet = random.choice(first) + random.choice(second) + "#theDameularity"   

twitter = TwitterAPI()
twitter.tweet(tweet)



     