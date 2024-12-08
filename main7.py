# Find all unique triplets in an array that sum up to zero.

# Input: A list of integers (e.g., [-1, 0, 1, 2, -1, -4]).
# Output: A list of unique triplets that sum to zero.

# assert three_sum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]
# assert three_sum([0, 0, 0]) == [[0, 0, 0]]
# assert three_sum([1, 2, -2, -1]) == []

def three_sum(array):
    result = []

    for i in array:
        if i == 0:
            return array
        
        if i >= 0:
            array.pop(i)
            result.append(array)

    return result

print(three_sum([-1, 0, 1, 2, -1, -4]))