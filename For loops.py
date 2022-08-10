#This is all about loops and howe to use them this is the bread and butter of things here

#A basic for loop
shapes = ['circle','square','triangle']

for shape in shapes:
    print(shape)
#A good rule of thumb is to name yur list as a plural for example 
#for cat in cats. Cats would be your list so the cat is the start of the for loop 
#for cat in cats, for dog in dogs, for item in items

#Add a message to a for loop 
names = ['aika','daniel','william']
for name in names:
    print(name.title() + ", is my favorit name today!")

#You can add as many lines of code as you want 
pigs = ['porky pig','piggy pig','fatty pig','skinny pig']
for pig in pigs:
    print(pig.title() + ", sure did taste good!")
    print("I hope the next pig that goes to market tasts as good as " + pig.title() + ".\n") #HINT ".\n" this creates a new line
#Look close you can see that all the line of code here are indented that is because it's a code block and loops all must follow code block rules
#You have haev all your following lins after the start of the loop indented like lines 20 and 21 here 

#Do something afte ther loop 
pigs = ['porky pig','piggy pig','fatty pig','skinny pig']
for pig in pigs:
    print(pig.title() + ", sure did taste good!")
    print("I hope the next pig that goes to market tasts as good as " + pig.title() + ".\n")

print("Thank you for the wonderfull dinner wife!")

