# COMP GUESSING P2

import random

def guess():
    magicNum = random.randint(1, 10)
    print(f"The number to guess is {magicNum}")
    compGuess = random.randint(1,10)
    
    tries = 1
    
    if compGuess == magicNum:
        print("WOW!  The computer guessed it on the first attempt!  Lucky computer!")
        print(f"The number was... {magicNum}")

    while compGuess != magicNum:
        print(f"The computer guessed {compGuess}")
        tries += 1
        if compGuess == magicNum:
            print(f"The computer guessed it correctly!")
            break
        else:
            if tries == 5:
                print(f"The computer has ran out of guesses.")
                break
            else:
                compGuess = random.randint(1, 10)
guess()

