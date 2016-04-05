#
# Software Engineering Lab - Assignment 5
# IIT Kharagpur - Hall Management System
#

"""
@ authors: Madhav Datt (14CS30015), Avikalp Srivastava (14CS10008)
"""

from __future__ import division
from database import db_func as db
from database import password_validation as pv
from requests import printer
import warnings

class HallManagement(object):
    """Contains details of HallManagement
    Paramater "*" must be passed wherever primary key is required for db operations
    Attributes:
        password: Hashed string after adding salt
    """

    def __init__(self, password, rebuild = False, payment_is_active = False):
        """
        Init Hall Management as a singleton class on with initial details
        """

        self.payment_is_active = False

        # The rebuild flag, if true, denotes that the object is being made from
        # data already present in the database
        # If False, a new data row is added to the specific table
        if rebuild == False:
            self._password = pv.hash_password(password)
            db.add("hmc", "password" = self.password)
        else:
            self.password = password

    # password getter and setter functions
    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = pv.hash_password(password)
        db.update("hmc", "*", "password", self.password)

    def activate_payment_link(self):
        """
        Activate link for payment by Student
        Used by Student to pay total_dues
        """

        self.payment_is_active = true
        db.update("hmc", "*", "payment_is_active", self.payment_is_active)

    def activate_payment_link(self):
        """
        Activate link for payment by Student
        Used by Student to pay total_dues
        """

        self.payment_is_active = true
        db.update("hmc", "*", "payment_is_active", self.payment_is_active)

    def deactivate_payment_link(self):
        """
        Activate link for payment by Student
        Used by Student to pay total_dues
        """

        self.payment_is_active = False
        db.update("hmc", "*", "payment_is_active", self.payment_is_active)