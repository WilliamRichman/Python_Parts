""" The input function waits for user input it looks like this input() 
any time you use the input() python will see it as a string so if you are going to capture numbers
make sure to use the int() and not input()"""

message = input("Please tell me your name. ")
print(message)

test = input("What kind of pet do you have a cat or a dog? ")
print(test)

""" How to capture data from the user  and insert a vaerble from the perivios question"""
question = input("What is the color of your " + test + " ? ")



""" you can also add these all together like so """
print( message + " I have a "  + test + " too I like them. I have never seen a " + question + " colored " + test + " before very cool. ")



""" Try to make an if elseif out the test question with differante answers """
""" You will need to use the int() to capture numbers  """
""" This will return a string and not an int """

""" age_mistake = input("How old are you? ") 

age_correct = int("How old are you? ") """


""" If you run the above you will see one is a string and one is an int """

""" lets use these in an if esle  """
""" The below I ask the user for input and save it as a string but then pass it to the int() and make it a number  """
height = input("How tall are you in inches? ")
height = int(height)

print(height)

if height >= 36:
    print("n\Your tall enough to ride this ride. ")
else:
    print("n\Your to short come back whne you have grow more. ")
