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

    def __init__(password):
        """
        Init Hall Management as a singleton class on with initial details
        """
        # TODO: Make a singleton class
        self.password = pv.hash_password(password)

    # password getter and setter functions
    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = pv.hash_password(password)

    def activate_payment_link(self):
        """
        Activate link for payment by Student
        Used by Student to pay total_dues
        """
