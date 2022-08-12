#Slicing through lists 
players = ["will","aika","daniel","joe","bob"]
print(players[0:3])
print(players[2:4])

#For loop using slicing
for player in players[:3]:
    print(player.title())
#This is short hand using a for loop to get the first 3 players of the list

