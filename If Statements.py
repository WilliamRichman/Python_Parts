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
    

#If Else statement "simple"
ages = 17
if ages >= 18:
    print("You are old enought to vote!")
    print("Have you registared to vote?")
else:
    print("Sorry your to youge to vote")
    print("Register when you turn 18")


#The if-elif-else chain
#this will evaluate all the set conditions to find the first true and do that action

#Notes admission 
#4 and under is free
#4 to 18  $5
#18 and older is $10

agea = 12
if agea < 4:
    print("Your admission is free")
elif agea < 18:
    print("Your admission is cost is $5.00")
else:
    print("Your admission price is $10.00")

#The better way to write this script block 
ageb = 13
if ageb < 4:
    price = 0
elif ageb < 18:
    price = 5
else :
    price = 10

print("Your admission cost is $" + str(price) + ".")


#Testing Multipul Conditions
required_tools = ['hammer','screw driver','drill']

if 'drill' in required_tools:
    print("Add a drill to your tool bag")
if 'bits' in required_tools:
    print("Add the dill bit index to your tool bag")
if 'saw' in required_tools:
    print("Add a saw to you tool bag")

print("\nFinshed packing your tool bag!")
#this only added the adda drill to your tool bag because its the only one in the list
#the rest were not in the list so as the loop ran the saw and bits came back false 
#only true objects from the list were printed
