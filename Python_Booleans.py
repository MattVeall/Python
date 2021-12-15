# In programming you often need to know if an expression is True or False.

# You can evaluate any expression in Python, and get one of two answers, True or False.

# When you compare two values, the expression is evaluated and Python returns the Boolean answer:
print(10 > 9)
print(10 == 9)
print(10 < 9)

# When you run a condition in an if statement, python returns True or False:
a = 200
b = 33

if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

# The bool() function allows you to evaluate any value, and give you True or False in return:
print(bool("hello"))
print(bool(15))

# Evaluate two variables:
x = "hello"
y = 15

print(bool(x))
print(bool(y))

# Almost any value is evaluated to True if it has some sort of content.

# Any string is True, except empty strings.

# Any number is True, except 0.

# Any list, tuple, set, and dictionary are True, except empty ones.

# The following will return True:
bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

# There are not many values that evaluate to False, except empty values, 

# Such as (), [], {}, "", the number 0, and the value None. 

# And of course the value False evaluates to False.

# The following will return False:
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))

# One more value, or object in this case, evaluates to False,

# and that is if you have an object that is made from a class with a __len__ function that returns 0 or False:
class myclass():
    def __len__(self):
        return 0

myobj = myclass()
print(bool(myobj))

# You can create functions that returns a boolean Value:
def myfuction() :
    return True

print(myfuction())

# You can execute code based on the Boolean answer of a function:
def myfunction() :
    return True

if myfuction():
    print("YES!")
else:
    print("No!")

# Python also has many built-in functions that return a boolean value, 

# like the isinstance() function, which can be used to determine if an object is of a certain data type:
x = 200
print(isinstance(x,int))
