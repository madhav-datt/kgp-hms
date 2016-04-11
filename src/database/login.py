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
        if user_ID not in table_data:
            return False
        if isinstance(table_data[user_ID], clerk.Clerk):
            if pv.check_password(password, table_data[user_ID].password):
                return True

    elif table == "mess_manager":
        table_data = dbr.rebuild("worker")
        if user_ID not in table_data:
            return False
        if isinstance(table_data[user_ID], mess_manager.MessManager):
            if pv.check_password(password, table_data[user_ID].password):
                return True

    elif table == "student":
        table_data = dbr.rebuild(table)
        if user_ID not in table_data:
            return False
        if pv.check_password(password, table_data[user_ID].password):
            return True

    elif table == "warden":
        table_data = dbr.rebuild(table)
        if user_ID not in table_data:
            return False
        if pv.check_password(password, table_data[user_ID].password):
            return True

    elif table == "hmc":
        table_data = dbr.rebuild(table)
        for key in table_data:
            if pv.check_password(password, table_data[key].password):
                return True

    return False
