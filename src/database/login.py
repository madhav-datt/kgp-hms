#
# Software Engineering Lab - Assignment 5
# IIT Kharagpur - Hall Management System
#

"""
@ authors: Madhav Datt (14CS30015), Avikalp Srivastava (14CS10008)
"""

import password_validation as pv
import re
import db_rebuild as dbr
from ..workers import clerk, mess_manager


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
        table_data = dbr.rebuild("worker")
        for key in table_data:
            if table_data[key].worker_ID == user_ID and \
                    isinstance(table_data[key], clerk.Clerk) and \
                    pv.check_password(password, table_data[key].password):
                return True

    elif table == "mess_manager":
        table_data = dbr.rebuild("worker")
        for key in table_data:
            if table_data[key].worker_ID == user_ID and \
                    isinstance(table_data[key], mess_manager.MessManager) and \
                    pv.check_password(password, table_data[key].password):
                return True

    elif table == "student":
        table_data = dbr.rebuild(table)
        for key in table_data:
            if table_data[key].student_ID == user_ID and \
                    pv.check_password(password, table_data[key].password):
                return True

    elif table == "warden":
        table_data = dbr.rebuild(table)
        for key in table_data:
            if table_data[key].warden_ID == user_ID and \
                    pv.check_password(password, table_data[key].password):
                return True

    elif table == "hmc":
        table_data = dbr.rebuild(table)
        for key in table_data:
            if pv.check_password(password, table_data[key].password):
                return True

    return False
