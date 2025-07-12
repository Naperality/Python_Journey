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

# however, str are not mutable or immutable for 
# individual character change but a str can be change value with another str
# sampleStr[0] = 't' shows error assignment
sampleStr = 'Philippines is Good'

# String len() shows the length of the string including whitespaces
print(len(sampleStr+" "))

# str.find() finds the specific character or string in the string
print(sampleStr.find('n')) #outputs -1 since no 'n' but 'N' is 0

#str.lower() lowercase the str and str.islower() return true if it is all lowercase
print(sampleStr.lower().islower())
#likewise to upper() and isupper()
print(sampleStr.upper().isupper())

#Code exercise Caesar Code using .find() and lower() or upper() and for loop
# alphabet = 'abcdefghijklmnopqrstuvwxyz'
# shift = 3
def caesar(str, offset, direction = 1):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_str = ''
    for letter in str.lower():
        #for whitespace to skip use continue or acccept white space
        if letter == ' ':
            encrypted_str += letter
            continue
        index = alphabet.find(letter)
        # print(letter,index)
        new_index = (index + offset * direction) % len(alphabet)
        encrypted_str += alphabet[new_index]
        # print(f"letter: {letter}, new letter: {encrypted_str}")
    # print(f'Original Text: {str}')
    # print(f'Encrypted Text: {encrypted_str}')
    return encrypted_str
encrypted = caesar(sampleStr, 3, -1)
decrypted = caesar(encrypted, 3)
print(encrypted)
print(decrypted)
# caesar(sampleStr,13)

# Vigenere cipher code
def vigenere(str,key, direction = 1):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''
    for letter in str.lower():
        # add space to the message
        if letter == ' ':
            encrypted_text += letter
            continue
        # Find the right key character to encode
        key_char = key[key_index % len(key)]
        key_index += 1
        # define the offset  and letter
        offset = alphabet.index(key_char)
        index = alphabet.find(letter)
        new_index = (index + offset * direction) % len(alphabet)
        encrypted_text += alphabet[new_index]
    return encrypted_text

def encryptVigenere(str,key):
    return vigenere(str,key)
def decryptVigenere(str,key):
    return vigenere(str,key,-1)
text = 'Nappy Dev Coding Day One'
custom_key = 'mypythonjourney'
encryption = encryptVigenere(text,custom_key)
print(encryption)
decryption = decryptVigenere(encryption,custom_key)
print(decryption)