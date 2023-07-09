def expandAroundCenter(s, left, right):
    
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return s[left + 1:right]

def longestPalindrome(s):
    if len(s) < 2:
        return s

 