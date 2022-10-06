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


""" use a while loop to count here we go to 5 """
current_number = 1 
while current_number <= 5:
    print(current_number)
    current_number +=1

""" lets count to 100 next """

my_number = 1 
while my_number <= 100:
    print(my_number)
    my_number += 1 