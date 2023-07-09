def expandAroundCenter(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return s[left+1:right]

def longestPalindrome(s):
    if len(s) < 2:
        return s

    longest = ""
    for i in range(len(s)):
        # Expand around a single character
        substr1 = expandAroundCenter(s, i, i)
        if len(substr1) > len(longest):
            longest = substr1

        # Expand around two characters
        substr2 = expandAroundCenter(s, i, i + 1)
        if len(substr2) > len(longest):
            longest = substr2

    return longest

# Input
input_str = "babad"

# Encontrar a maior substring palindrômica
output_str = longestPalindrome(input_str)
print(output_str)
