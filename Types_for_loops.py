#basic for loop construction
fruits =['apple','grape','cherry']
for fruit in fruits:
    print(fruit)

pets =['cat','dog','fish']
for x in pets:
    print(x)


#to count to 100 with a for loop 
for number in range(100):
    print(number)



""" letys use a Break to exit a loop """

prompt = "n\Tell me the name of a city you have visited. "
prompt += "n\enter quit when you are finished. "

while True:
    city = input(prompt)

    if city == 'quit' :
        break
    else:
        print("I'd love to go to " + city.title() + "!")




