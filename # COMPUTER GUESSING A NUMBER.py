# COMPUTER GUESSING A NUMBER

import random
magicNum = random.randint(1, 100)
print(f"The number to guess is {magicNum}")

compGuess = random.randint(1, 100)
tries = 1

while compGuess != magicNum:
    print(f"The computer guessed the number...{compGuess}")
    tries += 1
    if compGuess == magicNum:
        break
    else:
        compGuess = random.randint(1,100)

print(f"The computer guessed the correct number!  The number was {magicNum}")
print(f"It took the computer {tries} guesses to guess the number.")