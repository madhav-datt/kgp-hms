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

# Sign-in credentials for MySQL server
config = {
  'user': 'hmsuser',
  'password': 'hmspasstmp',
  'host': 'localhost',
  'database': 'hmskgp',
}

def set_connect():
    """
    Set initial connection with MySQL server, with hmsuser credentials
    Handle errors through codes
    """

    try:
        cnx = mysql.connector.connect(**config)

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print "Incorrect credentials, please contact your administrator"
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print "Database does not exist, please contact your administrator"
        else:
            print err + " Please contact your administrator"

    else:
        cnx.close()

    #TODO return cnx

def add():

def update():

def get():

def get_object():

def delete():
