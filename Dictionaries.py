#Simple Dictionary
allens = {'color' : 'green', 'points' : 5}
print(allens['color'])
print(allens['points'])


#Adding new key value pairs 
allens_0 = {'color':'red', 'points': 5}

allens_0['x_position'] = 0
allens_0['y_position'] = 25
print(allens_0)


#Looping through the Key Value Pairs 
user_0 = {
    'username':'goat1120',
    'firstname':'william',
    'lastname':'richman',
    }
for key, value in user_0.items():
    print("\nkey" + key)
    print("value" + value)
