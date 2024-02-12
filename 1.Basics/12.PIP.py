################################
#   PyPI, PIP:
################################
# Third party
# 1. PyPI
# It is a great python package repository
# You can use these website packages freely
# Package version
# major.minor.patch
# Major: changes that are not backward compatible
# Minor: changes that are backwards compatible, and have new features
# Patch: minor changes and bug fixes

# 2. pip
# pip is a command that let you install packages from PyPI or other repos
# pip --V # Shows the pip version
# pip install requests  # Install the requests package
# pip install requests==2.20.1  # Install the specific version

# pip list # list all installed packages
# pip list --outdated

# pip uninstall package

# pip show package  # Shows the package and it's dependencies

################################
#   Virtual Environments:
################################
# Where system packages are stored:
import sys
print(sys.prefix)

# Where third party packages are stored:
import site
print(site.getsitepackages())

# virtual environment are for sometimes that you have multiple projects and each one needs a specific versions of libraries
# python -m venv project_env

# Activate the environment
# Project_env/scripts/activate

# use where command
# where python
