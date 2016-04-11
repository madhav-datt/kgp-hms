#
# IIT Kharagpur - Hall Management System
# System to manage Halls of residences, Warden grant requests, student complaints
# hall worker attendances and salary payments
#
# MIT License
#

"""
@ authors: Madhav Datt, Avikalp Srivastava
"""

import bcrypt


def hash_password(password):
    """
    Hash a password for the first time using bcrypt from pypi
    Add a randomly-generated salt
    """

    return bcrypt.hashpw(password, bcrypt.gensalt())


def check_password(password, correct_password):
    """
    Check that a un-hashed password matches one that has previously been
    """

    if bcrypt.hashpw(str(password), correct_password.encode('utf-8')) == correct_password.encode('utf-8'):
        return True

    return False
