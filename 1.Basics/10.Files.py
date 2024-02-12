################################
#   Read:
################################
# To read a file in python follow these steps:
# 1. open the text file by open()
# 2. read with read(), readline(), readlines()
# 3. close with close()

# 1. Open:
open(path, mode)
path = "C:/sample/t.txt"  # If you are on windows also use /
# mode = 'r'      ,        'w',        'a'
#         reading         writing     appending

file = open("theFile.txt", "r") # The file is in the script directory


# 2. Reading:
read(size)  # Returns the string based on the size
read()  # Reads all the file and for the end of the file it returns an empty string
readline()  # Reads a line and returns that
readlines()  # Reads all files into a list of strings

# 3. Close:
file.close()  # It will close the file
# Remember to close the file always
# If you don't want to use the close open with "with":
with open("path") as f:
    contents = f.readlines()

# Examples:

# Read whole file at once:
with open('the-zen-of-python.txt') as f:
    contents = f.read()
    print(contents)

# by readlines():
with open('the-zen-of-python.txt') as f:
    [print(line.strip()) for line in f.readlines()] #.strip() is for cutting new lines

# by readline():
with open('the-zen-of-python.txt') as f:
    for line in f:
        print(line.strip())

# To open another languages use encoding="utf8 parameter in open

################################
#   Write:
################################
# To write to a file:
# 1. Use 'w' or 'a' for openning
# 2. Write to it using write() or writelines()
# 3. Close the file

# 1. Open:
# 'w'     truncates the contents as soon as file is opened
# 'a'     append to the existing file
# '+'     updating the text file, both reading and writing

# 2. Writing:
file.write("\n") # Writes a single string
file.writelines("\n") # Writes an iterable to a file

# Examples:
lines = ['Readme', 'How to write text files in Python']

with open('readme.txt', 'w') as f:
    for line in lines:
        f.write(line)
        f.write('\n')

with open('readme.txt', 'w') as f:
    f.writelines(lines)

with open('readme.txt', 'w') as f:
    f.write('\n'.join(lines))

# If you want to write another languages to the file use encoding="utf8"

################################
#   Create:
################################
# You can use 2 modes:
# 'w'     if the file exists it will erase the contents
# 'x'     Exclusive, if the exists, it will rais FileExistsError

# Examples:
with open('readme.txt', 'w') as f:
    f.write('Create a new text file!')

try:
    with open('docs/readme.txt', 'w') as f:
        f.write('Create a new text file!')
except FileNotFoundError:
    print("The 'docs' directory does not exist")

with open('readme.txt', 'x') as f:
    f.write('Create a new text file!')

################################
#   Check Existence:
################################
# To check if the file exists or not there is two approaches:
# 1. with exists() function:
from os.path import exists

file_exists = exists(path_to_file)

# 2. with is_file() method:
from pathlib import Path

path = Path(path_to_file)

path.is_file()


# We usually do this for checking files before errors

################################
#   Rename:
################################
# To rename a file we simply use:
import os

os.rename('readme.txt', 'notes.txt')

# If the file doesn't exist : FileNotFoundError
# If the destination file exists : FileExistsError

################################
#   Remove:
################################
# Simply
import os

os.remove('readme.txt')

# Be cautious of FileNotFoundError

################################
#   Read CSV:
################################
# CSV: stands for comma seperated values
# To read this:
import csv

with open('path/to/csv_file', 'r') as f:
    csv_reader = csv.reader(f)  # csv_reader is an iterable
    for line in csv_reader:
        # process each line
        print(line)

# An example:
import csv

with open('country.csv', encoding="utf8") as f:
    csv_reader = csv.reader(f)
    for line_no, line in enumerate(csv_reader, 1):
        if line_no == 1:
            print('Header:')
            print(line)  # header
            print('Data:')
        else:
            print(line)  # data

# Another way is to use DictReader
# It maps the information of each line to a dictionary whose keys are specified by the value of the first line
import csv

with open('country.csv', encoding="utf8") as f:
    csv_reader = csv.DictReader(f)
    # skip the header
    next(csv_reader)
    # show the data
    for line in csv_reader:
        print(f"The area of {line['name']} is {line['area']} km2")

# If you want to explicitly specify the keys:
import csv

fieldnames = ['country_name', 'area', 'code2', 'code3']

with open('country.csv', encoding="utf8") as f:
    csv_reader = csv.DictReader(f, fieldnames)
    next(csv_reader)
    for line in csv_reader:
        print(f"The area of {line['country_name']} is {line['area']} km2")

################################
#   Write CSV:
################################
# To write to a csv file:
# 1. open with 'w' mode
# 2. create an object by calling writer()
# 3. write data to it by writerow()/ writerows()

import csv

# open the file in the write mode
f = open('path/to/csv_file', 'w')

# create the csv writer
writer = csv.writer(f)

# write a row to the csv file
writer.writerow(row)

# close the file
f.close()

# Example of writing a to a csv
import csv

header = ['name', 'area', 'country_code2', 'country_code3']
data = [
    ['Albania', 28748, 'AL', 'ALB'],
    ['Algeria', 2381741, 'DZ', 'DZA'],
    ['American Samoa', 199, 'AS', 'ASM'],
    ['Andorra', 468, 'AD', 'AND'],
    ['Angola', 1246700, 'AO', 'AGO']
]

with open('countries.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.writer(f)

    # write the header
    writer.writerow(header)

    # write multiple rows
    writer.writerows(data)

# Writing using dictwriter
import csv

# csv header
fieldnames = ['name', 'area', 'country_code2', 'country_code3']

# csv data
rows = [
    {'name': 'Albania',
    'area': 28748,
    'country_code2': 'AL',
    'country_code3': 'ALB'},
    {'name': 'Algeria',
    'area': 2381741,
    'country_code2': 'DZ',
    'country_code3': 'DZA'},
    {'name': 'American Samoa',
    'area': 199,
    'country_code2': 'AS',
    'country_code3': 'ASM'}
]

with open('countries.csv', 'w', encoding='UTF8', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)
