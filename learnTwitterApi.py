#import tweepy
import tweepy
import re

#entrer votre key
consumer_key = "ApxncpHwK0dHyQCLkUWkr6nNo"
consumer_secret = "Kqwufe4Rjf9oVvHSoXBXrjwhu2C2TxCuF88YzFnt012DAnSzPv"
access_token = "826785351561781252-hXDFuC7m5o6VhyFabkoBxMHaU07S6ue"
access_token_secret = "0zRJ3mp8JzWUPrVUA1EkgPpgbEP9p0sxFxjE0Bi0LIAUX"
callback_url = "http://www.CallbackAnalysebd.com"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)


#access votre twitter par api
api = tweepy.API(auth)

#obtenir home_data(public)
#filtre = re.compile(u'[\uD800-\uDBFF][\uDC00-\uDFFF]')

#return twieet that user and frends of user, maximum 20 
#id = 832905517437710336
'''

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print tweet.id
    print tweet.text
'''

#Returns full Tweet objects for up to 100 tweets per request, specified by the id parameter.
#chaque tweet has un id
'''
tweet = api.get_status("832905517437710336")
print tweet.text
print tweet.author.screen_name
print tweet.author.id
'''

#---------------------------------------------------------------------
'''
#il y a des problem
#the Search index doesn't go back further than 7-10 days, n'import pages() ou items()
for tweet in tweepy.Cursor(api.search,q='Dolirhume').items(1000):
    print tweet.text
    print tweet.created_at


i=0
for tweet in tweepy.Cursor(api.search,q='Dolirhume').pages(1000):  
    for tw in tweet:   
        print tw.text
        print tw.created_at
        i = i+1
print i
'''
#----------------------------------------------------------------------
# il y a des problems
'''
tweetObj = api.statuses_lookup('832884892937629696')
print len(tweetObj)
for tweet in tweetObj:
    print tweet.text
'''





