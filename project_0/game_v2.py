"""Guess the number. PC guess the number."""

import numpy as np
from numpy.core.fromnumeric import size

def random_predict(number:int=1) -> int:
    """Guess the number by random

    Args:
        number (int, optional): Guessed number. Defaults to 1.

    Returns:
        int: Count of attempts
    """
    count = 0
    while True:
        count += 1
        predict_number = np.random.randint(1, 101)
        if number == predict_number:
            break
    return count

def score_game(random_predict) -> int:
    """Average count of attepts by 1000 attemts for guess of number.

    Args:
        random_predict ([type]): Guessed function

    Returns:
        int: Average count of attempts
    """
    counts = []
    # np.random.seed(1) # init random seed
    random_array = np.random.randint(1, 101, size=10000)
    for number in random_array:
        counts.append(random_predict(number))
    
    score = np.mean(counts)
    print(f"Your algoritm guess number for {score} attempts.")
    return score

# RUN
if __name__ == '__main__':
    score_game(random_predict)
# print(f"Attempts: {random_predict(10)}")
