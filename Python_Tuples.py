# Tuples are used to store multiple items in a single variable.

# Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.

# A tuple is a collection which is ordered and unchangeable.

# Tuples are written with round brackets.

# Create a Tuple:
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
