#
# Software Engineering Lab - Assignment 5
# IIT Kharagpur - Hall Management System
#

"""
@ authors: Madhav Datt (14CS30015), Avikalp Srivastava (14CS10008)
"""

import re

def valid_email(email):
    """
    Check if email string entered is valid
    """

    if re.match(r'^[^@]+@[^@]+\.[^@]+$', email):
        return True
    return False


def valid_phone(contact_number):
    """
    Check if contact number string entered is valid
    """

    if re.match(r'[789]\d{9}', contact_number):
        return True
    return False

def int_input(input_str):
    """
    Parse passed text string input to integer
    Return None if input contains characters apart from digits
    """

    try:
        input_val = int(input_str)
    except ValueError:
        input_val = None

    return input_val

def float_input(input_str):
    """
    Parse passed text string input to float
    Return None if input contains characters apart from digits
    """

    try:
        input_val = float(input_str)
    except ValueError:
        input_val = None

    return input_val
