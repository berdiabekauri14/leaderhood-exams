#  Given two strings word1 and word2, find the minimum number of operations required to convert word1 into word2. You have three operations allowed: insertion, deletion, or substitution.

# Input: Two strings word1 and word2 (e.g., "horse", "ros").
# Output: The minimum number of operations required to convert word1 into word2.

# assert min_distance("horse", "ros") == 3
# assert min_distance("intention", "execution") == 5
# assert min_distance("kitten", "sitting") == 3

def min_distance(word1, word2):
    result = ""

    if word1 == "" or word2 == "":
        return 0
    elif word1 == word2:
        return 0

    for i in word1:
        result = word1.replace(i, "").sorted()

    return len(result)

print(min_distance("horse", "ros"))