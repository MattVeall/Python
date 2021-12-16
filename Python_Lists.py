# Lists are used to store multiple items in a single variable.

# Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

 # Lists are created using square brackets:

# Make a list:
mylist = ["apple", "banna", "cherry", "apple"]

# Print the list:
print(mylist)

# Print list length:
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

# There are four collection data types in the Python programming language:

# 'List' is a collection which is ordered and changeable. Allows duplicate members.
# 'Tuple' is a collection which is ordered and unchangeable. Allows duplicate members.
# 'Set' is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# 'Dictionary' is a collection which is ordered** and changeable. No duplicate members.
# -----------------------------------------------------------------------------------------------------------
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

# -----------------------------------------------------------------------------------------------------------
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

# -----------------------------------------------------------------------------------------------------------
# To add an item to the end of the list, use the append() method:
list9 = ["apple", "banana", "cherry"]
list9.append("orange")
print(list9)

# The insert() method inserts an item at the specified index:
mylist1 = ["apple", "banana", "cherry"]
mylist1.insert(1, "orange")
print(mylist1)

# To append elements from another list to the current list, use the extend() method:
mylist2 = ["apple", "banana", "cherry"]
thislist = ["mango", "pineapple", "papaya"]
mylist2.extend(thislist)
print(mylist2)

# The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.):
mylist3 = ["apple", "banana", "cherry"]
thistruple = ("kiwi", "orange")
mylist3.extend(thistruple)
print(mylist3)

# -----------------------------------------------------------------------------------------------------------
#  The remove() method removes the specified item:
mylist3 = ["apple", "banana", "cherry"]
mylist3.remove("banana")
print(mylist3)

# The pop() method removes the specified index:
mylist4 = ["apple", "banana", "cherry"]
mylist4.pop(1)
print(mylist4)

# If you do not specify the index, the pop() mehtod removes the last item:
mylist5 = ["apple", "banana", "cherry"]
mylist5.pop()
print(mylist5)

# The del keyword also removes the specified index:
mylist6 = ["apple", "banana", "cherry"]
del mylist6[0]
print(mylist6)

# the del keyword can also delete the list completely:
mylist7 = ["apple", "banana", "cherry"]
del mylist7

#the clear() method empties the list, the list remains, but has no  content:
mylist8 = ["apple", "banna", "cherry"]
mylist8.clear()
print(mylist8)

# -----------------------------------------------------------------------------------------------------------
# you can loop through the list items use a for loop:
mylist9 = ["apple", "banana", "cherry"]
for x in mylist9:
    print(x)

# You can also loop through the list items by referring to their index number.

# Use the range() and len() functions to create a suitable iterable:
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
    print(thislist[i])

# You can loop through the list items by using a while loop.

# Use the len() function to determine the length of the list, then start at 0 and loop your way through the list items by refering to their indexes.

# Remember to increase the index by 1 after each iteration:
thislist = ["mango", "orange", "cherry"]
i = 0
while i < len(thislist):
    print(thislist[i])
    i = i + 1

# List Comprehension offers the shortest syntax for looping through lists, A short hand for loop that will print all items in a list:
mylist = ["Milk", "Bread", "Potato"]
[print(x) for x in mylist]

# -----------------------------------------------------------------------------------------------------------
# List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

# Example:

# Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name.

# Without list comprehension you will have to write a for statement with a conditional test inside:
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
    if "a" in x:
        newlist.append(x)
print(newlist)

# With list comprehesion you can do all that with only one line of code:

# The Syntax: newlist = [expression for item in iterable if condition == True]

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]

print(newlist)

# The condition is like a filter that only accepts the items that valuate to True, Only accept items that are not "apple"
# The condition if x != "apple"  will return True for all elements other than "apple", making the new list contain all fruits except "apple":
newlist = [x for x in fruits if x != "apple"]
print(newlist)

# The condition is optional and can be omitted, with no if statement:
newlist = [x for x in fruits]
print(newlist)

# The iterable can be any iterable object, like a list, set etc
#  You can use the range() function to create an iterable:
newlist = [x for x in range(10)]
print(newlist)

# Same example, but with a condition, accecpt only numbers lower than 5:
newlist = [x for x in range(10) if x < 5]
print(newlist)

# The 'expression' is the current item in the iteration, but it is also the outcome, which you can manipulate before it ends up like a list item in the new list:
newlist = [x.upper()for x in fruits]
print(newlist)

# You can set the outcome to whatever you like:
newlist = ["hello" for x in fruits]
print(newlist)

# The expression can also contain conditions, not like a filter, but as a way to manipulate the outcome:
# The epression: "Return the item if it is not banana, if it is banana return orange".
fruits = ["apple", "banana", "orange", "kiwi", "mango"]
newlist =[x if x !="banana" else "orange" for x in fruits]
print(newlist)

# -----------------------------------------------------------------------------------------------------------
# List objects have sort() method that will sort the list  alphanumerically, ascending, by default:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

# Sort the list numerically:
thisnumlist = [100, 50, 65, 82, 23]
thisnumlist.sort()
print(thisnumlist)\


# To sort descending, use the keyword argument reverse = Ture:
thislist.sort(reverse = True)
print(thislist) 

thisnumlist.sort(reverse = True)
print( thisnumlist)

# You can also customize your own function by using the keyword argument key = function.

# The function will return a number that will be used to sort the list (the lowest number first)

# Sor the list based on how close the number is to 50:
def myfunc(n):
    return abs(n - 65)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

# By defualt the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters:

# Case sensitive sorting can give an unexpected result:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

#  use built-in functions as key functions when sorting a list.

# So if you want a case-insensitive sort function, use str.lower as a key function:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

# What if you want to reverse the order of a list, regardless of the alphabet?

# The reverse() method reverses the current sorting order of the elements:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

# -----------------------------------------------------------------------------------------------------------
# You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2.

# There are ways to make a copy, one way is to use the built-in List method copy():
thislist = ["Milk", "Bread", "Potato"]
mylist = thislist.copy()
print(mylist)

# Another way to make a copy is to use the built-in method list():
thislist = ["banana", "Orange", "Kiwi", "cherry"]
mylist = list(thislist)
print(thislist)

# -----------------------------------------------------------------------------------------------------------
# There are several ways to join, or concatenate, two or more lists in Python.

# One of the easiest ways are by using the + operator.
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

# Another way to join two list is by appending all the items from list2 into list1, one by one:
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

for x in list2:
    list1.append(x)

print(list1)

# Or you can use the extend() method, which purpose is to add elements from one list to another list:
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)

# -----------------------------------------------------------------------------------------------------------
# Python has a set of built-in methods that you can use on lists.

# Method	Description
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	  Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list
