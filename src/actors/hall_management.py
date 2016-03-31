#
# Software Engineering Lab - Assignment 5
# IIT Kharagpur - Hall Management System
#

"""
@ authors: Madhav Datt (14CS30015), Avikalp Srivastava (14CS10008)
"""

from __future__ import division
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
        self.password = password;

    # password getter and setter functions
    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = password
