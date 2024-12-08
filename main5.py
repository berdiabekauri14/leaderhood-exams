# Write a function to check if two strings are anagrams (contain the same characters in the same frequency).

# Input: Two strings (e.g., "listen" and "silent").
# Output: A boolean (True or False) indicating if the strings are anagrams.

# assert are_anagrams("listen", "silent") == True
# assert are_anagrams("hello", "world") == False
# assert are_anagrams("triangle", "integral") == True

def are_anagrams(str1, str2):
    if str1 == "" or str2 == "":
        return False
    
    if str1[0] != str2[0]:
        return True
    elif str1[0] != str2 and max(str1) != max(str2):
        return False

    return True

print(are_anagrams("listen", "silent"))