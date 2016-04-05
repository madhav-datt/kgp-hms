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

class Warden(object):
    """Contains details of Warden

    Attributes:
        warden_ID: Integer to uniquely identify warden
        password: Hashed string after adding salt
        name: String
        email: String
        hall_ID: Integer to identify hall of residence
    """

    def __init__(self, password, name, email, hall_ID, rebuild = False,
                warden_ID = None):
        """
        Init Warden with details for object creation
        """

        self.name = name
        self.email = email
        self.hall_ID = hall_ID

        # The rebuild flag, if true, denotes that the object is being made from
        # data already present in the database
        # If False, a new data row is added to the specific table
        if rebuild == False
            self.password = pv.hash_password(password)
            self.warden_ID = db.add("warden", "password" = self.password,
            "name" = self.name, "email" = self.email, "hall_ID" = self.hall_ID)
        else:
            self.password = password
            self.warden_ID = warden_ID

    # warden_ID getter and setter functions
    @property
    def warden_ID(self):
        return self._warden_ID

    # password getter and setter functions
    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = pv.hash_password(password)
        db.update("warden", self.warden_ID, "password", self.password)

    # name getter and setter functions
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name
        db.update("warden", self.warden_ID, "name", self.name)

    # email getter and setter functions
    @property
    def address(self):
        return self._email

    @email.setter
    def email(self, email):
        self._email = email
        db.update("warden", self.warden_ID, "email", self.email)

    # hall_ID getter and setter functions
    @property
    def hall_ID(self):
        return self._hall_ID

    @hall_ID.setter
    def hall_ID(self, hall_ID):
        self._hall_ID = hall_ID
        db.update("warden", self.warden_ID, "hall_ID", self.hall_ID)
