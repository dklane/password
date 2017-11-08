#
###################################
# PROLOG SECTION
# new_password_basic.py
# Validates a new password being proposed through user input.
# This is the basic version of the program.
# Verifies that the password satisfies the following condition:
# - Must be at least 8 characters in length
# In this version the user gets only one try to meet the condition.
#
# Tested with Python 3.3.0 on Windows 7
# Fri Apr  5, 2013
#
# Copyright 2009-2015 National Academy Foundation. All rights reserved.
#
# Possible future enhancements:
# Unresolved bugs:
###################################

###################################
# PROCESSING INITIALIZATION SECTION
###################################
# set minimum password length
minlength = 8
# initialize the password as invalid
valid = False

###################################
# PROCESSING SECTION
# Branching code: if/else, break statement
# Looping code: for-loop
###################################
#
# get the user input
#
# prompt for the new password
password = str(input("Enter new password: "))
#
# test the conditions (in this case, only one) and report errors
#
# test the password length
if len(password) >= minlength:
    # if the password meets the condition, set valid to true
    valid = True
else:
    # otherwise, give the user a meaningful error message
    print("Error, password is less than",minlength,"characters.")

###################################   
# CLEANUP, TERMINATION, AND EXIT SECTION
###################################
# print informational messages (final status)
# if the password meets all conditions (in this case, only one)
if valid == True:
    # print the "successful" message
    print("Your new password is valid.")
# otherwise
else:
    # print the "unsuccessful" message
    print("Your new password is not valid.")
