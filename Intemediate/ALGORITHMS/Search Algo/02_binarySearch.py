# Check the value in the center of the array.
# If the target value is lower, search the left half of the array. 
# If the target value is higher, search the right half.

# Continue step 1 and 2 for the new reduced part of the array 
# until the target value is found or until the search area is empty.
# If the value is found, return the target value index. If the target value is not found, return -1.

def binarySearch(arr, target):
    leftIndex = 0
    rightIndex = len(arr) - 1
    
    while leftIndex <= rightIndex:
        mid = (leftIndex+rightIndex) // 2
        if arr[mid] == target:
            return arr[mid]
        
        elif target < arr[mid]:
            rightIndex = mid - 1
        else:
            leftIndex = mid + 1
    return -1

myList = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
print('The number is found: ',binarySearch(myList, 20))