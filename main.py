import urllib.request #needed to make request over the internet
import json #needed to parse the json files returned by telegram
import urllib.quote #allows to make http request with diverse characters
import cust #my custom functions
import settings #different bot settings, and onetime used variables


BotToken = str(settings.token())
ApiUrl = ("https://api.telegram.org/bot"+BotToken+"/")
Offset= settings.offset()


def askChat():
	return settings.chats(str(input()))
def proceed(sendrequest):
	print(sendrequest)
	urllib.request.urlopen(urllib.quote(sendrequest))

def apiSendMessage(id,text):
	Url=(ApiUrl+"sendMessage?chat_id="+str(id)+"&text="+str(text))
	proceed(Url)

def apiSendChatAction(id,action):
	Url=(ApiUrl+"sendChatAction?chat_id="+str(id)+"&action="+str(action))
	proceed(Url)


#===========================================================#
#    This is a code sample of jarvis, the know it all bot   #
#===========================================================#
apiSendChatAction(askChat(), "typing")
apiSendMessage(askChat(), str(input()))

exit()
print("Please enter text")
text=input()
print("please enter chat ID")
id=input()
