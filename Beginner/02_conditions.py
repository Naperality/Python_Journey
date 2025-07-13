# These are teh common conditions used
# Equals: a == b
# Not Equals: a != b
# Less than: a < b
# Less than or equal to: a <= b
# Greater than: a > b
# Greater than or equal to: a >= b
a = 90
b = 90
c = 85
if b > a: 
  print("b is greater than a") # outputs the print since its true
elif a == b:
  print("a and b are equal") 
else:
  print("a is greater than b")
  
# short hand rule for if-else or ternary 
print('A') if a < b else print('B')

# triple value ternary
print('A') if a < b else print('Equal') if a == b else print('B')

# And is logical operator if both 1/true
if a > b and c < a:
  print('Both are true')

# Or if either is 1/true
if a > b or c < a:
  print('Either one is true')

# Not is inverse of the value
if not a > b:
  print('a is Not greater than b')


# match is like switch
day = 3
match day:
  case 1:
    print("Monday")
  case 2:
    print("Tuesday")
  case 3:
    print("Wednesday")
    print("Thursday")
  case _:
    print('default')
    
month = 5
day = 4
match day:
  case 1 | 2 | 3 | 4 | 5 if month == 4:
    print("A weekday in April")
  case 1 | 2 | 3 | 4 | 5 if month == 5:
    print("A weekday in May")
  case _:
    print("No match")
    

def print_formatted(number):
    width = len(bin(number)[2:])
    
    for i in range(1,number+1):
        decimal = str(i).rjust(width)
        octal = oct(i)[2:].rjust(width)
        hexa = hex(i)[2:].upper().rjust(width)
        binary = bin(i)[2:].rjust(width)
        
        print(f'{decimal} {octal} {hexa} {binary}')
print_formatted(17)