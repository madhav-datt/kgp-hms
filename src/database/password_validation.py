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

def hash_password(password):
    """
    Hash a password for the first time using bcrypt from pypi
    Add a randomly-generated salt
    """
    return bcrypt.hashpw(password, bcrypt.gensalt())

def auth_password(password, correct_password):
    """
    Check that a unhashed password matches one that has previously been
    """
    if bcrypt.hashpw(password, correct_password) == correct_password:
        return true

    return false
