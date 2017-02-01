#!/usr/bin/env python

import json
import tweepy

#---------AUTH STUFF---------------
#say where to look for your config file
configfile = open("./twitterConfig.json");
#load your config file as json
config = json.load(configfile)
#point to or translate your key locations in the twitterConfig.json file
consumer_key = config['consumer_key']
consumer_secret = config['consumer_secret']
access_token = config['access_token']
access_secret = config['access_secret']
#authorize, initialize tweepy 
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
api = tweepy.API(auth)
#-------------------------------------

#------------------------------------------
# Setting up Stream feed
#------------------------------------------

class Listening(tweepy.StreamListener): #this code taken from the Tweepy documentation 
	def on_error(self, status_code): #if we get a 420 error (rate limited), disconnects and prints to screen
		if status_code == 420:
			return False #keep going if not a 420 error 
			print(status_code.text)
	def on_data(self, data): #a function for what to do when we get data
		with open('rawdata.json','a') as f: #open a json dump file for our data
			f.write(data) ## write our data to our file
			f.close() #close our file

stream = tweepy.Stream(api.auth, listener=Listening()) #setting up the stream, see Tweepy documentation
stream.filter(track=["toronto"],languages=['en']) #filtering our stream by search term and language, see https://dev.twitter.com/streaming/overview/request-parameters for parameters
