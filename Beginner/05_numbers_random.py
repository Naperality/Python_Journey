# python has three numbers int, float, and complex

num1 = 1

# type casting numbers 

print(int(num1))
print(float(num1))
print(complex(num1))

# python has a common library called random to get random

import random

print(random.randrange(1,5)) # gets random number from 1 - 5 works the same with range
print(random.randrange(1,10,2)) # gets random number between 1-10 with step of 2 3,5,7,9..

print(random.random()) # gets number float from 0 - 1

print(random.randint(1,5)) # gets integer inclusive

# can be used directly with list or tuples, or even strings characters
li1 = ['apple','banana',3,6]

print(random.choice(li1))

# can also shuffle
random.shuffle(li1)
print(li1)