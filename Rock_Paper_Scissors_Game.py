from multiprocessing import RLock
import random

while True:

    choices = ['rock','paper','scissors']

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("rock, paper, or scissors?: ").lower()

    if player == computer:
        print("The computer selected "+ computer)
        print("You selected "+ player)
        print("Tie! ")
    elif player == "rock":
        if computer == "paper":
            print("The computer selected "+ computer)
            print("You selected "+ player)
            print("You Lose! ")
        if computer == "scissors":
            print("The computer selected "+ computer)
            print("You selected "+ player)
            print("You Win! ")
    elif player == "paper":
        if computer == "scissors":
            print("The computer selected "+ computer)
            print("You selected "+ player)
            print("You Lose!")
        if computer == "rock":
            print("The computer selected "+ computer)
            print("You selcted "+ player)
            print("You Win!")
    elif player == "scissors":
        if computer == "rock":
            print("The computer selected "+ computer)
            print("You selcted "+ player)
            print("You Lose!")
        if computer == "paper":
            print("The computer selected "+ computer)
            print("You selected "+ player)
            print("You Win!")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        break

print("Good Bye!")
    
    

 #Need to add lizard spoke to the to list above and add the print statments as well as the images 
 #rulles
 #//# scissors / paper 
 # //# paper / rock 
 # //# rock / lizard 
 # //# lizared / spock 
 # //# spock / scissors 
 # //# scissors / lizared 
 # //# lizard / paper 
 # //# paper / spock 
 # //# spock / rock
