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

def SendKeyboard(id, text, button, data):#just a simple, basic keyboard. I might make it better by creating a function that would create the json object before, it would allow me to make multi buttons messages. In addition, I still need to figure out how callback data works. I really suck at this.
	Url=("sendMessage?chat_id="+str(id)+"&text="+cust.str2http(text)+"""&reply_markup={%22inline_keyboard%22:[[{"text":%22"""+cust.str2http(button)+"""","url":%22"""+data+"%22}]]}")
	cust.proceed(Url)