"""Guess the number. PC guess the number."""

import numpy as np


def random_predict(number: int = 1,
                   min_number: int = 1,
                   max_number: int = 101) -> int:
    """Guess the number by half-devide method

    Args:
        number (int, optional): Guessed number. Defaults to 1.

    Returns:
        int: Count of attempts
    """

    # min_number, max_number = 1, 101
    count = 0
    # if number == min_number or number == max_number:
    #     return 1
    while True:
        count += 1
        predict_number = (max_number + min_number) // 2
        if number == predict_number:
            break
        elif number > predict_number:
            min_number = predict_number
        elif number < predict_number:
            max_number = predict_number
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
    min, max = 1, 101
    random_array = np.random.randint(min, max, size=10000)
    for number in random_array:
        counts.append(random_predict(number, min_number=min, max_number=max))

    score = np.mean(counts)
    print(f"Your algoritm guess number for {score} attempts.")
    return score


# RUN
if __name__ == '__main__':
    score_game(random_predict)
