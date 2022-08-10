#Number lists
# Range Function. This is a for loop for number but use the range instead of calling items like cat in cats 
for value in range(1,10):
    print(value)
# You can see the indentation and see the formillur structure of the for loop
# 10 is not printed as all list start with 0 so counting up from 0 to 10 you end on 9
#0,1,2,3,4,5,6,7,8,9 that is 10 places

#Make a list of nmumbers using range and store that list 
numbers = list(range(1,6))
print(numbers)

#Make a list of even numbers only 
even_number = list(range(2,11,2))
print(even_number)
#The function start with 2 and then adds 2 to that vaule untill it reaches 11 
#odd numbers are bit harder to create 
