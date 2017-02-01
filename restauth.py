#!/usr/bin/env python

#---------------------------------------------------------
#importing libraries
import tweepy
import json
#---------------------------------------------------------

#tell python where to look for your config file
configfile = open("./twitterConfig.json");

# use json library to load your config file
config = json.load(configfile)

#translate your keys from the json file 
consumer_key = config['consumer_key']
consumer_secret = config['consumer_secret']
access_token = config['access_token']
access_secret = config['access_secret']

#authorize twitter, initialize tweepy
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

result_count = 0 

for tweet in tweepy.Cursor(api.search, q = "-RT, skating, toronto").items(): ##check tweepy documentation and Twitter API doc'n for more
		print('-----------------Start Tweet #------------------' + '\n')
		print('Name: ' + tweet.author.name.encode('utf-8') + '\n')
		print('Screen Name: ' + tweet.author.screen_name.encode('utf-8') + '\n')
		print('Created: ' + str(tweet.created_at) + '\n')
		print('Tweet: ' + tweet.text.encode('utf-8') + '\n')
		print('-----------------End Tweet #------------------' + '\n')
		result_count +=1
		
print "got %d results" % result_count

configfile.close()




