""" Let the user quit the program """

""" This loop keeps running until ity see the message = quit  """

from ast import Break
from asyncore import loop


prompt = "n\Tell me something and I will  reapeat back to you: "
prompt += "n\Enter 'quit' to end the program. "
message = ""
while message != 'quit' :
    message = input(prompt)
    print(message)

""" right now when the user enters quit lets change that so it will run as long as the statment stays true  """

prompt = "n\Tell me something and I will  reapeat back to you: "
prompt += "n\Enter 'quit' to end the program. "

active = True
while active:
    message = input(prompt)

    if message == 'quit' :
        active = False
    else:
        print(message)

""" I can make a very cool little typing program with this to always check the input to output of typing neat programing idea """
""" letys use a Break to exit a loop """

prompt = "n\Tell me the name of a city you have visited. "
prompt += "n\enter quit when you are finished. "

while True:
    city = input(prompt)

    if city == 'quit' :
        break
    else:
        print("I'd love to go to " + city.title() + "!")


