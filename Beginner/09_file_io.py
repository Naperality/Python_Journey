# python had file handlement
# using open() to open a file, mode of it

# lis tof modes in open():
# "r" - Read - Default value. Opens a file for reading, error if the file does not exist

# "a" - Append - Opens a file for appending, creates the file if it does not exist

# "w" - Write - Opens a file for writing, creates the file if it does not exist

# "x" - Create - Creates the specified file, returns an error if the file exists

# 't' - text while 'b' - images (binary)
sourcePath = 'C:/Users/Hp/Desktop/Python_Journey/Beginner/demoFiles/01_file.txt'
f = open(sourcePath)
# to read the file use read()
print(f.read())
f.close() # to close always the file

# use with statement to open and auto close file
with open(sourcePath) as f:
    print(f.read(2))
    print(f.readline())# continues the read of the first line

with open(sourcePath) as f:
    for line in f:
        print(line)

# appending and writing new files
with open(sourcePath, 'a') as f:
    f.write('\nNew line added!')

with open(sourcePath) as f:
    print(f.read())

# overwritting the fieles uses the w
with open(sourcePath, 'w') as f:
    f.write('Opps! deleted the content hehe')

with open(sourcePath) as f:
    print(f.read())

# now creating more files using x
open('C:/Users/Hp/Desktop/Python_Journey/Beginner/demoFiles/newFile.txt','x')
