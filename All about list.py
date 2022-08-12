#All about list and how to use them
colors = ['red','green','blue','yellow','pink','light green']


#Pint each item from the list by calling its index 
print(colors[4])
print(colors[2])


#You can add methoods to this exp 
print(colors[4].title())

#You can ask for the last item in a list using the -1 
print(colors[-1].title())

#How to use this
message = "My favorit color is " + colors[-1].title()+ "."
print(message)


#How to change the value of an item in a list
anies = ['cat','dog','fish','bird']
print(anies)

#How to replace an element here i replace cat with lizard
anies[0] = 'lizard'
print(anies[0])

#Use the append command here I add chickes to the list
anies.append('chickens')
print(anies)

#How to insert items into a list I give it the position of 1
anies.insert(1,'bugs')
print(anies)

#How to remove elements from a list here I will delet bugs in position 1 
del anies[1]
print(anies)

#The POP methood / POP allows you  to remove the last item in a list but it keeps teh value so you can still use it later 
bikes = ['bmx','moutin','street']
print(bikes)

popped_bikes = bikes.pop()
print(bikes)
print(popped_bikes)

#You can sort a list alphabetically
colors = ['red','green','blue','yellow','pink','light green']
colors.sort() #This is a methood look closely 
print(colors)

#Sort a list temporarily 
ppp = ['tree','dog','hat']
print("Here is the PPP list unsorted:")
print(ppp)

print("\nHere is the sorted list:")
print(sorted(ppp)) #this is a function look closely


#Print a list in revers 
print(ppp)
ppp.reverse()
print(ppp)


#Find the lenght of a list "How man items are in it"
print(ppp)
len(ppp)


#How to loop through a slice 
players = ['william','daniel','aigerim','stacy','joy','wilbur']
print("Here are the first three 4 players:")
for player in players[:4]:
    print(player.title())

#Copy a list
my_foods =['chicken','corn','hot dogs','ice cream',]
friend_foods = my_foods[:] #Hint you can filter from here as well
print("My favorit foods are:")
print(my_foods)

print("\nMy friends favorit foods are:") #Hint no space \nMy for new line
print(friend_foods)




