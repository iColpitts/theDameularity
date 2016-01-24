#twitterTest.py
import tweepy, twitterKeys, datetime

# create bot
auth = tweepy.OAuthHandler(twitterKeys.consumer_key, twitterKeys.consumer_secret)
auth.set_access_token(twitterKeys.access_token, twitterKeys.access_token_secret)
api = tweepy.API(auth)

# retrieve last savepoint if available
try:
    idFile = open("lastID.txt", "r")
    lastID = idFile.read()
    idFile.close()
except IOError:
    lastID = ""
    print "No savepoint found. Trying to get as many results as possible."

toSearch = True
while True:
    current_time = datetime.datetime.now()
    if current_time.minute % 05 == 00:
        if toSearch == True:
            # search query
            timelineIterator = tweepy.Cursor(api.search, q="#theDameularity", since_id=lastID, lang="").items()

            # put everything into a list to be able to sort/filter
            timeline = []
            for status in timelineIterator:
                timeline.append(status)

            try:
                lastID = timeline[0].id
            except IndexError:
                lastID = lastID

            tw_counter = 0
            err_counter = 0

            # iterate the timeline and retweet
            for status in timeline:
                try:
                    print "(%(date)s) %(name)s: %(message)s\n" % \
                        { "date" : status.created_at,
                        "name" : status.author.screen_name.encode('utf-8'),
                        "message" : status.text.encode('utf-8') }

                    api.retweet(status.id)
                    tw_counter += 1
                except tweepy.error.TweepError as e:
                    # just in case tweet got deleted in the meantime or already retweeted
                    err_counter += 1
                    #print e
                    continue

            print "Finished. %d Tweets retweeted, %d errors occured." % (tw_counter, err_counter)
            # write last retweeted tweet id to file
            with open("lastID.txt", "w") as file:
                file.write(str(lastID))

            toSearch = False
    elif current_time.minute % 15 != 00:
        toSearch = True

     