""" The input function waits for user input it looks like this input() """

message = input("Please tell me your name. ")
print(message)

test = input("What kind of pet do you have a cat or a dog? ")
print(test)

""" How to capture data from the user  and insert a vaerble from the perivios question"""
question = input("What is the color of your " + test + " ?")



""" you can also add these all together like so """
print( message + " I have a "  + test + " too I like them. I have never seen a " + question + " colored " + test + " before very cool. ")

