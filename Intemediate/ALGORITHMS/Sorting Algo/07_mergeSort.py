# Divide the unsorted array into two sub-arrays, half the size of the original.
# Continue to divide the sub-arrays as long as the current piece of the array has more than one element.
# Merge two sub-arrays together by always putting the lowest value first.
# Keep merging until there are no sub-arrays left.

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # Find the middle of the array
        L = arr[:mid]        # Divide the array into two halves
        R = arr[mid:]

        merge_sort(L)  # Sort the first half
        merge_sort(R)  # Sort the second half

        i = j = k = 0

        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

    return arr
# Example usage:
sample_array = [38, 27, 43, 3, 9, 82, 10]
sorted_array = merge_sort(sample_array)
print("Sorted array:", sorted_array)