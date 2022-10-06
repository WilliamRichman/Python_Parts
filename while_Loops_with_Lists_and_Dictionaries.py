#a list of of confirmed uuser and an empty list to put them in after they are confirmed
from timeit import repeat
from urllib import response


unconfirmed_users = ['willima','aigerim','daniel']
confirmed_users = []

#move the unconfirmed users to the comfirmed list and use the pop method
while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("Verifying users: " + current_user.title())
    confirmed_users.append(current_user)
    #the above creates a new vcariabl called current_user 
    #Then it pulls names from the unconfirmed_users list using .pop this starts at the end of the list so daniel will now be first in the confirmed_users list
    #it then appends the .pop object in this case daniel and puts it in the confirmed_users list
    
    #display all confirmed users
    print("n\These users have been confirmed:")
    for confimed_user in confirmed_users: 
        print(confimed_user.title())

#the above runs from line 2 to 18


""" Removing all instances of a specific value from a list """
#list name is pets 
pets = ['dog','cat','goldfish','cat','bird','cat','hamster']
print(pets)

while 'cat' in pets:
    pets.remove('cat')

print(pets)
#This removes all cats form the list 


""" filling a dictionare with user input """
#The below is broken not working 

#lets fill a dictionare with names that we prompt for 
#empty dictionary 
responses = {}

#setting a flag to True 
polling_active = True

while polling_active:
    name = input("What is your first name? ")
    response = input("do you like cats or dogs? ")

    #store the response in the dictionary
    responses[name] = response

    #repeat the question for the next user if there is one if not exit 
    repeat = input("Is there anyone else that would like to take the servay? If there is no one else type no")
    if repeat == 'no':
        polling_active = False

#polling is complete. Show the results 
print("n\ ---- Polling Results ---- ")
for name, response in responses.item():
    print(name + "likes " + response + ".")


#The above is broken not working 


""" Lets fix the above """

replies = {}

polling_active = True

while polling_active:
    name = input("What is your first name? ")
    reply = input("Do you like cats of Dogs? ")

    replies[name] = reply

    print(replies)

    repeat = input("Is there anyone else that wants to take the survay? if not type no. ")
    if repeat == 'no':
        polling_active = False

#The above asks for and captures that data 
#show the data

print("----Polling Results ----")
for name, reply in replies.items():
    print(name + "likes " + reply + "! ")

""" The above is fixed """

