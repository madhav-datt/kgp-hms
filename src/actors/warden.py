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

    def __init__(self, password, name, email, hall_ID, controlling_warden = False,
                rebuild = False, warden_ID = None):
        """
        Init Warden with details for object creation
        """

        self.name = name
        self.email = email
        self.hall_ID = hall_ID
        self.controlling_warden = controlling_warden

        # The rebuild flag, if true, denotes that the object is being made from
        # data already present in the database
        # If False, a new data row is added to the specific table
        if rebuild == False
            self.password = pv.hash_password(password)
            self.warden_ID = db.add("warden", "password" = self.password,
            "name" = self.name, "email" = self.email, "hall_ID" = self.hall_ID,
            "controlling_warden" = self.controlling_warden)
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

    # controlling_warden getter and setter functions
    @property
    def controlling_warden(self):
        return self._controlling_warden

    @controlling_warden.setter
    def controlling_warden(self, controlling_warden):
        self._controlling_warden = controlling_warden
        db.update("warden", self.warden_ID, "controlling_warden", self.controlling_warden)

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

    def total_occupancy(self):
        """
        Return dictionary with occupancy of all Halls
        Works only if called on object with controlling_warden = True
        Return None if not called by controlling_warden object
        """

        if self.controlling_warden == False:
            return None

        hall_table = db.rebuild("hall")

        # Dictionary occupancy_table as elements in the following form
        # {hall_name : (single_room_occupancy, double_room_occupancy)}
        occupancy_table = {}
        for key in hall_table:
            occupancy_table[hall_table[key].name] = \
            (hall_table[key].single_room_occupancy, hall_table[key].double_room_occupancy)

        return occupancy_table
