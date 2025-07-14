# Two Loops the While and for loops
i = 0
# while i < 5:
#     print(i) # loops to print i until 0-4
#     i += 1

while i < 6:
    i+=1
    if i == 3:
        continue # breaks the loop until 1-2 if used continue it skips 3
    print(i)
else:
    print('i is no longer printable')
    
# for loops are used to iterate over a list tuple or string dictionary

fruits = ["apple", "banana", "cherry"] # list
for x in fruits:
  print(x)

for x in "banana": # iterate over a string
  print(x)
    
fruits2 = tuple(fruits) # tuple
print(type(fruits2))
for x in fruits2:
    print(x)
