# List are array in python denoted in [] brackets
list1 = []

# it allows duplicates and it is mutable or changeable
list1 = ['apple','banana','mango','apple','mango','cherry']

print(list1, len(list1))

# can create a new list using list()
listStr = list('Hello')
print(listStr) # outputs each character on the string into list

# accessing list items
print(list1[0]) # first item
print(list1[1:]) # just like string slicing this outputs starts with banana
print(list1[::-1]) # can also do reverse just like string

# changing list items
list1[0] = 'Nap'
print(list1)

# changing a range through slicing just like string
list1[1:3] = ['black','white']
print(list1)

# list.insert() method
list1.insert(4,'berry')
print(list1)

# list.append() and .extend()
list1.append('Bomb') # adds new element to the last
list1.extend(('hello','world')) # adds element last but either tuple or any iterable

print(list1)

# Removing items in list
list1.remove('hello')
list1.pop(-1)

print(list1)

# loop through list jus tlike strings
for word in list1:
    print(word, end=' ')

for i in range(len(list1)):
    print(list1[i], end=' ')

# or use list comprehension
[print(word, end='-') for word in list1]

# making new list with list comprehension
newList1 = [word.lower() for word in list1 if 'a' in word] # gets only the word with letters 'a'

print(newList1)
newList1.sort() # sorts the list into ascending order, for ascii codes of letter 'a'=97 while 'A'=65
# note: if want sort to descending then use .sort(reverse = True)
for word in newList1:
    print(word)

# we can also use sort depends on what key for this example the closest
def closerFunc(n):
    return abs(n - 50)
listNum = [-11,24,1,2,3,4,78,90,56,23,45,100, 0.87, -12.43]
listNum.sort(key = closerFunc)
[print(Num, end = ' ') for Num in listNum]


# list using reverse regardless of key or ascii codes
newList1.reverse()
print(newList1)


