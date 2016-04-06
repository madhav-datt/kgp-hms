#
# Software Engineering Lab - Assignment 5
# IIT Kharagpur - Hall Management System
#

"""
@ authors: Madhav Datt (14CS30015), Avikalp Srivastava (14CS10008)
"""

from workers import clerk, mess_manager
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

def authenticate(table, user_ID, password):
    """
    Authenticate login with entered user_ID and password
    Check table to match and return True if correct
    """

    if table == "clerk":
        table_data = db.build("worker")
        for key in table_data:
            if table_data[key].worker_ID == user_ID and \
            isinstance(table_data[key], clerk.Clerk) and \
            check_password(password, table_data[key].password):
                return True

    elif table == "mess_manager":
        table_data = db.build("worker")
        for key in table_data:
            if table_data[key].worker_ID == user_ID and \
            isinstance(table_data[key], mess_manager.MessManager) and \
            check_password(password, table_data[key].password):
                return True

    elif table == "student":
        table_data = db.build(table)
        for key in table_data:
            if table_data[key].student_ID == user_ID and \
            check_password(password, table_data[key].password):
                return True

    elif table == "warden":
        table_data = db.build(table)
        for key in table_data:
            if table_data[key].warden_ID == user_ID and \
            check_password(password, table_data[key].password):
                return True

    elif table == "hmc":
        table_data = db.build(table)
        for key in table_data:
            if check_password(password, table_data[key].password):
                return True

    return False
