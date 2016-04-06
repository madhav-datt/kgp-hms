#
# Software Engineering Lab - Assignment 5
# IIT Kharagpur - Hall Management System
#

"""
@ authors: Madhav Datt (14CS30015), Avikalp Srivastava (14CS10008)
"""

import warnings
import ctypes
import mysql.connector
from mysql.connector import errorcode
from halls import hall
from actors import student, warden, hall_management
from requests import complaint, grant_request
from workers import attendant, clerk, mess_manager, worker


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

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            ctypes.windll.user32.MessageBoxA(0, "Incorrect credentials, please contact your administrator",
            "Database Error", 1)
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            ctypes.windll.user32.MessageBoxA(0, "Database does not exist, please contact your administrator",
            "Database Error", 1)
        else:
            ctypes.windll.user32.MessageBoxA(0, err + " Please contact your administrator",
            "Database Error", 1)

    else:
        return cnx

    return None


def rebuild(table):
    """
    Rebuild object dictionary for specified table
    """

    cnx = connect()
    cursor = cnx.cursor()

    query = ("SELECT * from %s")
    data_table = {}

    if table == "student" or table == "warden" or table == "hmc" or \
        table == "hall" or table == "grant_request" or table == "worker" or \
        table == "complaint":
        cursor.execute(query, table)
    else:
        ctypes.windll.user32.MessageBoxA(0, "Table not recognized. Object build failed",
        "Database Error", 1)
        return None

    cursor.fetchall()
    for row in cursor:
        # Insert new row of data into table
        if table == "student":
            table_obj = student.Student(row[1], row[2], row[3], row[4], row[5],
                                row[6], row[8], True, row[0])

        elif table == "warden":
            table_obj = warden.Warden(row[1], row[2], row[3], row[4], row[5], True, row[0])

        elif table == "hall":
            table_obj = hall.Hall(row[1], row[5], row[6], row[7], row[10], row[11],
                            row[2], row[4], row[3], row[12], True, row[0])

            table_obj.mess_account = row[13]
            table_obj.amenities_account = row[14]
            table_obj.repair_account = row[15]
            table_obj.salary_account = row[16]
            table_obj.others_account = row[17]
            table_obj.rent_account = row[18]

        elif table == "worker":
            if row[3] == "M":
                table_obj = mess_manager.MessManager(row[2], row[6], row[1], row[4], True, row[0])
            elif row[3] == "C":
                table_obj = clerk.Clerk(row[2], row[6], row[1], row[4], True, row[0])
            elif row[3] == "A":
                table_obj = attendant.Attendant(row[2], row[6], row[5], row[7], True, row[0])

        elif table == "complaint":
            table_obj = complaint.Complaint(row[1], row[2], row[3], row[4], True, row[0])

        elif table == "hmc":
            table_obj = hall_management.HallManagement(row[0], row[1])

        elif table == "grant_request":
            table_obj = grant_request.GrantRequest(row[7], row[1], row[2], row[3], row[4],
                                                    row[5], row[6], True, row[0])

        data_table[row[0]] = table_obj

    cursor.close()
    cnx.close()

    return data_table


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
    add_student = ("INSERT INTO student "
                    "(password, name, address, contact_number, hall_ID, room_no, \
                    mess_charge, room_type) "
                    "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")

    add_warden = ("INSERT INTO warden "
                    "(password, name, email, hall_ID, controlling_warden) "
                    "VALUES (%s, %s, %s, %s, %s)")

    add_hall = ("INSERT INTO hall "
                "(name, warden_ID, clerk_ID, mess_manager_ID, status, \
                single_room_count, double_room_count, single_room_occupancy, \
                double_room_occupancy, single_room_rent, double_room_rent, \
                amenities_charge, mess_account, amenities_account, repair_account, \
                salary_account, others_account, rent_account) "
                "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, \
                %s, %s, %s, %s, %s)")

    add_worker = ("INSERT INTO worker "
                    "(password, name, worker_type, monthly_salary, daily_wage, \
                    hall_ID, monthly_attendance) "
                    "VALUES (%s, %s, %s, %s, %s, %s, %s)")

    add_complaint = ("INSERT INTO complaint "
                    "(student_ID, action_status, description, action_report) "
                    "VALUES (%s, %s, %s, %s)")

    add_hmc = ("INSERT INTO hmc "
                "(password, payment_is_active) "
                "VALUES (%s, %s)")

    add_grant_request = ("INSERT INTO grant_request "
                        "(repair_charge, other_charge, salary_charge, hall_ID) "
                        "VALUES (%s, %s, %s, %s)")

    cnx = connect()
    cursor = cnx.cursor()

    # Insert new row of data into table
    if table == "student":
        cursor.execute(add_student, param)
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
        print
        return None

    # Commit to database
    cnx.commit()

    primary_key = cursor.lastrowid()
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

    update_row = ("UPDATE %s SET %s = %s WHERE %s = %s")

    # Update row of data from table
    if table == "student":
        cursor.execute(update_row, (table, field, value, "student_ID", primary_key))
    elif table == "warden":
        cursor.execute(update_row, (table, field, value, "warden_ID", primary_key))
    elif table == "hall":
        cursor.execute(update_row, (table, field, value, "hall_ID", primary_key))
    elif table == "worker":
        cursor.execute(update_row, (table, field, value, "worker_ID", primary_key))
    elif table == "complaint":
        cursor.execute(update_row, (table, field, value, "complaint_ID", primary_key))
    elif table == "hmc":
        cursor.execute(update_row, (table, field, value, "password", primary_key))
    elif table == "grant_request":
        cursor.execute(update_row, (table, field, value, "grant_ID", primary_key))
    else:
        ctypes.windll.user32.MessageBoxA(0, "Table not recognized. Update failed",
        "Database Error", 1)

    cursor.close()
    cnx.close()


def get(table, primary_key, field):
    """
    Query database to get field from a particular table using Primary Key value
    Can only get one field at a time
    """

    cnx = connect()
    cursor = cnx.cursor()

    query = ("SELECT %s FROM %s WHERE %s = %s")

    # Query data from table
    if table == "student":
        cursor.execute(query, (field, table, "student_ID", primary_key))
    elif table == "warden":
        cursor.execute(query, (field, table, "warden_ID", primary_key))
    elif table == "hall":
        cursor.execute(query, (field, table, "hall_ID", primary_key))
    elif table == "worker":
        cursor.execute(query, (field, table, "worker_ID", primary_key))
    elif table == "complaint":
        cursor.execute(query, (field, table, "complaint_ID", primary_key))
    elif table == "grant_request":
        cursor.execute(query, (field, table, "grant_ID", primary_key))
    elif table == "hmc":
        cursor.execute(query, (field, table, "password", primary_key))
    else:
        ctypes.windll.user32.MessageBoxA(0, "Table not recognized. Query failed",
        "Database Error", 1)

        cursor.close()
        cnx.close()
        return None

    # Get queried value as array with one data value
    queried = curson.fetchone()

    cursor.close()
    cnx.close()
    return queried[0]


def delete(table, primary_key):
    """
    Delete value from table corresponding to Primary Key
    """

    cnx = connect()
    cursor = cnx.cursor()

    delete_row = ("DELETE FROM %s WHERE %s = %s")

    # Delete row of data from table
    if table == "student":
        cursor.execute(delete_row, (table, "student_ID", primary_key))
    elif table == "warden":
        cursor.execute(delete_row, (table, "warden_ID", primary_key))
    elif table == "hall":
        cursor.execute(delete_row, (table, "hall_ID", primary_key))
    elif table == "worker":
        cursor.execute(delete_row, (table, "worker_ID", primary_key))
    elif table == "complaint":
        cursor.execute(delete_row, (table, "complaint_ID", primary_key))
    elif table == "grant_request":
        cursor.execute(delete_row, (table, "grant_ID", primary_key))
    else:
        ctypes.windll.user32.MessageBoxA(0, "Table not recognized. Delete failed",
        "Database Error", 1)

    cursor.close()
    cnx.close()
