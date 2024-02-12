################################
#   Intro:
################################
# A list is an ordered collection of items
new_list = [1,3.5, "43"]

# We could have a list in a list:
coordinates = [[0, 0], [1, 3]]

# Accessing the elements by indexes from 0:
persons[1]
persons[-2] # Or reverse access like strings

numbers = [1, 3, 6, 2, 6]
numbers[1] = 2 # Modify the second element to 2
numbers.append(9) # Adding the number 9 at the end of the list
numbers.insert(1, 100) # insert the number 100 in the second place: 1,100,3.
del numbers[2] # Removing the third element of the list
numbers.pop() # delete the last element
numbers.remove(6) # removing the first number 6

################################
#   Tuple:
################################
# A tuple is an immutable list
rgb = ('red', 'green', 'blue')
numbers = (1,) # To define an one item tuple

################################
#   Sort:
################################
# To sort the items in a list
numbers.sort()
numbers.sort(reverse=True) # For reverse sorting

# To use it on a list of tuples
# First we need to define a key to search
companies = [('Google', 2019, 134.81),
             ('Apple', 2019, 260.2),
             ('Facebook', 2019, 70.7)]

# define a sort key (this metod instead of lambda
#def sort_key(company):
#    return company[2]
#companies.sort(key=sort_key, reverse=True)

# sort the companies by revenue
companies.sort(key=lambda company: company[2])

# show the sorted companies
print(companies)

#There is also a function like sort
new_numbers = sorted(numbers)
new_numbers = sorted(numbers, reverse=True)

################################
#   Slice:
################################
# This is all similar to the slicing of the strings
colors[::2]
colors[-3:]
# The default values for the start is 0 and the stop is the last element 
# The default value for step is 1
colors[::-1] # Reverse the list

# Substitute part of the list
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
colors[0:2] = ['black', 'white']

# Substitute and resize the list
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
colors[0:2] = ['black', 'white', 'gray']

# Slice to delete a part of the list
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
del colors[2:5]

################################
#   Unpacking:
################################
# We can automatically assign a list to some variables
colors = ['red', 'blue', 'green']
red, blue, green = colors

# If you want to unpack a list to some variables and the remaining to a list:
colors = ['red', 'blue', 'green']
red, blue, *other = colors
# In this case other will be a list

################################
#   Iteration:
################################
# We can iterate through a list using for and in
cities = ['New York', 'Beijing', 'Cairo', 'Mumbai', 'Mexico']
for city in cities:
    print(city)

# The enumerate function returns a tuple that contains the current indexes and elements of a list
for item in enumerate(cities):  # Default enumeration
    print(item)

for index, city in enumerate(cities):   # Unpacking the enumerations
    print(f"{index}: {city}")

for index, city in enumerate(cities,1):     # unpacking the enumerations and also start indexing from 1
    print(f"{index}: {city}")

################################
#   Finding Index:
################################
# To get the index of an element we use index method
cities = ['New York', 'Beijing', 'Cairo', 'Mumbai', 'Mexico']
result = cities.index('Mumbai')

################################
#   Iterables:
################################
# An itereable is an object that includes 0,1,... elements
# An itereable has the ability to return its elements one at a time
# Some examples are strings , range(), lists, tuples,...

# An iterable can be iterated over
colors = ['red', 'green', 'blue']
colors_iter = iter(colors)

color = next(colors_iter)
print(color)

color = next(colors_iter)
print(color)

color = next(colors_iter)
print(color)

# cause an excpetion
color = next(colors_iter)
print(color)

# Or
colors = ['red', 'green', 'blue']
iterator = iter(colors)

for color in iterator:
    print(color)

################################
#   Map:
################################
# The map function iterates over all elements in a list/tuple, applies a function to each and return a new iterator

iterator = map(function, list)


def double(bonus):
    return bonus * 2
bonuses = [100, 200, 300]
iterator = map(double, bonuses)

# Or
bonuses = [100, 200, 300]
iterator = map(lambda bonus: bonus*2, bonuses)

# To turn the iterator to a list:
list(iterator)

################################
#   Filter:
################################
# Iterate over elements of a list and select them based on specified criteria
filter(fn, list)
# The fn is a function that returns true/false

scores = [70, 60, 80, 90, 50]
filtered = filter(lambda score: score >= 70, scores)

print(list(filtered))

# Or on tuples
countries = [
    ['China', 1394015977],
    ['United States', 329877505],
    ['India', 1326093247],
    ['Indonesia', 267026366],
    ['Bangladesh', 162650853],
    ['Pakistan', 233500636],
    ['Nigeria', 214028302],
    ['Brazil', 21171597],
    ['Russia', 141722205],
    ['Mexico', 128649565]
]

populated = filter(lambda c: c[1] > 300000000, countries)

print(list(populated))

################################
#   Reduce:
################################
# Sometimes we want to reduce the whole list into a single value
reduce(fn, list)
# fn is a function of 2 arguements

from functools import reduce

def sum(a, b):
    print(f"a={a}, b={b}, {a} + {b} ={a+b}")
    return a + b


scores = [75, 65, 80, 95, 50]
total = reduce(sum, scores)
print(total)

# Or
from functools import reduce

scores = [75, 65, 80, 95, 50]

total = reduce(lambda a, b: a + b, scores)

print(total)

################################
#   List Comprehension:
################################
# Creating the new list from the elements of an existing one

# An example with map function is:
numbers = [1, 2, 3, 4, 5]
squares = list(map(lambda number: number**2, numbers))

# The equivalent with list comprehension:
squares = [n**2 for number in numbers]

# Now list comprehension with if:
mountains = [
    ['Makalu', 8485],
    ['Lhotse', 8516],
    ['Kanchendzonga', 8586],
    ['K2', 8611],
    ['Everest', 8848]
]

highest_mountains = list(filter(lambda m: m[1] > 8600, mountains))

# The same problem with comprehension:
highest_mountains = [m for m in mountains if m[1] > 8600]
