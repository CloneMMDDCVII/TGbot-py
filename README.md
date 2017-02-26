Welcome :)
if you have no idea what you're looking at, there are two possibilities :
  1) my code hurts your eyes, in which cases you don't need to go to the doctor, your eyes are fine, my code is not.
  2) my code is the only piece of software you understand. This is my case :D
  
TGbot-py is a piece of code (calling it software might be presomptuous) that's aimed at interracting with both a user on a Telegram Client, and a piece of arduino code (hi @Pierre999 )  that should drive a car. 
The way I am building the code follows the logic of making it work for directing a car, however, the code is dead simple, so you should be able to adapt it for your project.

So, to run the code, add your Telegram Bot token in settings.py (do whatever you want with offset, for now, I don't even know what I wrote it for XD), add your chats id alongside with the username you want to assign, and you're good to go :)

Current functions :
custom functions,
  ask()
    returns a number from user
  askChat()
    asks user for input, checks whether input is a valid nickname, if so, returns corresponding i.
  proceed(url)
    prints query and proceeds it
  str2http(text)
    returns url encoded text
    
main functions
  nothing, just write your code here.

api functions
  sendMessage(id, text)
    sends a message to the chat with specified id
  sendChatAction(id, action)
    sends corresponding action to the specified chat (like Bot is typing...)
  Button()
    creates a json button with user input.
  BuildKeyboardLine(number of rows in your line)
    creates a json line of specified number of buttons
  BuildKeyboard(number of lines, number of rows)
    creates a json keyboard by adding up lines created with buildKeyboardLine
  SendKeyboard(id, text)
    still needs to accept more parameters. Sends user created keyboard to specified chat.
