################################
#   Intro:
################################
# Dictionary: A collection of key-value pairs.(key is immutable)
person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 25,
    'favorite_colors': ['blue', 'green'],
    'active': True
}

# Accessing values:
# 1.Using square brackets:
print(person["first_name"]) # If the element is not there, It throws an error
# 2.Get method:
print(person.get("first_name")) # If the element is not there it returns None
print(person.get("ssn", "000")) # It returns 000 if ssn doesnt exist

# To add or modify a value
dict[key] = new_value
# Delete a value
del dict[key] 

# loop through a dictionary
# items() returns a list of tuples of that dictionary
for key, value in person.items():
    print(f"{key}: {value}")


# Looping through keys only
for key in person.keys():
    print(key)
# Looping through keys only (Default)
for key in person:
    print(key)

# Looping through values
for value in person.values():
    print(value)

################################
#   Dictionary Comprehension:
################################
# 1.To transform a dictionary:

# The usual way:
stocks = {
    'AAPL': 121,
    'AMZN': 3380,
    'MSFT': 219,
    'BIIB': 280,
    'QDEL': 266,
    'LVGO': 144
}

new_stocks = {}
for symbol, price in stocks.items():
    new_stocks[symbol] = price*1.02

print(new_stocks)

# The dictionary comprehension method
new_stocks = {symbol: price * 1.02 for (symbol, price) in stocks.items()}

print(new_stocks)

# 2. To filter a dictionary:
# The usual way:
stocks = {
    'AAPL': 121,
    'AMZN': 3380,
    'MSFT': 219,
    'BIIB': 280,
    'QDEL': 266,
    'LVGO': 144
}

selected_stocks = {}
for symbol, price in stocks.items():
    if price > 200:
        selected_stocks[symbol] = price

print(selected_stocks)

# The dictionary comprehension method
selected_stocks = {s: p for (s, p) in stocks.items() if p > 200}

print(selected_stocks)
