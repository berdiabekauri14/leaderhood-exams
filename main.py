# Create a function that takes a list of numbers and returns the sum of all positive numbers.
# Input: A list of integers (e.g., [1, -4, 7, 12]).
# Output: The sum of all positive integers in the list.

# assert problem_1_sum_of_positive([1, -4, 7, 12]) == 20
# assert problem_1_sum_of_positive([-1, -2, -3, -4]) == 0
# assert problem_1_sum_of_positive([]) == 0

def sum_of_positive(array):
    for i in array:
        if i <= 0:
            return
        
        return i + i
    
print(sum_of_positive([-1, 2, 3, 4]))