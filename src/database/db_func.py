#
# Software Engineering Lab - Assignment 5
# IIT Kharagpur - Hall Management System
#

"""
@ authors: Madhav Datt (14CS30015), Avikalp Srivastava (14CS10008)
"""

import warnings
import mysql.connector
from mysql.connector import errorcode
from __future__ import print_function

# Sign-in credentials for MySQL server
config = {
  'user': 'hmsuser',
  'password': 'hmspasstmp',
  'host': 'localhost',
  'database': 'hmskgp',
}

def connect():
    """
    Set initial connection with MySQL server, with hmsuser credentials
    Handle errors through codes
    Function only opens connection, does not close
    """

    try:
        cnx = mysql.connector.connect(**config)

    except mysql.connector.Error as err: #TODO Don't print, throw as notification/box
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print "Incorrect credentials, please contact your administrator"
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print "Database does not exist, please contact your administrator"
        else:
            print err + " Please contact your administrator"

    else:
        return cnx

    return None

def add(table, **param):
    """
    Add tuple to specified database table
    Order of database entries must be followed exactly

    Example:
    add("student", name = "John", password = "secretword", address = "home",
    contact_number = "9876543210", hall_ID = 4, room_no = "B-334",
    mess_charge = 250.5, room_type = "S")
    """

    # MySQL statements to add to tables
    # Passed parameters must exactly match attribute order
    add_student = ("INSERT INTO student "
                    "(password, name, address, contact_number, hall_ID, room_no, \
                    mess_charge, room_type) "
                    "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")

    add_warden = ("INSERT INTO warden "
                    "(password, name, email, hall_ID) "
                    "VALUES (%s, %s, %s, %s)")

    add_hall = ("INSERT INTO hall "
                "(name, warden_ID, clerk_ID, mess_manager_ID, status, \
                single_room_count, double_room_count, single_room_occupancy, \
                double_room_occupancy, single_room_rent, double_room_rent, \
                amenities_charge, mess_account, amenities_account, repair_account, \
                salary_account, others_account, rent_account) "
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, \
                %s, %s, %s, %s, %s)")

    add_worker = ("INSERT INTO worker "
                    "(name, email, worker_type, monthly_salary, daily_wage, \
                    hall_ID, monthly_attendance) "
                    "VALUES (%s, %s, %s, %s, %s, %s, %s)")

    add_complaint = ("INSERT INTO complaint "
                    "(student_ID, action_status, description, action_report) "
                    "VALUES (%s, %s, %s, %s)")



    cnx = connect()
    if table == "student":



def update():

def get():

def get_object():

def delete():
