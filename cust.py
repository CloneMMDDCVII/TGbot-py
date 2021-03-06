import urllib.request #needed to make request over the internet
import json #needed to parse the json files returned by telegram
import urllib.parse #allows to make http request with diverse characters
import cust #my custom functions
import settings #different bot settings, and onetime used variables
import api

BotToken = str(settings.token())

ApiUrl = ("https://api.telegram.org/bot"+BotToken+"/")

Offset= settings.offset()

def ask():
	return int(input())

def askChat(): #allows the use of nicknames when testing
	return settings.chats(str(input()))

def proceed(sendrequest):#process the request as needed. It was stupid to have it in every single function.
	print(ApiUrl+sendrequest)
	urllib.request.urlopen((ApiUrl+sendrequest))

def str2http(string):#turns a string to a url friendly format
	return urllib.parse.quote(string)	
