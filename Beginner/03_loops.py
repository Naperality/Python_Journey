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

# range function lets loop over a number
for x in range(6):
    print(x)
    
# range has range(start,stop,step) or range(start,stop)
for x in range(1,30,5):
    print(x)
else: 
    print('Finished')

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)