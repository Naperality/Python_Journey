def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1) # Recursive case where the function calls itself with a decremented value of n

# Example usage:
num = 5
print(f"The factorial of {num} is {factorial(num)}")
# This code defines a recursive function to calculate the factorial of a number.
