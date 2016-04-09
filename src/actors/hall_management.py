#
# Software Engineering Lab - Assignment 5
# IIT Kharagpur - Hall Management System
#

"""
@ authors: Madhav Datt (14CS30015), Avikalp Srivastava (14CS10008)
"""

from ..database import db_func as db
from ..database import password_validation as pv


class HallManagement(object):
    """Contains details of HallManagement
    Parameter "*" must be passed wherever primary key is required for db operations

    Attributes:
        password: Hashed string after adding salt
    """

    def __init__(self, password, rebuild=False, payment_is_active=False):
        """
        Init Hall Management as a singleton class on with initial details
        """

        # The rebuild flag, if True, denotes that the object is being made from
        # data already present in the database
        # If False, a new data row is added to the specific table
        if not rebuild:
            db.add("hmc")
            self.password = pv.hash_password(password)
        else:
            self.password = password

        self.payment_is_active = payment_is_active

    # password getter and setter functions
    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = pv.hash_password(password)
        db.update("hmc", "*", "password", self.password)

    # payment_is_active getter and setter functions
    @property
    def payment_is_active(self):
        return self._payment_is_active

    @payment_is_active.setter
    def payment_is_active(self, payment_is_active):
        self._payment_is_active = payment_is_active
        db.update("hmc", "*", "payment_is_active", self.payment_is_active)

    def activate_payment_link(self):
        """
        Activate link for payment by Student
        Used by Student to pay total_dues
        """

        self.payment_is_active = True

    def deactivate_payment_link(self):
        """
        Deactivate link for payment by Student
        Used by Student to pay total_dues
        """

        self.payment_is_active = False
