#!/usr/bin/env python

import json
import tweepy

#---------AUTH STUFF----------------------------
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
#---------------------------------------------------


#------------------------------------------
# Setting up Stream feed
#------------------------------------------

class Listening(tweepy.StreamListener): ###this code taken from the Tweepy documentation and dataquest.io
	def on_error(self, status_code): ##if we get an error e.g. rate limited, disconnects and tells us
		if status_code == 420:
			return False
			print(status_code.text)
	def on_data(self, data): ##a function for when we get data
		with open('rawdata.json','a') as f: ###open a json dump file for our data
			f.write(data) ## write our data to our file
			f.close()

stream = tweepy.Stream(api.auth, listener=Listening()) ##setting up the stream, see Tweepy documentation
stream.filter(track=["toronto"],languages=['en']) #filtering our stream by search term and language, see https://dev.twitter.com/streaming/overview/request-parameters for parameters
