# Create a function that finds the length of the longest substring without repeating characters

# Input: A string (e.g., "abcabcbb").
# Output: An integer representing the length of the longest substring (e.g., 3 for "abc").

# assert longest_unique_substring("abcabcbb") == 3
# assert longest_unique_substring("bbbbb") == 1
# assert longest_unique_substring("") == 0
# assert longest_unique_substring("pwwkew") == 3

def longest_unique_substring(string):
    if string == "":
        return 0

    return len(string)

print(longest_unique_substring("abc"))