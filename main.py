import urllib.request #needed to make request over the internet
import json #needed to parse the json files returned by telegram
import urllib.parse #allows to make http request with diverse characters
import cust #my custom functions
import settings #different bot settings, and onetime used variables


BotToken = str(settings.token())
ApiUrl = ("https://api.telegram.org/bot"+BotToken+"/")
Offset= settings.offset()


def askChat(): #allows the use of nicknames when testing
	return settings.chats(str(input()))

def proceed(sendrequest):#process the request as needed. It was stupid to have it in every single function.
	print(sendrequest)
	urllib.request.urlopen((sendrequest))

def str2http(string):#turns a string to a url friendly format
	return urllib.parse.quote(string)	

def apiSendMessage(id,text):#self explanatory, ain't it?
	Url=(ApiUrl+"sendMessage?chat_id="+str(id)+"&text="+str(text))
	proceed(Url)

def apiSendChatAction(id,action):#check telegram's bot api documentation for inputable actions
	Url=(ApiUrl+"sendChatAction?chat_id="+str(id)+"&action="+str(action))
	proceed(Url)

def apiSendKeyboard(id, text, button):#just a simple, basic keyboard. I might make it better by creating a function that would create the json object before, it would allow me to make multi buttons messages. In addition, I still need to figure out how callback data works. I really suck at this.
	Url=(ApiUrl+"sendMessage?chat_id="+str(id)+"&text="+str2http(text)+"""&reply_markup={%22inline_keyboard%22:[[{"text":%22"""+str2http(button)+"""","callback_data":"data"}]]}""")
	proceed(Url)

#===========================================================#
#    This is a code sample of jarvis, the know it all bot   #
#    I know. It's not original. But who cares               #
#===========================================================#
#apiSendChatAction(askChat(), "typing")
#apiSendMessage(askChat(), str(input()))
#apiSendKeyboard(askChat(), input(), input())

exit()
