#
# Software Engineering Lab - Assignment 5
# IIT Kharagpur - Hall Management System
#

"""
@ authors: Madhav Datt (14CS30015), Avikalp Srivastava (14CS10008)
"""

import ctypes
import db_func
from ..halls import hall
from ..actors import student, warden, hall_management
from ..requests import complaint, grant_request
from ..workers import attendant, clerk, mess_manager, worker


def rebuild(table):
    """
    Rebuild object dictionary for specified table
    """

    cnx = db_func.connect()
    cursor = cnx.cursor()

    query = "SELECT * from %s;"
    data_table = {}

    if table == "student" or table == "warden" or table == "hmc" or \
                    table == "hall" or table == "grant_request" or table == "worker" or \
                    table == "complaint":
        cursor.execute(query, (table))
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

        else:
            table_obj = None

        data_table[row[0]] = table_obj

    cursor.close()
    cnx.close()

    return data_table

