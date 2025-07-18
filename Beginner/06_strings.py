# strings can be in "" or '' 
string = 'Napoleon'

# multi line strings are written with ''' '''
multiStr = '''  This is a multiline string'''
print(multiStr, string)

# string slicing used str[:]

print(string[2:]) # note: slicing starts at 0 index but leaving out would automatically start at 0 or at end

# Negative indexing

print(string[-6:-1]) # note: the end would always be excluded in slicing so output poleo

# special function of slicing is reversing

print(string[::-1]) # uses the same function of range(start,stop,step) where string[start:stop:step]

# Modify strings
# strings has methods like string.upper() , .lower(), 
# .strip(), .replace(), .split() and .translate(str.maketrans({}))

print(string.upper())
print(string.lower())
print(multiStr.strip())
newMulti = multiStr.strip()
print(string.replace('N','n'))
print(newMulti.split(' '))
print(string.translate(str.maketrans({'n':' changed '})))

# Concatonate strings using '+' sign and .join()
print(string + multiStr)
li = ['nap','visitacion']
print(''.join(li)) # inside the '' would be the divider like is '.' it would output nap.visitacion

print('-'.join(newMulti.split(' ')))

# Format strings or F-strings uses f'' where you can type any variable/formula inside using {}
print(f'An Example of F-string 20x3 = {20*3}')

# other useful methods of string are
print(string.find('n')) # returns the index where it was found
print(string.capitalize()) # capitalize the first letter only
print(string.ljust(20,'O')) # left justified with value on number of spaces
print(string.rjust(20)) # right justified "
