#Tuples 
#Are a list that is static and does not change you use () to define a Tuple and not [] like a list
dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

#Loop through a tuple
for dimention in dimensions:
    print(dimention)

#Writing over a tuple
#the old dimentions are 200 50 so we will call that first 
#lines 14 thrigh 16 call the old dimentions to ensure they are 200 50
print("original dimetions:")
for dimention in dimensions:
    print(dimention)

#lines 19 through 22 show are are changing the dimetions to 400 100 and printout the new set in the tuple
dimensions = (400, 100)
print("\nModified dimintions:")
for dimention in dimensions:
    print(dimention)




