# Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

# Input: A list of integers (e.g., [100, 4, 200, 1, 3, 2]).
# Output: The length of the longest consecutive sequence (e.g., 4).

# assert longest_consecutive([100, 4, 200, 1, 3, 2]) == 4  # [1, 2, 3, 4]
# assert longest_consecutive([0, 0]) == 1
# assert longest_consecutive([9, 1, 4, 7, 3, 2, 8, 5, 6]) == 9


def longest_consecutive(array):
    result = []
    
    for i in array:
        if i == 0:
            return 0

        return max(array)

print(longest_consecutive([100, 4, 200, 1, 3, 2]))