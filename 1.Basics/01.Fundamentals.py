################################
#   Syntax:
################################
# This is a comment
# Python uses whitespaces for identation

# You can use \ to span statements in multiple lines like:
if (a == True) and \
        (b == False):
            print("hi")

# To list all keywords in python use:
import keyword
print(keyword.kwlist)

# Literals
a = 'This is a string'
b = "This is also a string"
c = """ This is a multiline
string"""
d = ''' This is 
also 
another
multiline string'''

################################
#   Variables:
################################
# Defining a variable
# variable_name = value
x = 1

# Naming a variable
# 1.Can contain letters, numbers, underscores, BUT can not start with a number
# 2.Can not contain whitespaces
# 3.Can not use keywords for them

################################
#   Strings:
################################
# You can use ' ' or " " for single line strings
# and """ """ or ''' ''' for multiline strings

# For quoting use:
quote = '"Beautiful is better than ugly.". Said Tim Peters'
quote = "'Beautiful is better than ugly.'. Said Tim Peters"
# Or use scape sequence:
quote = "\"Beautiful is better than ugly.\". Said Tim Peters"

# If you want to use \ as \ not as a scape sequence
# You can use raw string like:
message = r"C:\python"

# To use an string inside another string we use formatted string:
name = "John"
message = f"Hi {name}"

# Concatinating strings
greeting = "Good" "Morning!"
# Or
greeting = "Good"
time = "Afternoon"
greeting = greeting + time + "!"

# Each string is a list of characters
# You can access them by string[index]
# P     y   t   h   o   n
# 0     1   2   3   4   5           straight indexing
# -1    -2  -3  -4  -5  -6          reverse indexing
message = "Python"
print(message[0]) #P  #Exactly like message[-1]

# To get the lenght of a string (use len(string)):
print(len(greeting))

# Slicing strings
# string[start:end:step]
# include start and exclude stop
string = " This is a simple string"
string_slice1 = string[3:7]     # Slice characters 3,4,5,6
string_slice2 = string[3:]      # Slice character 3 till the end
string_slice3 = string[:7]      # Slice characters from start to 7 (exclude)
string_slice4 = string[1:10:3]  # Slice 1,4,7

# Remember that strings are immutable, this will produce an error
name = "John"
name[3] = "j"

################################
#   Numbers:
################################
# Python supports integers, floats, complex

# Operation on numbers
# +, -, *, /, //, %, **
# You can modify the order of them by ()

# The division always return an float
# If you mix a float in any operation the result will be float

# You can use underscores to represent numbers, the interpreter ignores them
count = 100_000_000

################################
#   Bool:
################################
# It only contains 2 values
is_active = True
is_admin = False

# The comparisons always return boolean
'a' < 'b'
1 > 2

# bool() function return the bool value
bool("hi")

# All the falsy values are
0       # Number zero
''      # An empty string
False   
None
[]      # An empty list
()      # An empty tuple/set
{}      # An empty dictionary

################################
#   Constants:
################################
# Python doesn't have a constant typ
# By convention we declare constants by all capital letters 
# And treat them as constants

FILE_SIZE_LIMIT = 1024

################################
#   Comments:
################################
# Python have 3 comments

# 1. Block comment
# Printing hello
print("hello")

# 2. Inline comments
print("hello") # Printing hello

# 3. Documentation string (docstring)
# NOTE: they are not ignored by the python
# a. One line docstring
def quicksort():
    """ Sort the list """

# b. Multi line docstring
def increase():
    """ Increase by:
    ratings
    1,2,3 """
# You can access them by obj.__doc__ (obj is the name of the function)
# Use docstring for functions, modules and classes

################################
#   Type Conversion:
################################
# Input function takes the inputs as a string
value = input("Enter a value: ")

# Type conversions: int(str), float(str), bool(val), str(val)
value_in_numbers = int(value)  # Or int(input("Enter a value: ")

# Returning the type of the variable
type(value)
