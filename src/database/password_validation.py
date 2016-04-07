#
# Software Engineering Lab - Assignment 5
# IIT Kharagpur - Hall Management System
#

"""
@ authors: Madhav Datt (14CS30015), Avikalp Srivastava (14CS10008)
"""

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
