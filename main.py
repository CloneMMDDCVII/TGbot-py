import urllib.request #needed to make request over the internet
import json #needed to parse the json files returned by telegram
import cust
import settings
#BotSettings


BotToken = str(settings.token())
ApiUrl = ("https://api.telegram.org/bot"+BotToken+"/")
Offset= settings.offset()


#print(ApiUrl)





def apiSendMessage(id,text):
	sendrequest=(ApiUrl+"sendMessage?chat_id="+str(id)+"&text="+str(text))
	print(sendrequest)
	urllib.request.urlopen(sendrequest)


#def onmessage(msg, chat_id, user_id)

#if msg=="move":
	

#===========================================================#
#    This is a code sample of jarvis, the know it all bot   #
#===========================================================#

apiSendMessage(settings.chats(str(input())), str(input()))

exit()
print("Please enter text")
text=input()
print("please enter chat ID")
id=input()
