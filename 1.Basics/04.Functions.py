################################
#   Intro:
################################
# A function is a block of a reusable code 
# There is a declaration and calling for the functions
# Functions can take parameters or not
# Functions can return a value or not

# Definition
def function(parameters):
    """ doc string for this function """
    body

# Calling 
function(arguements)

# Without parameter and return
def greet():
    print("Hi")

# Without return
def greet(name):
    print(f"Hi {name}")

# With parameter and return
def greet(name):
    return f"Hi {name}"

################################
#   Default Parameters:
################################
def function(param1, param2 = value2, param3 = value3):
    pass

# NOTE: Place the parameters with the default values after other parameters,
# otherwise it will generate a syntax error

################################
#   Keyword Arguements:
################################
# To change the positions of the arguements in function call we use this feature
def get_net_price(price, discount):
    return price * (1-discount)

net_price = get_net_price(discount = .1, price = 100)

# Once you used a keyword arguement , you should use keyword arguements for the remaining parameters.
def get_net_price(price, tax=0.07, discount=0.05):
    return price * (1 + tax - discount)

# net_price = get_net_price(100, tax=.08, .06) # This will generate an error
net_price = get_net_price(100, tax = .08, discount = .06) # This is the right form

################################
#   Recursion:
################################
# Recursive function is a function that calls itself until it doesn't.

# def fn():
#     #.....
#     if condition:
#         # Stop calling the function , maybe return some value
#     else:
#         fn()

# Recursive function always has a stop condition

################################
#   Lambda:
################################
# Lambada functions are ananymous(without names) and have one expression
lambda parameters: expression
# It's equivalent to this:
def ananymous(parameters):
    return expression
# It is useful for cases like 
# 1. Function that accepts a function
def get_full_name(first_name, last_name, formatter):
    return formatter(first_name, last_name)

# now we can use the usual way like 
def last_first(first_name, last_name):
    return f"{last_name} {first_name}"
full_name = get_full_name("John", "Doe", last_first)

# Or With lambda we can use 
full_name = get_full_name("John", "Doe", lambda f,l: f"{l} {f}")

# 2. Functions that return a function 
def times(n):
    return lambda x: x*n
triple = times(3)
print(triple(2))

# Lambda in a loop
callables = []
for i in (1,2,3):
    collable.append(lambda a=i: a)

for f in collables:
    print(f())

################################
#   Doc Strings:
################################
# help function gets the documentation of a function, module, class
help(print)

# Python stores the docstring in the __doc__ property of the function
# to get access to the __doc__ property of add()
add.__doc__

################################
#   Unpacking Tuples:
################################
# This will make a tuple:
numbers = 10, 20, 30

# Use unpacking to swap 2 values:
x = 10
y = 20
x, y = y, x

# To unpack too many items(with dummy variable)
x, y, _ = 10, 20, 30

# Left handside *:
r, g, *other = (1, 2, 3, 4, 5)

# Right handside *:
odds = (1, 3, 5)
evens = (2, 4, 6)
numbers = (*odds, *evens)

################################
#   *Args:
################################
# It's about *args parameters and how to use them for variadic functions
def add(x, y, *args):
    total = x + y
    for arg in args:
        total += arg

    return total

# then we pass a tuple for args(zero, one or more parameters):
result = add(10, 20, 30, 40)

# args name is by convinient, however you can use *numbers for example.

# You can not have no more positional arguements after the keyword arguement
def add(x, y, *args, z):
    return x + y + sum(args) + z


add(10, 20, 30, 40, 50) # This will result an error
add(10, 20, 30, 40, z=50) # But this is totaly fine

# Unpacking tuples when passing
def point(x, y):
    return f'({x},{y})'

a = (0, 0)
origin = point(*a)
print(origin)

################################
#   **Kwargs:
################################
# When a function has **kwargs, it can accepts a number of keyword arguements as a dictionary
def connect(**kwargs):
    print(type(kwargs))
    print(kwargs)

connect(server='localhost', port=3306, user='root', password='Py1hon!Xt')

# To pass a dictionary
config = {'server': 'localhost',
        'port': 3306,
        'user': 'root',
        'password': 'Py1thon!Xt12'}

connect(**config)

# Using both args and kwargs:
def fn(*args, **kwargs):
    print(args)
    print(kwargs)

fn(1, 2, x=10, y=20)

################################
#   Partial Functions:
################################
# In practice we use partial functions to reduce the number of arguements of a function:
def multiply(a, b):
    return a*b
def double(a):
    return multiply(a, 2)

result = double(10)

# From functools module: (functools.partial(fn,/, *args, **kwargs)
from functools import partial

def multiply(a, b):
    return a*b
double = partial(multiply, b=2)

result = double(10)
result = double(10, b=3)

################################
#   Type Hints:
################################
# We use type hints to leverage the both static and dynamic types
def say_hi(name):  # Usual
    return f'Hi {name}'
def say_hi(name: str) -> str:   # Type Hints
    return f'Hi {name}'
# parameter name has the str type and the return value has the type str

#NOTE: Python interpreter ignores the hinting completely(You need a static type checker)

####################################################
# Using mypy:
# pip install mypy
# mypy app.py

# Type hint for variable:
name: str = "John"

# Adding for multiple types:
from typing import Union
def add(x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
    return x + y
# Or we can use |:
def add(x: int | float, y: int | float) -> int | float:
    return x + y

# Type aliasing:
number = Union[int, float]
def add(x: number, y: number) -> number:
    return x + y

# For list, dictionaries, ...
ratings: list = [1, 2, 3]
# Or
from typing import List
ratings: List[int] = [1, 2, 3]

# None
# If a function doesn't return a value:
def log(message: str) -> None:
    print(message)
