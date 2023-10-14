# Practicing on unittest
# Name = Indrajeet Mondal; Date = 14th October 2023
# SourceCode

import random

answer = random.randint(1,10)
while True:
    try:
        guess = int(input("Guess a number between 1 and 10:- "))
        if 0 < guess < 11:
            if(guess == answer):
                print("You are a genius !!")
                break

    except ValueError:
        print("Please enter a number !!")
        continue