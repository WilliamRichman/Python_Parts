#Simple Dictionary
allens = {'color' : 'green', 'points' : 5}
print(allens['color'])
print(allens['points'])


#Adding new key value pairs 
allens_0 = {'color':'red', 'points': 5}

allens_0['x_position'] = 0
allens_0['y_position'] = 25
print(allens_0)


#Looping through the Key Value Pairs 
user_0 = {
    'username':'goat1120',
    'firstname':'william',
    'lastname':'richman',
    }
for key, value in user_0.items():
    print("\nkey" + key)
    print("value" + value)


""" lets fill an empty dictionary wityh user responses  """
#lets fill a dictionare with names that we prompt for 
#empty dictionary 
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
