# Given an integer x, return true if x is a palindrome, and false otherwise. 
# Twist is it also applies to numbers

# using str cause its faster
def isPalindrome(x):
    return True if str(x) == str(x)[::-1]else False

# other solution without convertion of string
def isPalindromeNum(x):
    if x < 0:
        return False
    orig = x
    reversed = 0
    while x > 0:
        reversed = reversed * 10 + x % 10
        x = x//10
    return orig == reversed

print(isPalindrome(121))
print(isPalindromeNum(121))

