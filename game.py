"""Guess the number"""

import numpy as np

number = np.random.randint(1,101)

count = 0 # attempts

while True:
    count += 1
    predict_number = int(input("Input number 1 - 100: "))

    if predict_number > number:
        print("Number must be less")
    elif predict_number < number:
        print("Number must be greater")
    else:
        print(f"You guessed the number. This is number = {number}, by {count} attempts.")
        break
