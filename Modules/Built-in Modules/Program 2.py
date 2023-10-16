# Creating a guessing game using sys module
# Name = Indrajeet Mondal; Date = 16th October 2023
# SourceCode

from random import randint

answer = randint(1, 10)

while True:
    try:
        guess = int(input("Guess a number between 1 to 10:- "))
        if 0 < guess < 11:
            if guess == answer:
                print("Congratulation !!!")
                break
    except ValueError:
        print("Please enter a valid number !!!")
