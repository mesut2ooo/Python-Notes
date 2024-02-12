################################
#   Intro:
################################
# Get the current working directory
import os 
print(os.getcws())

# To change the directory:
os.chdir('/script')

# Path is os independent module
fp = os.path.join('temp', 'python')  # Joins path components
print(fp)  # temp\python (on Windows)

pc = os.path.split(fp)  # Split path components
print(pc)  # ('temp', 'python')

# To check if a path is a directory
os.path.exists(dire)
os.path.isdir(dire)

# To create a new director:
# Always check the directory is not existing
if not os.path.exists(dir):
    os.mkdir(dir)

# Renaming a directory:
import os

oldpath = os.path.join("C:\\", "temp", "python")
newpath = os.path.join("C:\\", "temp", "python3")

if os.path.exists(oldpath) and not os.path.exists(newpath):
    os.rename(oldpath, newpath)
    print("'{0}' was renamed to '{1}'".format(oldpath, newpath))

# Remove a directory:
if os.path.exists(dir):
    os.rmdir(dir)

# Travers a directory:
import os

path = "c:\\temp"
for root, dirs, files in os.walk(path):  # It returns the root, sub-dirs
    print("{0} has {1} files".format(root, len(files)))

################################
#   Listing:
################################
# To list all files in a directory you can use os.walk()

# Suppose we have a file tree like this:
# D:\web
# ├── assets
# |  ├── css
# |  |  └── style.css
# |  └── js
# |     └── app.js
# ├── blog
# |  ├── read-file.html
# |  └── write-file.html
# ├── about.html
# ├── contact.html
# └── index.html

# How to list all html files:
import os


path = 'D:\\web'

html_files = []

for dirpath, dirnames, filenames in os.walk(path):
    for filename in filenames:
        if filename.endswith('.html'):
            html_files.append(os.path.join(dirpath, filename))

for html_file in html_files:
    print(html_file)

# Make more usable:
import os


def list_files(path, extentions=None):
    """ List all files in a directory specified by path
    Args:
        path - the root directory path
        extensions - a iterator of file extensions to include, pass None to get all files.
    Returns:
        A list of files specified by extensions
    """
    for root, _, files in os.walk(path):
        for file in files:
            if extentions is None:
                yield os.path.join(root, file)
            else:
                for ext in extentions:
                    if file.endswith(ext):
                        yield os.path.join(root, file)


if __name__ == '__main__':
    filepaths = list_files(r'D:\web', ('.html', '.css'))
    for filepath in filepaths:
        print(filepath)
# yield returns a generator object to the one who calls the function
