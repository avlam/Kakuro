import numpy as np
import itertools


def combinations(target_sum, n_digits):
    """
    Given a target_sum, and the number of unique integers to use, return set of tuples containing possible number combinations.
    """
    output=set()
#     check if valid
    min_set = tuple(x+1 for x in range(n_digits))
    max_set = tuple(9-x for x in range(n_digits))
    min_sum = sum(min_set)
    max_sum = sum(max_set)
    if (target_sum > max_sum) or (target_sum < min_sum):
        print(f'{target_sum} is invalid for {n_digits}')
    elif target_sum == min_sum:
        print(f'minimum set for {target_sum}')
        output.add(min_set)
    elif target_sum == max_sum:
        print(f'maximum set for {target_sum}')
        output.add(max_set)
    else:
        digits = np.array([i for i in range(1,10)])
        choose = [1 if i<=n_digits else 0 for i in range(1,10)]
        guesses = list(set(itertools.permutations(choose)))
        for guess in guesses:
            if np.matmul(guess,digits) == target_sum:
                combo = guess*digits
                combo = combo[combo != 0]
                output.add(tuple(combo))
    return output
