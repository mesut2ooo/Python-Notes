################################
#   If Else:
################################
# Just one if
# if condition:   # If the condition is true
#     if-blocks
#     if-blocks

# if and else
# if conditon:
#     if-blocks
# else:   # If the condition is false
#     else-blocks

# if, elif, else
# if if-condition:
#     if-blocks
# elif elif-condition1:
#     elif-blocks1
# elif elif-condition2:
#     elif-blocks2
# else:
#     else-block

# It will iterate successively and when one of them is true , it ignores the rest

################################
#   Ternary:
################################
# It is the same as if else
value_if_true if condition else value_if_false
# For example:
price = 20 if int(age) >= 18 else 5

################################
#   For With Range:
################################
# In python there is a function called range
# :: range(start, stop, step)

for index in range(5):
    print(index)

for index in range(1,6):
    print(index)

for index in range(1,10,3):
    print(index)

# Again: note that it includes start and excludes stop

################################
#   While:
################################
# The format is like this:
while condition:
  body
# We call this a pretest loop because the condition is being checked first
# If the condition is always true, it will be an indefinite loop
################################
#   Break:
################################
# It will break the loop (for/while) immidiately
#       Whenever it is run
while statement1:
    if statement2:
        break

################################
#   Continue:
################################
# It will skip the current iteration and start the next one
while statement1:
    if statement2:
        continue

################################
#   Pass:
################################
# It acts as a placeholder and we tend to use it 
#   wherever we don't want to do anything
class Stream:
    pass

if statement:
    pass

def fn():
    pass

while condition:
    pass

# NOTE: If we don't use it and just leave the place empty, we will get a syntax error

################################
#   For Else or While Else:
################################
# We can use else optionally after the for loop
# else clause will execute only if the loop executes normally(if the loop dosen't encouter a break)
# or it will execute when the iterable has no item
people = [{'name': 'John', 'age': 25},
        {'name': 'Jane', 'age': 22},
        {'name': 'Peter', 'age': 30},
        {'name': 'Jenifer', 'age': 28}]

name = input('Enter a name:')

for person in people:
    if person['name'] == name:
        print(person)
        break
else:
    print(f'{name} not found!')

# It is also true for while loops
# If the loop doesn't executes normally (encounter a break)
fruit = input("Enter a fruit name: ")
index = 0

while index < len(fruit):
    # check the fruit name
    if fruit[index] == 'a':
        print("This fruit has 'a'")
        break

    index += 1
else:
    print("This fruit has no 'a' in its name")

################################
#   Do While:
################################
# Python doesn't support the do while loop 
# But we can emulate this like 
# while True:
#     # code block

#     # break out of the loop
#     if condition
#         break

# It will run at least one time
