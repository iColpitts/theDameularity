import tweepy, datetime, sys
import random

consumer_key = 	"lnOQmu2WQW2gu37akWIE0y5Yy"
consumer_secret = "KVcJPRh0R2fKgQ7gqPyYeJW4HlvdhSGu27bAd3H5LzvP2ALr9C"
access_token = "4800429799-WJLVZYWgflwjc4SeqsqS54wx474Ck58Xd2bItcc"
access_token_secret = "gDUXqFAKtuF3IxKoldtpSCD6AExD9raZ0yQ058GHzFWlC"
 
class TwitterAPI:
    def __init__(self):
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        self.api = tweepy.API(auth)
 
    def tweet(self, message):
        self.api.update_status(status=message)

toPrint = True

while True:
    current_time = datetime.datetime.now()
    #print current_time
    #print current_time.minute
    #Attributes: hour, minute, second, microsecond, and tzinfo
    
    #if current_time.minute == 00:
        #if toPrint == True:
    print current_time
    #toPrint = False
    if __name__ == "__main__":
        firstList = open('pulpNovels.txt','r')
        secondList = open('finish.txt', 'r')
        
        first = firstList.readlines()
        second = secondList.readlines()
        first = [n.replace('\n', '') for n in first]
        firstList.close()
        secondList.close()

        tweet = random.choice(first) + random.choice(second) + "#theDameularity"   

    #print tweet
    twitter = TwitterAPI()
    twitter.tweet(tweet)
    #elif current_time.minute != 00:
        #toPrint = True
        #print current_time.second



     