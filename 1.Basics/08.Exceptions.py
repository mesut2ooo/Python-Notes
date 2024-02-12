################################
#   Try Except:
################################
# Error handling is needed where the program behave like we didn't expect it to be
# Some scenarios like:
# 1.Reading a file that doesn't exist
# 2.Connecting to a remote server that is offline
# 3.Bad user input
# Errors are like TypeError, NameError, etc.


# The syntax is as follows:
# try:
#     # Code that might cause an error
# except:
#     # Handle error


# Catching specific exception:
# try:
#     # Code that might cause an error
# except ValueError as error:
#     # Code to handle the exception


# Catching multiple exceptions:
# try:
#     # code that may cause an exception
# except ValueError as e1:
#     # handle exception
# except TypeError as e2:
#     # handle exception
# except ZeroDivisionError as e3:
#     # handle exception 
# except Exception as error:
#     # handle the remaing errors that are not named before here

# Or
# except (ValueError,ZeroDivisionError):
#     # handle the exceptions

################################
#   Try Except Finally:
################################
# finally clause executes wether an exception occurs or not
# try:
#     # code that may cause exceptions
# except:
#     # code that handle exceptions
# finally:
#     # code that clean up

# For situations when you cannot handle the exception but you want to clean up resources:
# try:
#     # the code that may cause an exception
# finally:
#     # the code that always executes

################################
#   Try Except Else:
################################
# We use else when the errors don't occur:
# try:
#     # code that may cause errors
# except:
#     # code that handle exceptions
# else:
#     # code that executes when no exception occurs

# We can also use finally statement for cleaning up and it will run afterall
