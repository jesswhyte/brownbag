#!/usr/bin/env python

#import libraries
import tweepy
import json

#tell python where to look for your config file
configfile = open("./twitterConfig.json");

# use json library to load your config file
config = json.load(configfile)

#translate your keys from the json file 
consumer_key = config['consumer_key']
consumer_secret = config['consumer_secret']
access_token = config['access_token']
access_secret = config['access_secret']

#authorize,initialize tweepy
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)

result_count = 0 #we're going to count our results, so set counter to 0

with open("mydata.json", 'a') as f: #make mydata.txt our dump file, and we're appending to it ('a')
	# for every tweet returned from this query, increase the results count, and dump returned data to a json file
	for tweet in tweepy.Cursor(api.search, q = "-RT, skating, toronto").items(): 
			result_count +=1
			json.dump(tweet._json, f) #dump it, add ,indent=4 to make it prettier
			f.write("\n") ##line break 
			
	
print "got %d results" % result_count #print the total

configfile.close() #close our files
f.close()


