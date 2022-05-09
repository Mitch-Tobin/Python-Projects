# DRAGON REALM

import random
import time

def displayIntro():
    print("You are in a land full of dragons... in front of you, you will see two caves.")
    print("In one cave, the dragon is friendly...and will share his treasure with you.")
    print("In the other cave, the dragon is greedy and hungry, and will eat you on sight!")

def chooseCave():
    cave = ''
    while cave != '1' and cave != '2':
        print("Which cave would you like to enter? (1 or 2)")
        cave = input()
    return cave

def checkCave(chosenCave):
    print("You approach the cave...")
    time.sleep(2)
    print("It's very dark and spooky...")
    time.sleep(2)
    print("A large dragon JUMPS OUT AT YOU AND...")
    print()
    time.sleep(2)

    friendlyCave = random.randint(1,2)
    if chosenCave == str(friendlyCave):
        print("gives you some of his treasure!  He is very friendly")
    else:
        print("gobbles you down in one bite!  RIP")

playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':
    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)

    print("Would you like to play again? (yes or no)")
    playAgain = input()