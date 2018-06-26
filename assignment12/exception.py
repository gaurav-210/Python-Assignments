
# Q.1- Name and handle the exception occured in the following program:

# try:
#     a = 3
#     if a < 4:
#         a = a / (a - 3)
#     print(a)
#
# except ValueError:
#          print("Oops!   Try again...")
#
#          ZeroDivisionError: division by zero


# solution :
# a=3
# try:
#     if a<4:
#         a=a/(a-3)
#         print(a)
# except:
#     print("exception occur")
#
# Q.2- Name and handle the exception occurred in the following program:
# l=[1,2,3]
# print(l[3])


# l =[1,2,3]
# try:
#     print(l[3])
# except Exception:
#     print("Exception occour")
#

# Q.3- What will be the output of the following code:
#
# try:
#     raise NameError("Hi there")  # Raise Error
# except NameError:
#     print ("An exception")
#     raise  # To determine whether the exception was raised or not
#
# # Function which returns a/b
#
# # ans:-
# # An exception
# # Traceback (most recent call last):
# #   File "C:/Users/ACER/PycharmProjects/Hangman/exception.py", line 6, in <module>
# #     raise NameError("Hi there")  # Raise Error
# # NameError: Hi there

# Q.4- What will be the output of the following code:
# def AbyB(a, b):
# 	try:
# 		c = ((a + b) / (a - b))
# 	except ZeroDivisionError:
# 		print("a/b result in 0")
# 	else:
# 		print(c)
#
#
# # Driver program to test above function
# AbyB(2.0, 3.0)
# AbyB(3.0, 3.0)


# ans:-
# -5.0
# a/b result in 0

#
# Q.5- Write a program to show and handle following exceptions:
# 1. Import Error
# 2. Value Error
# 3. Index Error


# try:
#     import abc
#     print((l[3]))
# except Exception:
#     print("Exception occour for imoport error")
#
# try:
#   n=int(input("Enter name"))
#   print("hello",n)
# except Exception:
#     print("Exception occour for value error")
#
#
#
# l =[1,2,3]
# try:
#     print(l[4])
# except Exception:
#     print("Exception occour for index errror ")

#
# Q.6- Create a user-defined exception AgeTooSmallError() that warns the user when they have entered age less than 18.
# The code must keep taking input till the user enters the appropriate age number(less than 18).


class Error(Exception):
    """Base class for other exceptions"""
    pass


class AgeTooSmallError(Error):
    """Raised when the entered age is smaller than 18"""
    pass


while True:
    try:
        age = int(input("Enter Age: "))
        if age <18 :
            raise AgeTooSmallError
        break
    except AgeTooSmallError:
        print("The entered Age is too small, try again!")
        print('')

print("You entered the appropriate age value!")
