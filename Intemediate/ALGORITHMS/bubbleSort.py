# Go through the array, one value at a time.
# For each value, compare the value with the next value.
# If the value is higher than the next one, swap the values so that the highest value comes last.
# Go through the array as many times as there are values in the array.

mylist = [64, 34, 25, 12, 22, 11, 90, 5]

for i in range(len(mylist) - 1):
    for j in range(len(mylist) - 1 - i):
        if mylist[j] >  mylist[j+1]:
            mylist[j], mylist[j+1] = mylist[j+1], mylist[j]

print("Sorted array is:", mylist)   

# with swapped to check if swap were made

for i in range(len(mylist) - 1):
    swapped = False
    for j in range(len(mylist) - 1 - i):
        if mylist[j] > mylist[j + 1]:
            mylist[j], mylist[j + 1] = mylist[j + 1], mylist[j]
            swapped = True
    if not swapped:
        break