################################
#   Intro:
################################
# Set is an unordered list of immutable elements
# Like in math, sets doesn't accept duplicate elements
skills = {'Python programming','Databases', 'Software design'}

# You can pass an iterable to set function
characters = set('letter')
print(characters)

# Get the size:
len(characters)

'l' in characters  # Check if there is 'l' in the set
'l' not in characters # Reverse boolean

# Add to a set
characters.add("sg")

# Removing from a set
characters.remove("sg")
characters.discard("sg") # It doesn't raise an error
characters.pop() # It return and removes a random element
characters.clear() # Removes all the elements

# To make a set an immutable:
new_characters = frozenset(characters)

# Loop through them
for char in characters:
    print(char)
for index, char in enumerate(characters):
    print(f"{index} : {char}")

################################
#   Set Comprehension:
################################
tags = {'Django', 'Pandas', 'Numpy'}
# Usual way:
lowercase_tags = set()
for tag in tags:
    lowercase_tags.add(tag.lower())
# Usual way with lambda:
lowercase_tags = set(map(lambda tag: tag.lower(), tags))

# With comprehension
lowercase_tags = {tag.lower() for tag in tags}
# With comprehension and if
new_tags = {tag.lower() for tag in tags if tag != 'Numpy'}

################################
#   Mix Sets:
################################
s1 = {'Python', 'Java'}
s2 = {'C#', 'Java'}

# To make the union of two sets:
s = s1.union(s2)
s = s1 | s2

# To make the intersection of two sets:
s = s1.intersection(s2)
s = s1 & s2

# To make the difference(it's more like minus of the sets):
s = s1.difference(s2)
s = s1 - s2

# Symmetric difference:
s = s1.symmetric_difference(s2)
s = s1 ^ s2


# NOTE: operators only accepts sets , but method can accepts any iterable like list or set

################################
#   Relations:
################################
# Subset:
numbers = {1, 2, 3, 4, 5}
scores = {1, 2, 3}

print(scores.issubset(numbers)) # Subset method
print(scores <= numbers) # Subset operator
print(scores < numbers) # Proper subset

print(numbers.issuperset(scores)) # SuperSet method
print(numbers >= scores) # SuperSet operator
print(numbers > scores) # Proper superSet operator

# Disjoint (Completely different)
letters = {'A', 'B', 'C'}
alphanumerics = {'A', 1, 2}

result = letters.isdisjoint(alphanumerics)
