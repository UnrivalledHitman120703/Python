# Practicing on unittest
# Name = Indrajeet Mondal; Date = 14th October 2023
# SourceCode

import random


def run_guess(guess, answer):
    if 0 < guess < 11:
        if guess == answer:
            print(answer and "You are a genius!")
            return True
    else:
        print("hey bozo, I said 1~10")


answer = random.randint(1, 10)

if __name__ == "__main__":
    while True:
        try:
            guess = int(input("Guess a number 1~10: "))
            if run_guess(guess, answer):
                break
        except ValueError:
            print("Please enter a number")
            continue
