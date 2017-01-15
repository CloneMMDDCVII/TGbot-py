import urllib.request #needed to make request over the internet
import json #needed to parse the json files returned by telegram
import urllib.parse #allows to make http request with diverse characters
import cust #my custom functions
import settings #different bot settings, and onetime used variables
import api

BotToken = str(settings.token())
ApiUrl = ("https://api.telegram.org/bot"+BotToken+"/")
Offset= settings.offset()









#===========================================================#
#    This is a code sample of jarvis, the know it all bot   #
#===========================================================#
api.SendChatAction(cust.askChat(), "typing")
api.SendMessage(cust.askChat(), str(input()))
api.SendKeyboard(cust.askChat(), input(), input())

exit()
