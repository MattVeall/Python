# Strings in python are surrounded by either single quotation marks, or double quotation marks.

# 'hello' is the same as "hello".

# You can display a string literal with the print() function:
print("Hello")
print('Hello')

# Assigning a string to a variable: 
a = "Hello"
print(a)

# You can assign a multiline string to a variable by using three quotes:
A ="""This is an example of assigning
 a multiline string to a 
 variable by using three quotes"""
print(A)

# or three single quotes
b ='''This is an example of assigning
 a multiline string to a 
 variable by using three single quotes'''
print(b)

# Strings in Python are arrays of bytes representing unicode characters.

# However, Python does not have a character data type, a single character is simply a string with a length of 1.

# Square brackets can be used to access elements of the string.

# Get the character at position 1 (remember that the first character has the position 0):
a = "Hello world!"
print(a[1])

# Since strings are arrays, we can loop through the characters in a string, with a for loop:
for x in "banana":
    print(x)

# To get the length of a string, use len() function:
a = "Hello, World!"
print(len(a))

# To check if a certain phrase or character in a string, we can use the keyword in:
txt = "The best things in life is free"
print("free" in txt)

# Use if statement:
txts = "The best things in life is free"
if "free" in txt:
    print("Yes, 'free' is present")

# To check if a certain phrase or character is Not present in a sting, we can use the keyword not in:
txtt = "The best things in life is free!"
print("expensive" not in txtt)

# You can return a range of characters by using the slice syntax.

# Specify the start index and the end index, separated by a colon, to return a part of the string:
b = "Hello World!"
print(b[2:5])

# By leaving out the start index, the range will start at the first character:
B = "Hello World!"
print(b[:5])

# By leaving out the end index, the range will go to the end:
c = "Hello World!"
print(c[2:])

# Use negative indexes to start the slice from the end of the string:
C = "Hello World!"
print(C[-5:-2])

# Python has a set of built-in methods that you can use on strings

# The upper() method returns the string in upper case:
d = "Hello, World!"
print(a.upper())

# The lower() method returns the string in lower case:
D = "Hello, World!"
print(D.lower())

# The strip() method removes any whitespace from the beginning or the end:
e = " Hello, World! "
print(e.strip()) # returns "Hello, World!"

# The replace() method replaces a string with another string:
E = "Hello, World!"
print(E.replace("H","J"))

# The split() method splits the string into substrings if it finds instances of the separator:
f = "Hello, World!"
print(f.split(",")) # returns ['Hello', ' World!']

# To concatenate, or combine, two strings you can use the + operator
# Merge variable a with variable b into variable c:
a = "Hello"
b = "World!"
c = a + b
print(c)

# To add a space between them, add a "":
a = "Hello"
b = "World!"
c = a + " " + b
print(C)

# The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} are

# Use the format() method to insert numbers into strings:
age = 36
txtts = "My name is Steve, and i am {}"
print(txtts.format(age))

# The format() method takes unlimited number of arguments, and are placed into the respective placeholders:
quantity = 3
item_no = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, item_no, price))

# You can use index numbers {0} to be sure the arguments are placed in the correct placeholders:
quantity = 3
item_no = 567
price = 49.49
myorder = "I want {2} dollar for {0} pieces of item {1}"
print(myorder.format(quantity, item_no, price))

# To insert characters that are illegal in a string, use an escape character.

# An escape character is a backslash \ followed by the character you want to insert.

# An example of an illegal character is a double quote inside a string that is surrounded by double quotes

# To fix this problem, use the escape character \"

# The escape character allows you to use double quotes when you normally would not be allowed:
txt = "We are the so-called \"Vikings\" from the north. "
print(txt)

#Other escape characters used in Python:

# Code	Result	
# \'	Single Quote	
# \\	Backslash	
# \n	New Line	
# \r	Carriage Return	
# \t	Tab	
# \b	Backspace	
# \f	Form Feed	
# \ooo	Octal value	
# \xhh	Hex value

# Python has a set of built-in methods that you can use on strings.

# Note: All string methods returns new values. They do not change the original string

# Method	Description
# capitalize()	Converts the first character to upper case
# casefold()	Converts string into lower case
# center()	Returns a centered string
# count()	Returns the number of times a specified value occurs in a string
# encode()	Returns an encoded version of the string
# endswith()	Returns true if the string ends with the specified value
# expandtabs()	Sets the tab size of the string
# find()	Searches the string for a specified value and returns the position of where it was found
# format()	Formats specified values in a string
# format_map()	Formats specified values in a string
# index()	Searches the string for a specified value and returns the position of where it was found
# isalnum()	Returns True if all characters in the string are alphanumeric
# isalpha()	Returns True if all characters in the string are in the alphabet
# isdecimal()	Returns True if all characters in the string are decimals
# isdigit()	Returns True if all characters in the string are digits
# isidentifier()	Returns True if the string is an identifier
# islower()	Returns True if all characters in the string are lower case
# isnumeric()	Returns True if all characters in the string are numeric
# isprintable()	Returns True if all characters in the string are printable
# isspace()	Returns True if all characters in the string are whitespaces
# istitle()	Returns True if the string follows the rules of a title
# isupper()	Returns True if all characters in the string are upper case
# join()	Joins the elements of an iterable to the end of the string
# ljust()	Returns a left justified version of the string
# lower()	Converts a string into lower case
# lstrip()	Returns a left trim version of the string
# maketrans()	Returns a translation table to be used in translations
# partition()	Returns a tuple where the string is parted into three parts
# replace()	Returns a string where a specified value is replaced with a specified value
# rfind()	Searches the string for a specified value and returns the last position of where it was found
# rindex()	Searches the string for a specified value and returns the last position of where it was found
# rjust()	Returns a right justified version of the string
# rpartition()	Returns a tuple where the string is parted into three parts
# rsplit()	Splits the string at the specified separator, and returns a list
# rstrip()	Returns a right trim version of the string
# split()	Splits the string at the specified separator, and returns a list
# splitlines()	Splits the string at line breaks and returns a list
# startswith()	Returns true if the string starts with the specified value
# strip()	Returns a trimmed version of the string
# swapcase()	Swaps cases, lower case becomes upper case and vice versa
# title()	Converts the first character of each word to upper case
# translate()	Returns a translated string
# upper()	Converts a string into upper case
# zfill()	Fills the string with a specified number of 0 values at the beginning
