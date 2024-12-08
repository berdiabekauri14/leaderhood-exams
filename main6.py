# Write a function to find the common elements between two lists.

# Input: Two lists of integers (e.g., [1, 2, 3] and [2, 3, 4]).
# Output: A list of integers representing the intersection (e.g., [2, 3]).

# assert find_intersection([1, 2, 3], [2, 3, 4]) == [2, 3]
# assert find_intersection([1, 1, 2], [1, 3]) == [1]
# assert find_intersection([], [1, 2]) == []

def find_intersection(array1, array2):
    result = []
    for i, _ in array1, array2:
        if i == _:
            result.append(i, _)
    
    return result

print(find_intersection([1, 2, 3], [2, 3, 4]))