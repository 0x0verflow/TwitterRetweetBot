#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy
from time import sleep

############################
######## RetweetBot ########
############################
# All rights belong to the #
### creator of this file ###
############################
### (C) by 0x0verflow.cf ###
############################


######### Settings #########

consumer_key = 'CONSUMER_KEY'
consumer_secret = 'CONSUMER_SECRET'
access_token = 'ACCESS_TOKEN'
access_token_secret = 'ACCESS_TOKEN_SECRET'

bot_keywords = ["keyword", "#keyword", "@MyBot"]

############################





########## Script ##########

print("[*] Retweet Bot          | V1.0")
print("[*] ---------------------------")
print("[*] by 0x0verflow.cf")
print("")
print("")

print("[I] Starting up...")


#?> Login
print("[I] Trying to log into Twitter. There is no error message, so just hope the best!")

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

print("[I] Login done... Ah shit, here we go again!")
print("[I] Using account: \"" + api.me().name + "\" (Aaaand that's the point, where you see, if it's working.)")

sleep(2)


#?> Starting search loop
print("[I] Starting check loop...")

sleep(5)

while 1:
    for keyword in bot_keywords:
        print("")
        print("")
        print("[I] -> Checking Keyword: \"" + keyword + "\" (Waiting 20s before checking...)")
        sleep(20)
        for tweet in tweepy.Cursor(api.search, keyword, lang='de').items(10):
            print("")
	    print("")
            print("------------------ Check ------------------")
            try:
                print("[I] Trying to retweet found tweets...")
                tweet.retweet()
		tweet.favorite()
                print("[I] Tweet retweeted: \n    -> " + tweet.text)
		print("-------------------------------------------")

            except tweepy.TweepError as e:
                print("[E] Tweet could not be retweeted (or is it already?):")
                print("    -> " + e.reason)
		print("-------------------------------------------")

            except StopIteration:
                break


print("[I] Exiting...")
sleep(10)
