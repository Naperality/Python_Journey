# Go through the array value by value from the start.
# Compare each value to check if it is equal to the value we are looking for.
# If the value is found, return the index of that value.
# If the end of the array is reached and the value is not found, return -1 to indicate that the value was not found.

# Example is using it in a array or list using 'in'

myList = list(range(50,0,-2))

if 4 in myList:
    print('There is 4')
else:
    print('There is no 4')

# or if index is needed then 
def indexSearch(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            print('There is', target, i)
            
# use enumerate to get the index and value
for index, value in enumerate(myList):
    if 6 == value:
        print(index,value)
         
indexSearch(myList,18)
print(myList)