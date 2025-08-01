# Create a new array for counting how many there are of the different values.
# Go through the array that needs to be sorted.
# For each value, count it by increasing the counting array at the corresponding index.
# After counting the values, go through the counting array to create the sorted array.
# For each count in the counting array, create the correct number of elements, with values that correspond to the counting array index.
def count_sort(arr):
    if not arr:
        return arr
    
    max_value = max(arr)
    count = [0] * (max_value + 1)
    
    # Count occurrences of each value
    for num in arr:
        count[num] += 1
    
    # Build the sorted array
    sorted_arr = []
    for i, cnt in enumerate(count):
        sorted_arr.extend([i] * cnt)
    
    return sorted_arr
# Example usage:
sample_array = [3, 6, 8, 10, 1, 2, 1]
sorted_array = count_sort(sample_array)
print("Sorted array:", sorted_array)
# Example usage:
# sample_array = [3, 6, 8, 10, 1, 2, 1]     
# sorted_array = count_sort(sample_array)
# print("Sorted array:", sorted_array)