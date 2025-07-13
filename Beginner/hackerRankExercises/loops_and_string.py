# Task
# The provided code stub reads an integer, , from STDIN. For all non-negative integers , print .
# Example
# The list of non-negative integers that are less than  is . Print the square of each number on a separate line.

if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        print(i**2)
        
# The included code stub will read an integer, , from STDIN.
# Without using any string methods, try to print the following:
# Note that "" represents the consecutive values in between.
if __name__ == '__main__':
    n = int(input())
    for num in range(1,n+1):
        print(num,end="")
        
# We have seen that lists are mutable (they can be changed), 
# and tuples are immutable (they cannot be changed).
# Let's try to understand this with an example.
def mutate_string(string, position, character):
    l = list(string)
    l[position] = character
    message = ''.join(l)  
    return message

# In this challenge, the user enters a string and a substring. 
# You have to print the number of times that the substring occurs in the given string. 
# String traversal will take place from left to right, not from right to left.
# Note: String letters are case-sensitive.
# Input Format
# The first line of input contains the original string. The next line contains the substring.
# Constraints
# Each character in the string is an ascii character.
# Output Format
# Output the integer number indicating the total number of occurrences of the substring in the original string.

def count_substring(string, sub_string):
    start = 0
    count = 0
    
    while True:
        index = string.find(sub_string,start)
        if index == -1:
            break
        count += 1
        start = index + 1
    return count

# In the first line, print True if  has any alphanumeric characters. Otherwise, print False.
# In the second line, print True if  has any alphabetical characters. Otherwise, print False.
# In the third line, print True if  has any digits. Otherwise, print False.
# In the fourth line, print True if  has any lowercase characters. Otherwise, print False.
# In the fifth line, print True if  has any uppercase characters. Otherwise, print False.

if __name__ == '__main__':
    s = input()
    alpha = alnum = digit = upper = lower = False
    for letter in s:
        if letter.isalpha():
            alpha = True
        if letter.isalnum():
            alnum = True
        if letter.isdigit():
            digit = True
        if letter.isupper():
            upper = True
        if letter.islower():
            lower = True
    print(f'{alnum}\n{alpha}\n{digit}\n{lower}\n{upper}')