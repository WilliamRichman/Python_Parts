#All about list and how to use them
colors = ['red','green','blue','yellow','pink','light green']


#Pint each item from the list by calling its index 
print(colors[4])
print(colors[2])


#You can add methoods to this exp 
print(colors[4].title())

#you can ask for the last item in a list using the -1 
print(colors[-1].title())

#how to use this
message = "My favorit color is " + colors[-1].title()+ "."
print(message)


#how to change the value of an item in a list
anies = ['cat','dog','fish','bird']
print(anies)

#How to replace an element here i replace cat with lizard
anies[0] = 'lizard'
print(anies[0])

#use the append command here I add chickes to the list
anies.append('chickens')
print(anies)

#How to insert items into a list I give it the position of 1
anies.insert(1,'bugs')
print(anies)

#how to remove elements from a list here I will delet bugs in position 1 
del anies[1]
print(anies)

#The POP methood / POP allows you  to remove the last item in a list but it keeps teh value so you can still use it later 
bikes = ['bmx','moutin','street']
print(bikes)

popped_bikes = bikes.pop()
print(bikes)
print(popped_bikes)

