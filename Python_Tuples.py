# Tuples are used to store multiple items in a single variable.

# Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.

# A tuple is a collection which is ordered and unchangeable.

# Tuples are written with round brackets.

# Create a Tuple:
import this


thistuple = ("apple", "banana", "cherry")
print(thistuple)

# Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.

# Tuples allow duplicate values:
mytuple = ("apple", "banana", "cherry", "apple", "cherry")
print(mytuple)

# Print the number of items in the tuple
atuple = ("apple", "banana", "cherry")
print(len(atuple))

# To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.
btruple = ("apple",)
print(type(btruple))

# Tuple items can be of any data type:
tuple1 = ("apple", "banna", "cherry")
tuple2 = (1, 6, 7, 9, 3)
tuple3 = (True, False, False)

# A tuple with strings, integers and boolean values:
tuple3 = ("abc", 34, True, 40, "male")

# It is also possible to use the tuple() constructor to make a tuple.
tuple4 = tuple(("apple", "banana", "cherry")) # Note the double brackets
print(tuple4)

# You can access tuple items by referring to the index number, inside square brackets:
tuple5 = ("apple", "banana", "cherry")
print(tuple5[1])

# You can negative index
tuple6 = ("apple", "banana", "cherry")
print(tuple6[-1])

# You can specify a range of indexes 
tuple7 = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(tuple7[2:5])

# By leaving out the start value, the range will start at the first item:
tuple8 = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(tuple8[:4])

# By leaving out the end value, the range will go on to the end of the list:
tuple9 = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(tuple9[2:])

# Specify negative indexes if you want to start the search from the end of the tuple:
mytuple1 = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(mytuple1[-4:-1])

# To determine if a specifed item is present in a tuple use the in keyword:
mytuple2 = ("apple", "banana", "cherry")
if "apple" in mytuple2:
    print("yes, 'apple' is in the fruits tuple")

# --------------------------------------------------------------------------------------------
# Tuples are unchangeable, meaning that you cannot change, add, or remove items once the tuple is created.

# But there are some workarounds. You can convert the tuple into a list, change the list, and convert the list back into a tuple.
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

# Since tuples are immutable, they do not have a build-in append() method, but there are other ways to add items to a tuple.
# Same again convert to a list:
mytuple3 = ("apple", "banana", "cherry")
y =list(mytuple3)
y.append("orange")
mytuple3 = tuple(y)
print(mytuple3)

# Add a tuple to a tuple:
mytuple4 = ( "apple", "banana", "cherry")
y = ("orange",)
mytuple4 += y
print(mytuple4)

# Tuples are unchangeable, so you cannot remove items from it, but you can use the same workaround:
mytuple5 = ("apple", "banana", "cherry")
y = list(mytuple5)
y.remove("apple")
mytuple5 = tuple(y)
print(mytuple5)

# or you can delete the tuple completely:
mytuple6 = ("apple", "banana", "cherry")
del mytuple6
print(mytuple6) # This will raise an error because the tuple no longer exists

# ---------------------------------------------------------------------------------------------------

# Unpacking a Tuples
# When we create a tuple, we normally assign values to it. This is called "packing" a tuple:
fruits = ("apple", "banana", "cherry")
# But, in Python, we are also allowed to extend the values back into variables. This is called "unpacking":
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

# If the number of variables is less than the number of values, you can add an * 
# to the variable name and the values will be assigned to the variable as a list:
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(blue, orange, *purple) = fruits

print(blue)
print(orange)
print(purple)

# If the asterisk is added to another variable name than the last, 
# Python will assign values to the variable until the number of values left matches the number of variables left.
fruits = ("apple", "mango", "banana", "orange", "cherry")

(blue, *green, red) = fruits

print(blue)
print(green)
print(red)

# You can loop through the tuple items by using a for loop.
thistuple2 = ("apple", "banana", "orange")
for x in thistuple2:
    print(x)

# You can also loop through the tuple items by referring to their index number.
# Use the range() and len() functions to create a suitable iterable

thistuple3 = ("apple", "banana", "cheery")
for i in range(len(thistuple3)):
    print(thistuple3[1])

# You can loop through the list items by using a while loop
#Use the len() function to determine the length of the tuple, then start at 0 and loop your way through the tuple items by refering to their indexes.
#Remember to increase the index by 1 after each iteration.

thistuple4 = ("apple", "banana", "orange")
i = 0
while i < len(thistuple4):
    print(thistuple4[i])
    i = i + 1 

# ------------------------------------------------------------------------------------------
# To join two or more tuples you can use the + operator:
tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)

# If you want to multiply the content of a tuple a given number of times, you can use the * operator:
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2

print(mytuple)
