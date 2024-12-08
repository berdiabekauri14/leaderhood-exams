# Create a function that accepts two integers, start and end, and returns a list of all non-prime numbers within the range [start, end] (inclusive). A non-prime number is defined as any integer greater than 1 that is not a prime number.

# Input: start = 10, end = 20
#  Output: [10, 12, 14, 15, 16, 18, 20]
# Input: start = 1, end = 10
#  Output: [1, 4, 6, 8, 9, 10]
# Input: start = 20, end = 30
#  Output: [20, 21, 22, 24, 25, 26, 27, 28, 30]
# Input: start = 24, end = 25
#  Output: [24, 25]
# Input: start = 1, end = 1
#  Output: [1]

def non_prime_numbers(start, end):
    result = []

    for i in range(start, end):
        if i % 2 == 0:
            result.append(i)

    return result

print(non_prime_numbers(10, 20))