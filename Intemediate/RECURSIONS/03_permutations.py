# permutations sequence using recursion
def permutations(s):
    if len(s) == 0:
        return ['']
    result = []
    for i, char in enumerate(s):
        for perm in permutations(s[:i] + s[i+1:]):
            result.append(char + perm)
    return result

# Example usage
s = "abc"  # Change this value to compute permutations of a different string
print(f"The permutations of '{s}' are: {permutations(s)}")