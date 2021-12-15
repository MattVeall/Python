print("    /|")
print("   / |")
print("  /  |")
print(" /   |")
print("/____|")

phrase = "Hello World" # assign variable (this case a string "Hello world")
# WORKING WITH STRINGS
print(len(phrase)) # tells how many characters in the variable (in the string Hello world).
print(phrase.islower()) # tells if variable is lowercase by True or false
print(phrase.isupper()) # tells if variable is uppercase by True or false
print(phrase[0]) # pulls the character designated by the number (0 1 2 3 4 5 ect)
print(phrase.upper()) # make all characters uppercase.
print(phrase.lower()) # makes all charters lowercase.
print(phrase.index("e")) # tells where the first found character is (H=0,e=1) can search whole words i.e "world"
print(phrase.replace("Hello", "Goodbye")) #replace text i.e replace Hello with Goodbye
print("Hello\nWorld") # what follows \n puts it beneath
print("Hello \"World\"") # \ cancel the string to make it a quotation
print("Hello World".upper()) # put str in capitals 

# WORKING WITH NUMBERS
from math import * # imports more Math options (module)
print(5 + 2.5) # ADD
print(5 * 2) # Multiply
print(3 * 4 + 5) # multiply then ADD
print(3 * (4 + 5)) # ADD then multiply
print(10 / 2) # Division
print(10 % 3) # Division but shows the remainder (Modulates operator.) 10 Mod 3
my_num = 5 # creates a number variable
print(str(my_num) + " this is how you turn a numbers into a string") # str can turn numbers into a string
print(str(5) + " this is how you turn a numbers into a string") # str can turn numbers into a string
my_num = -6
print(abs(my_num)) # Absolute value to get a absolute value of a number
print(pow(3, 2)) # Power. gives the number(3) the Power of (2)
print(max(4, 6)) # Max tells which number is larger
print(min(4, 6)) # min tells which number is smaller
print(round(3.7)) # round, rounds to he nearest whole number
print(floor(8.7)) # gives the lowest point of the number. (rounds down)
print(ceil(8.3)) # gives the highest point of the number. ( rounds up)
print(sqrt(36)) #  sqrt will square root the number

#USER INPUT
name = input("Enter your name: ") #input lets the user input information into the program (can make the input a variable)
age = input("Enter your age: ")
print("Hello " + name + "! You are " + age)  # prints string & input once the user inputs information.


#BASIC CALCULATOR
num1 = input("Enter a number: ") # lets user input number inter string.( must convert stri into number to get result)
num2 = input("Enter another number: ")
result = int(num1) + float(num2) #int converts the string into a integer number(whole number),
# float converts str into a decimal number

print(result)
