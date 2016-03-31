#
# Software Engineering Lab - Assignment 5
# IIT Kharagpur - Hall Management System
#

"""
@ authors: Madhav Datt (14CS30015), Avikalp Srivastava (14CS10008)
"""

from __future__ import division
from database import db_func as db
from databade import password_validation as pv
import warnings

class Student(object):
    """Contains details of Student

    Attributes:
        student_ID: Integer to uniquely identify student
        password: Hashed string after adding salt
        name: String
        address: String
        contact_number: String
        photograph: Image
        hall_ID: Integer to identify hall of residence
        room_no: String
        room_type: "S" for single, "D" for double room
        mess_charge: Float with mess charges payable by student
        total_dues: Float with calculation of total amount due by student
    """

    def __init__(self, student_ID, password, name, gender, address,
                contact_number, photograph, hall_ID, room_no, room_type):
        """
        Init Student with details from Admission Letter
        """

        self.student_ID = student_ID
        self.password = password
        self.name = name
        self.address = address
        self.contact_number = contact_number
        self.photograph = photograph
        self.hall_ID = hall_ID
        self.room_no = room_no
        self.room_type = room_type

        # Mess charges payable by student
        self.mess_charge = 0.
        self.total_dues = 0.

    # student_ID getter and setter functions
    @property
    def student_ID(self):
        return self._student_ID

    @student_ID.setter
    def student_ID(self, student_ID):
        self._student_ID = student_ID

    # password getter and setter functions
    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = password

    # name getter and setter functions
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    # address getter and setter functions
    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, address):
        self._address = address

    # contact_number getter and setter functions
    @property
    def contact_number(self):
        return self._contact_number

    @contact_number.setter
    def contact_number(self, contact_number):
        self._contact_number = contact_number

    # photograph getter and setter functions
    @property
    def photograph(self):
        return self._photograph

    @photograph.setter
    def photograph(self, photograph):
        self._photograph = photograph

    # hall_ID getter and setter functions
    @property
    def hall_ID(self):
        return self._hall_ID

    @hall_ID.setter
    def hall_ID(self, hall_ID):
        self._hall_ID = hall_ID

    # room_no getter and setter functions
    @property
    def room_no(self):
        return self._room_no

    @room_no.setter
    def room_no(self, room_no):
        self._room_no = room_no

    # room_type getter and setter functions
    @property
    def room_type(self):
        return self._room_type

    @room_type.setter
    def room_type(self, room_type):
        self._room_type = room_type

    # mess_charge getter and setter functions
    @property
    def mess_charge(self):
        return self._mess_charge

    @mess_charge.setter
    def mess_charge(self, mess_charge):
        self._mess_charge = mess_charge

    # total_dues getter function
    @property
    def total_dues(self):
        """
        Calculate total dues payable by student
        total_dues = room_rent + mess_charges + amenities_charges
        """
        return self.mess_charge +

        #TODO: Add based on DB querying functionalities
