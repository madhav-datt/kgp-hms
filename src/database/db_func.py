#
# Software Engineering Lab - Assignment 5
# IIT Kharagpur - Hall Management System
#

"""
@ authors: Madhav Datt (14CS30015), Avikalp Srivastava (14CS10008)
"""

import ctypes
import mysql.connector
from PyQt4 import QtGui
from mysql.connector import errorcode


def connect():
    """
    Set initial connection with MySQL server, with hmsuser credentials
    Handle errors through codes
    Function only opens connection, does not close
    """

    # Sign-in credentials for MySQL server
    config = {
        'user': 'hmsuser',
        'password': 'hmspasstmp',
        'host': 'localhost',
        'database': 'hmskgp',
    }

    try:
        cnx = mysql.connector.connect(**config)
        cnx.autocommit = True

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
           # QtGui.QMessageBox.information('Delete?', 'Are you sure you want to delete this item?')
            ctypes.windll.user32.MessageBoxA(0, "Incorrect credentials, please contact your administrator",
                                             "Database Error", 1)
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            ctypes.windll.user32.MessageBoxA(0, "Database does not exist, please contact your administrator",
                                             "Database Error", 1)
        else:
            ctypes.windll.user32.MessageBoxA(0, err, " Please contact your administrator",
                                             "Database Error", 1)

    else:
        return cnx

    return None


def add(table, **param):
    """
    Add tuple to specified database table
    Order of database entries must be followed exactly

    Example:
    add("student", password = "secretword", name = "John", address = "home",
    contact_number = "9876543210", hall_ID = 4, room_no = "B-334",
    mess_charge = 250.5, room_type = "S")
    """

    # MySQL statements to add to tables
    # Passed parameters must exactly match attribute order
    # Creates row with default values:
    #   string_parameter: 'parameter'
    #   numerical_value: 0
    #   boolean_value: 'False'
    add_student = ("INSERT INTO student "
                   "(password, name, address, contact_number, hall_ID, room_no, mess_charge, room_type) "
                   "VALUES ('password', 'name', 'address', 'contact', 0, 'room', 0, 'U')")

    add_warden = ("INSERT INTO warden "
                  "(password, name, email, hall_ID, controlling_warden) "
                  "VALUES ('password', 'name', 'email', 0, 'False')")

    add_hall = ("INSERT INTO hall "
                "(name, warden_ID, clerk_ID, mess_manager_ID, status, \
                single_room_count, double_room_count, single_room_occupancy, \
                double_room_occupancy, single_room_rent, double_room_rent, \
                amenities_charge, mess_account, amenities_account, repair_account, \
                salary_account, others_account, rent_account) "
                "VALUES ('name', 0, 0, 0, 'U', 0, 0, 0, 0, 0, 0, 0, 0, \
                0, 0, 0, 0, 0)")

    add_worker = ("INSERT INTO worker "
                  "(password, name, worker_type, monthly_salary, daily_wage, \
                  hall_ID, monthly_attendance) "
                  "VALUES ('password', 'name', 'U', 0, 0, 0, 0)")

    add_complaint = ("INSERT INTO complaint "
                     "(student_ID, action_status, description, action_report) "
                     "VALUES (0, 'U', 'description', 'action report')")

    add_hmc = ("INSERT INTO hmc "
               "(password, payment_is_active) "
               "VALUES ('password', 'False')")

    add_grant_request = ("INSERT INTO grant_request "
                         "(repair_charge, other_charge, salary_charge, hall_ID) "
                         "VALUES (0, 0, 0, 0)")

    cnx = connect()
    cursor = cnx.cursor()

    # Insert new row of data into table
    if table == "student":
        cursor.execute(add_student)  # , param)
    elif table == "warden":
        cursor.execute(add_warden, param)
    elif table == "hall":
        cursor.execute(add_hall, param)
    elif table == "worker":
        cursor.execute(add_worker, param)
    elif table == "complaint":
        cursor.execute(add_complaint, param)
    elif table == "hmc":
        cursor.execute(add_hmc, param)
    elif table == "grant_request":
        cursor.execute(add_grant_request, param)
    else:
        ctypes.windll.user32.MessageBoxA(0, "Table not recognized. Insert failed",
                                         "Database Error", 1)
        return None

    # Commit to database
    cnx.commit()

    primary_key = cursor.lastrowid
    cursor.close()
    cnx.close()

    return primary_key


def update(table, primary_key, field, value):
    """
    Update field value in table using corresponding Primary Key
    Can only update one field at a time
    """

    cnx = connect()
    cursor = cnx.cursor()

    update_row = "UPDATE {} SET {} = '{}' WHERE {} = {}"

    # Update row of data from table
    if table == "student":
        cursor.execute(update_row.format(table, field, value, "student_ID", primary_key))
    elif table == "warden":
        cursor.execute(update_row.format(table, field, value, "warden_ID", primary_key))
    elif table == "hall":
        cursor.execute(update_row.format(table, field, value, "hall_ID", primary_key))
    elif table == "worker":
        cursor.execute(update_row.format(table, field, value, "worker_ID", primary_key))
    elif table == "complaint":
        cursor.execute(update_row.format(table, field, value, "complaint_ID", primary_key))
    elif table == "hmc":
        update_row = "UPDATE {} SET {} = '{}'"
        cursor.execute(update_row.format(table, field, value))
    elif table == "grant_request":
        cursor.execute(update_row.format(table, field, value, "grant_ID", primary_key))
    else:
        ctypes.windll.user32.MessageBoxA(0, "Table not recognized. Update failed",
                                         "Database Error", 1)

    # Commit to database
    cnx.commit()
    cursor.close()
    cnx.close()


def get(table, primary_key, field):
    """
    Query database to get field from a particular table using Primary Key value
    Can only get one field at a time
    """

    cnx = connect()
    cursor = cnx.cursor()

    query = "SELECT {} FROM {} WHERE {} = {}"

    # Query data from table
    if table == "student":
        cursor.execute(query.format(field, table, "student_ID", primary_key))
    elif table == "warden":
        cursor.execute(query.format(field, table, "warden_ID", primary_key))
    elif table == "hall":
        cursor.execute(query.format(field, table, "hall_ID", primary_key))
    elif table == "worker":
        cursor.execute(query.format(field, table, "worker_ID", primary_key))
    elif table == "complaint":
        cursor.execute(query.format(field, table, "complaint_ID", primary_key))
    elif table == "grant_request":
        cursor.execute(query.format(field, table, "grant_ID", primary_key))
    elif table == "hmc":
        query = "SELECT {} FROM {}"
        cursor.execute(query.format(field, table))
    else:
        ctypes.windll.user32.MessageBoxA(0, "Table not recognized. Query failed",
                                         "Database Error", 1)

        cursor.close()
        cnx.close()
        return None

    # Get queried value as array with one data value
    queried = cursor.fetchone()

    cursor.close()
    cnx.close()
    return queried[0]


def delete(table, primary_key):
    """
    Delete value from table corresponding to Primary Key
    """

    cnx = connect()
    cursor = cnx.cursor()

    delete_row = "DELETE FROM {} WHERE {} = {}"

    # Delete row of data from table
    if table == "student":
        cursor.execute(delete_row.format(table, "student_ID", primary_key))
    elif table == "warden":
        cursor.execute(delete_row.format(table, "warden_ID", primary_key))
    elif table == "hall":
        cursor.execute(delete_row.format(table, "hall_ID", primary_key))
    elif table == "worker":
        cursor.execute(delete_row.format(table, "worker_ID", primary_key))
    elif table == "complaint":
        cursor.execute(delete_row.format(table, "complaint_ID", primary_key))
    elif table == "grant_request":
        cursor.execute(delete_row.format(table, "grant_ID", primary_key))
    else:
        ctypes.windll.user32.MessageBoxA(0, "Table not recognized. Delete failed",
                                         "Database Error", 1)

    cnx.commit()
    cursor.close()
    cnx.close()
