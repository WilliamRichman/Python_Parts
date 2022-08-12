#If Statements allow you to examine the currrent status of a program
#Two if statemnets here one with and one without the key object
fruits = ['apricots','blueberries','cantaloupe','bananas','blackberries','cherries']

#this if statment will come back with CHERRIES
for fruit in fruits:
    if fruit == "cherries":
        print(fruit.upper())
    else:
        print(fruit.title())

#this if statment will come back with retunr with the content of the fruits list
for fruit in fruits:
    if fruit == "blackcurrant":
        print(fruit.upper())
    else:
        print(fruit.title())

#Conditional tests
#this will come back true or false this is not true 
car = 'Toyota'
car == 'bmw'

#this will also not be true due to the case 
car == "toyota"
#how to fix this 
car.lower() == "toyota"

#Checking for Inequality just add != This now comes back as True
car != "Honda"

#Compairing numbers 
#You can include math comairisons <, <=, >, >=
age = 16

if age != 21:
    print("They are to young to drink")

answer = 45

if answer != 50:
    print("That Answer Is Incorreect Please Try Again")

#Checking Multiple conditions 
age_0 = 22
age_1 = 18
age_0 >= and age_1 >= 21
#this comes back false

#Using or to check conditions 
age_0 >= or age_1 >= 25


#Check to see if a value is in a list
requested_toppings = ['cheese','olives','beef','chicken'] 

'mushrooms' in requested_toppings

'olives' in requested_toppings


#Checking Weather a vaule is not in a list
banned_users = ['billy','johny','daniel','aika','jorge']
user = 'william'

if user not in banned_users:
    print(user.title() + ", you may play if you wish.")
    



