import random

magicNum = random.randint(1,10)

guess = int(input("Guess a Number: "))

while magicNum!= guess:
    if guess < magicNum:
        print("Too low")
        guess = int(input("Guess a Number: "))
    elif guess > magicNum:
        print("Too high")
        guess = int(input("Guess a Number: "))
    else: 
        break
print("You guessed the correct number!")

