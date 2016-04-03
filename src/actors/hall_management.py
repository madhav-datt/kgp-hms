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
from requests import printer
import warnings

class HallManagement(object):
    """Contains details of HallManagement

    Attributes:
        password: Hashed string after adding salt
    """

    def __init__(self, password, rebuild = false):
        """
        Init Hall Management as a singleton class on with initial details
        """

        # The rebuild flag, if true, denotes that the object is being made from
        # data already present in the database
        # If false, a new data row is added to the specific table
        if rebuild == false:
            self._password = pv.hash_password(password)
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
