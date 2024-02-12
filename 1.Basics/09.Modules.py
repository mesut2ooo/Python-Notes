################################
#   Intro:
################################
# A module is a file that contains python code.
# if the file name is pricing.py , the module would be pricing

# ways to import a module:
# 1.
import pricing
# 2. 
import pricing as sell_price
# 3.
from pricing import fn, fn2
# 4.
from pricing import fn as function
# 5.
from pricing import *   # import every object in there

################################
#   Search Paths:
################################
# When you import a module 
# Python will search these pathes:
# 1. The current folder
# 2. A list of folders specified in PYTHONOPATH environment variable.
# 3. An installation-dependent folders that you configured when you installed python

# Python stores the resulting search path in the sys.path
import sys
for path in sys.path:
    print(path)

# You can add your pathes to the search path:
import sys
sys.path.append("d:\\modules\\")

################################
#   Name variable:
################################
# __name__ is called dunder name(double underscores)
# Python assign the __main__ to the __name__ var when you run the script directly and the module name if you import the script as a module

# So __name in the running main script is __main__
# And in modules is the name of the module

################################
#   Packages:
################################
# Packages is a way to group modules:
# First place all the module files in a folder
# Second create an __init__.py file
# You can define two things in this file:
# __init__.py

# import the order module automatically
from sales.order import create_sales_order

# default sales tax rate
TAX_RATE = 0.07

# When you use import *, python will look for __init__.py, if it is available# It will load all modules in a special list called __all__
# __init__.py

__all__ = [
    'order',
    'delivery'
]

# And when you import the package folder by *, it can just use order and delivery files


# We can have subpackages, These are subfolders in the main package folder

################################
#   Private Functions:
################################
# If you define a function in the module with prefix _, It will be
# private, means that you can't access it with import *
def send(email, message):
    print(f'Sending "{message}" to {email}')

def _attach_file(filename):
    print(f'Attach {filename} to the message')

# Another way is __all__:
# mail.py

__all__ = ['send']

def send(email, message):
    print(f'Sending "{message}" to {email}')

def attach_file(filename):
    print(f'Attach {filename} to the message')

