#  Create a function that takes a list of numbers, including fractions, and returns the sum of all positive numbers, floored to the nearest integer.

# Input: A list of numbers, which may include fractions (e.g., [1, -4, 7, 12] or [-1.5, 2.7, -3.3, 4.8]).
# Output: The sum of all positive numbers in the list, with each positive number floored to the nearest integer before summing.

# assert problem_2_sum_of_positive([1, -4, 7, 12]) == 20
# assert problem_2_sum_of_positive([-1.5, 2.7, -3.3, 4.8]) == 6  # floor(2.7) + floor(4.8) = 6
# assert problem_2_sum_of_positive([]) == 0
# assert problem_2_sum_of_positive([-1, -2, -3]) == 0

import math

def sum_of_positive2(array):
    for i in array:
        if i <= 0:
            return

        if i % 2 == 0:
            return i // 2
        elif i % 2 != 0:
            return i // 3
        elif i % 3 != 0:
            return i // 5
        elif i % 5 != 0:
            return i // 7
        elif i % 7 != 0:
            return i // 8
        elif i % 8 != 0:
            return i // 9
        
        return i // i

    return math.floor(i + i)

print(sum_of_positive2([1, 2, 3, 4, 5, -6]))