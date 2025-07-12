# 01_variables_and_types.py

# 🟢 Variable Declarations
name = "Napoleon"
age = 21
grade = 92.5
is_graduate = False

# can store multiple values in one line
x, y, z = "Orange", "Banana", "Apple"
x = y = z = "Orange, Banana, Apple"

# 🟢 Print with Types
print("Name:", name, "| Type:", type(name))
print("Age:", age, "| Type:", type(age))
print("Grade:", grade, "| Type:", type(grade))
print("Graduate?:", is_graduate, "| Type:", type(is_graduate))

# 🟢 Input and Output
user_name = input("What is your name? ")
user_age = int(input("How old are you? "))

# can type cast a value
int() # to integer
str() # to string
float() # to float 

# putting values to string or use concatenate
print(f"Hello, {user_name}! You are {user_age} years old.")
print("Hello, "+ user_name + "! You are " + str(user_age) + " years old.")

#use comma to output different data types
print("Hello,", user_name+"! You are", user_age,"years old.") 
# no need for spaces since it gives spaces after and before

# 🧪 Mini Practice
# Convert a string to int and multiply
number_str = input("Enter a number to multiply by 2: ")
number = int(number_str)
print("Result:", number * 2)


# Strings

# strings are characters starts index 0 or last character is at -1 and so on
sampleStr = "Nigeria"
print(sampleStr[4]) # outputs 'r'
print(sampleStr[-3]) # outputs 'r'

# String len() shows the length of the string including whitespaces
print(len(sampleStr+" "))