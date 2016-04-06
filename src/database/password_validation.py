#
# Software Engineering Lab - Assignment 5
# IIT Kharagpur - Hall Management System
#

"""
@ authors: Madhav Datt (14CS30015), Avikalp Srivastava (14CS10008)
"""

from __future__ import division
import warnings
import bcrypt
import re

def hash_password(password):
    """
    Hash a password for the first time using bcrypt from pypi
    Add a randomly-generated salt
    """
    return bcrypt.hashpw(password, bcrypt.gensalt())

def check_password(password, correct_password):
    """
    Check that a unhashed password matches one that has previously been
    """
    if bcrypt.hashpw(password, correct_password) == correct_password:
        return True

    return False

def is_valid(password):
    """
    Check if passed plain-text string is a valid password
    Valid passwords - minimum criteria:
        8 characters
        1 capital letter
        1 numerical value
        no spaces
    """

    present_capital = re.search(r'[A-Z]', password, re.M)
    present_num = re.search(r'\d', password, re.M)

    if (len(password) >= 8) and (" " not in password) and present_capital and present_num:
        return True

    return False
