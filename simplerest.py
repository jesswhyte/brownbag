#!/usr/bin/env python

#---------------------------------------------------------
#importing libraries
#---------------------------------------------------------
import tweepy

#-----------------------------------------------------------------
# Variables that contains the user credentials to access Twitter API
# Go to dev.twitter.com, using your twitter account, to obtain API keys and tokens
# it is not good practice to put your keys in your code. And it's terrible practice to upload them anywhere (like github)
# Check the restauth.py script for example of how to set up a config file for credentials
#-----------------------------------------------------------------

consumer_key = 'yourconsumerkey'
consumer_secret = 'yourconsumersecret'
access_key = 'youraccesskey'
access_secret = 'youraccesssecret'

#authorize twitter, initialize tweepy
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

result_count = 0 # we're going to count the results

for tweet in tweepy.Cursor(api.search, q = "skating, toronto, -RT").items(): #for every tweet returned from this query
		print('Name: ' + tweet.author.name.encode('utf-8') + '\n') #print the author's name, converted to UTF-8, with line break...
		print('Screen Name: ' + tweet.author.screen_name.encode('utf-8') + '\n')
		print('Created: ' + str(tweet.created_at) + '\n')
		print('Tweet: ' + tweet.text.encode('utf-8') + '\n')
		print('-----------------End Tweet #------------------' + '\n')
		result_count +=1 #add 1 to the results count
	
print "got %d results" % result_count #print the number of results

