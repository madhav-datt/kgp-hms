#
# Software Engineering Lab - Assignment 5
# IIT Kharagpur - Hall Management System
#

"""
@ authors: Madhav Datt (14CS30015), Avikalp Srivastava (14CS10008)
"""

import bcrypt


def hash_password(password):
    """
    Hash a password for the first time using bcrypt from pypi
    Add a randomly-generated salt
    """

    return bcrypt.hashpw(password, bcrypt.gensalt()).encode('utf-8')


def check_password(password, correct_password):
    """
    Check that a un-hashed password matches one that has previously been
    """
    print password
    print correct_password.encode('utf-8')
    print bcrypt.hashpw(str(password), correct_password.encode('utf-8'))
    if bcrypt.hashpw(str(password), correct_password.encode('utf-8')) == correct_password.encode('utf-8'):
        return True

    return False
