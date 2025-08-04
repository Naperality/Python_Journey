# Start with the least significant digit (rightmost digit).
# Sort the values based on the digit in focus by first putting the values in the 
# correct bucket based on the digit in focus, and then put them back into array in the correct order.
# Move to the next digit, and sort again, like in the step above, until there are no digits left.

def counting_sort_for_radix(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10  # Since we are dealing with base 10 numbers

    # Count occurrences of each digit
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1

    # Change count[i] so that it contains the actual position of this digit in output[]
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array
    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1

    # Copy the output array to arr[], so that arr[] now contains sorted numbers according to the current digit
    for i in range(n):
        arr[i] = output[i]
def radix_sort(arr):
    if not arr:
        return arr
    
    # Find the maximum number to know the number of digits
    max_num = max(arr)

    # Do counting sort for every digit
    exp = 1
    while max_num // exp > 0:
        counting_sort_for_radix(arr, exp)
        exp *= 10

    return arr
# Example usage:
sample_array = [170, 45, 75, 90, 802, 24, 2, 66]
sorted_array = radix_sort(sample_array) 
print("Sorted array:", sorted_array)