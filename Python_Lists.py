# Lists are used to store multiple items in a single variable.

# Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

 # Lists are created using square brackets:

# Make a list:
mylist = ["apple", "banna", "cherry", "apple", ]

# Print the list:
print(mylist)

# Print list length
print(len(mylist))

# List items -  Data Types, list items can be of any data types, string, int, boolean:
list1 = ["apples", "banana", "cherry"]
list2 = [1,5,7,9,3]
list3 = [True, False, False]

print(list1,list2,list3)

# A list can contain different data types, a list with strings, integers and boolean values:
list4 = ["abc", 34, True, 40, "male"]

# list are defined as objects with the data type 'list' <class 'list'>
list5 = ["apple", "banana", "cherry"]
print(type(list5))

# Using the list() constructor to make a list:
thislist = list(("apple", "banana", "cherry")) # note the double around the brackets:
print(thislist) 

# List are indexed, print the second item of the list:
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

# List can be negative indexed, -1 last item, -2 second last item
thislist2 = ["apple", "banana", "cherry"]
print(thislist2[-1])

# Specify a range of indexes by specifying where to start and where to end the range:
thislist3 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist3[2:5])

# Specify items from begining to, but NOT including , "kiwi"
thislist4 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist4[:4])

# Returns the items from "cherry" to the end:
thislist5 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist5[2:])

# Returns the items from "orange" (-4) to, but NOT including "mango" (-1):
thislist6 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist6[-4:-1])

# Check if item exists:
thislist7 = ["apple", "banana", "cherry"]
if "apple" in thislist7:
    print("Yes, 'apple' is in the list")

# Change the value of a specific item, change the second item:
thislist8 = ["apple", "banana", "cherry"]
thislist8 [1] = "blackcurrent"
print(thislist8)

# Change a range of item values:
thislist9 = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist9[1:3] = ["blackcurrent", "watermelon"]
print(thislist9)

# Change the second value by replacing it with two new values:
list6 = ["apple", "banana", "cherry"]
list6 [1:2] = ["blackcurrant", "watermealon"]
print(list6)

# Change the second and thrid value by replacing it with one value:
list7 = ["apple", "banana", "cherry"] 
list7 [1:3] = ["watermelon"]
print(list7)

# Insert "watermelon" as thrid item:
list8 = ["apples", "banana", "cherry"]
list8.insert(2, "watermelon")
print(list8)
