# Task
# Given an integer, , perform the following conditional actions:

# If  is odd, print Weird
# If  is even and in the inclusive range of  to , print Not Weird
# If  is even and in the inclusive range of  to , print Weird
# If  is even and greater than , print Not Weird
# Input Format

# A single line containing a positive integer, .
# Constraints
# Output Format
# Print Weird if the number is weird. Otherwise, print Not Weird.

# my solution
if __name__ == '__main__':
    n = int(input().strip())
    
    even = True if n%2 == 0 else False
    
    if even and (2 <= n <= 5 or n > 20):
        print('Not Weird')
    elif even and 6 <= n <= 20:
        print('Weird')
    else:
        print('Weird')


