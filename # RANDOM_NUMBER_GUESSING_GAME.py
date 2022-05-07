# RANDOM_NUMBER_GUESSING_GAME

from random import randrange

randomNum = randrange(1,11)  #Gives us a random number from the range 1-10 and stores it in randomNum variable.  


turnNum = 1
gameover = False

while turnNum <= 3 and gameover == False:
    
    
    guess = input("What number am I thinking of?")
    guess = int(guess)
    
    if guess == randomNum:
        print("Congratulations!  You win!")
        gameover = True

    if guess > randomNum:
        print("Woah there partner, that guess is too high.")
    
    if guess < randomNum:
        print("Gonna need you to guess a number a little bit bigger next time.")
        
    turnNum += 1
    
if gameover == False:
    print("Too bad, the number was: " + str(randomNum))