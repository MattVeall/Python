# The key function for working with files in Python is the open() function.

# The open() function takes two parameters; filename, and mode.

# There are four different methods (modes) for opening a file:

# "r" - Read - Default value. Opens a file for reading, error if the file does not exist

# "a" - Append - Opens a file for appending, creates the file if it does not exist

# "w" - Write - Opens a file for writing, creates the file if it does not exist

# "x" - Create - Creates the specified file, returns an error if the file exists

# In addition you can specify if the file should be handled as binary or text mode

# "t" - Text - Default value. Text mode

# "b" - Binary - Binary mode (e.g. images)

# To open a file for reading it is enough to specify the name of the file:
f = open("Examplefile.txt")

# The code above is the same as:
f = open("Example.txt", "rt")

# To open the file, use the built-in open() function.

# The open() function returns a file object, which has a read() method for reading the content of the file:
f = open("Example.txt", "r")
print(f.read())

# If the file is located in a different location, you will have to specify the path:
f = open("D:\\myfiles\Example.txt", "r")
print(f.read())

# By default the read() method returns the whole text, but you can also specify how many characters you want to return. 
# Return the 5 first characters of the file:
f = open("Example.txt", "r")
print(f.read(5))

# Return one line by using the readline() method:
f = open("Example.txt" "r")
print(f.readline())

# Read two lines of the file:
f = open("Example.txt", "r")
print(f.readline())
print(f.readline())

# Loop through the file line by line:
f = open("Example.txt", "r")
for x in f:
    print(x)

# Close the file when you are finish with it:
f = open("Example.txt", "r")
print(f.readline())
f.close()

# To write to an existing file, you must add a parameter to the open() function:

# "a" - Append - will append to the end of the file

# "w" - Write - will overwrite any existing content

# Open the file "Example.txt" and append content to the file:
f = open("Example.txt", "a")
f.write("Now this file has more content!")
f.close()

# Open and read the file after appending:
f = open("Example.txt" "r")
print(f.read())

# Open the file 'Example.txt' and overwrite the content:
f = open("Example.txt", "w")
f.write("Woops! i have deleted the content!")
f.close()

# To create a new file in Python, use the open() method, with one of the following parameters:

# "x" - Create - will create a file, returns an error if the file exist

# "a" - Append - will create a file if the specified file does not exist

# "w" - Write - will create a file if the specified file does not exist

# Create a file called "myfile.txt":
f = open("myfile.txt", "x")  

# Create a new file if it does not exist:
f = open("myfile.txt", "w")

# To delete a file, you must import the OS module, and run its os.remove() function:
import os
os.remove("Example.txt")

# To avoid getting an error, you might want to check if the file exists before you try to delete it:
import os
if os.path.exists("myfile.txt"):
    os.remove("myfile.txt")
else:
    print("The file does not exist")

# to Delete and entire folder, use the os.rmdir() method:
import os
os.rmdir("Examplefolder")
