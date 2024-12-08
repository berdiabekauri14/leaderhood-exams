# Create a function to find the missing number in a list of integers from 1 to n.

# Input: A list of integers from 1 to n with one number missing (e.g., [1, 2, 4, 5]).
# Output: The missing number (e.g., 3 in this case).

# assert find_missing_number([1, 2, 4, 5]) == 3
# assert find_missing_number([3, 5, 6, 1, 2]) == 4
# assert find_missing_number([2]) == 1

def find_missing_number(n, array):
    for i in array:
        if i != n:
            return n
        
print(find_missing_number(3, [1, 2, 4, 5]))