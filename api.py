import urllib.request #needed to make request over the internet
import json #needed to parse the json files returned by telegram
import urllib.parse #allows to make http request with diverse characters
import cust #my custom functions
import settings #different bot settings, and onetime used variables
import api

def SendMessage(id,text):#self explanatory, ain't it?
	Url=("sendMessage?chat_id="+str(id)+"&text="+str(text))
	cust.proceed(Url)

def SendChatAction(id,action):#check telegram's bot api documentation for inputable
	Url=("sendChatAction?chat_id="+str(id)+"&action="+str(action))
	cust.proceed(Url)

def Button():
	print("button text")
	text="%22text%22%3A%22"+cust.str2http(input())+"%22"
	print("data type : url, callback_data, callback_query")
	print("data content")
	data="%22"+cust.str2http(input())+"%22%3A%22"+cust.str2http(input())+"%22"
	button = "{"+text+","+data+"}"
	return button

def BuildKeyboardLine(i):
	a=1
	Line = "["
	while a <= i:
		button = Button()
		if a != i:
			button = button + ","
		Line = Line+button
		a=a+1
	Line = Line + "]"
	return Line

def BuildKeyboard(i, j):
	a=1
	full = "&reply_markup={%22inline_keyboard%22:["
	while a <= i:
		keyboard = BuildKeyboardLine(j)
		if a != i:
			keyboard = keyboard + ","
		full = full+keyboard
		a=a+1
	full = full + "]}"
	return full
	
def SendKeyboard(id, text):#just a simple, basic keyboard. I might make it better by creating a function that would create the json object before, it would allow me to make multi buttons messages. In addition, I still need to figure out how callback data works. I really suck at this.
	Url=("sendMessage?chat_id="+str(id)+"&text="+cust.str2http(text)+BuildKeyboard(cust.ask(), cust.ask()))
	cust.proceed(Url)
