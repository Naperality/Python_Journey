# Go through the array to find the lowest value.
# Move the lowest value to the front of the unsorted part of the array.
# Go through the array again as many times as there are values in the array.

mylist = [64, 34, 25, 5, 22, 11, 90, 12]

for i in range(len(mylist)):
    # Assume the first element is the minimum
    min_index = i
    for j in range(i + 1, len(mylist)):
        if mylist[j] < mylist[min_index]:
            min_index = j
    # Swap the found minimum element with the first element
    mylist[i], mylist[min_index] = mylist[min_index], mylist[i]

print("Sorted array:", mylist)