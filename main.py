import urllib.request #needed to make request over the internet
import json #needed to parse the json files returned by telegram
import urllib.parse #allows to make http request with diverse characters
import cust #my custom functions
import settings #different bot settings, and onetime used variables
import api #all basic functions are now stored in api.py










print("""#===========================================================#
#    TGBot-py by BrokenClock  V0.03 non-interractive mode   #
#===========================================================#""")
#===========================================================#
#    This is a code sample of jarvis, the know it all bot   #
#===========================================================#
#api.SendChatAction(cust.askChat(), "typing")
#api.SendMessage(cust.askChat(), str(input()))
api.SendKeyboard(cust.askChat(), input(), input(), input())

exit()
