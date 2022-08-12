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




