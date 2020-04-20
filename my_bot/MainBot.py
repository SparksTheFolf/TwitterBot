import tweepy

from keys import *

print('Hello This is my BOT')


auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)


mentions = api.home_timeline()

for mention in mentions:
    print(mention.created_at)
    print(mention.id_str)
    print(mention.text)
    print('------------------------------------------------------')
    time.sleep(15)