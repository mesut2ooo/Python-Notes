################################
#   Formatted Strings:
################################
# F string is a better way instead of format() method
first_name = 'John'
last_name = 'Doe'
s = F'Hello, {" ".join((first_name, last_name))}!'

# Multi line f-string:
name = 'John'
website = 'PythonTutorial.net'

message = (
    f'Hello {name}. '
    f"You're learning Python at {website}."
)
# or
message = f'Hello {name}. ' \
          f"You're learning Python at {website}."
# or
message = f"""Hello {name}.
You're learning Python at {website}."""

# Multiple curly braces:
s = f'{{1+2}}'  # {1+2}
s = f'{{{1+2}}}'   # {1+2}
s = f'{{{{1+2}}}}'   # {{1+2}}
# python replaces each pair of doubled curly braces with a single one

# Python evaluates curly braces from left to right

# Format numbers using f string
number = 16
s = f'{number:x}'   # Hexa decimal
s = f'{number:e}'   # Scientific Notation
s = f'{number: 06}'     # Pad zeros  --> 00200
s = f'{number: .2f}'    # Number of decimal places --> 16.00
number = 400000000000
s = f'{number: ,}'  # also can use _ --> 400,000,000,000

# Show the number with percentage
number = 0.1259
s = f'{number: .2%}'
print(s)  # 12.59%

s = f'{number: .1%}'
print(s)  # 12.5%


# There is also more sophisticated patterns

################################
#   Raw Strings:
################################
# It is useful to use raw strings when you're dealing with many backslashes
# like regular expressions or directory paths
s1 = r'lang\tver\nPython\t3'
s2 = 'lang\\tver\\nPython\\t3'

print(s1 == s2) # True

# Since \ scapes the ' or " , a raw string can not end with odd number of \s:
s = r'\\\'   # this will rais an error '

# Convert to a raw string
s = '\n'
raw_string = repr(s)

raw_string = repr(s)[1:-1]      # To remove the quotes

################################
#   Back Slash:
################################
# Backslash is used for scape sequence
# \n      #new line
# \t      #tab
# \'      # single quote '
# \"      # single double qoute "


# You can not use backslash in f strings
colors = ['red','green','blue']
# s = f'The RGB colors are:\n {'\n'.join(colors)}'  # Error

# instead
colors = ['red','green','blue']
rgb = '\n'.join(colors)
s = f"The RGB colors are:\n{rgb}"

# In raw strings a back slash is just a literal

