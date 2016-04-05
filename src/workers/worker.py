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
import warnings

class Worker(object):
    """Contains details of Worker Instance

    Attributes:
        worker_ID: Integer to uniquely identify worker
        name: String
        hall_ID: Integer to uniquely identify hall
        monthly_salary: Float
        daily_wage: Float
        monthly_attendance: Integer with monthly attendance count for daily workers
    """

    def __init__(self, name, hall_ID, password = None, monthly_salary = None,
                daily_wage = None, monthly_attendance = None):
        """
        Init Worker with details as recruited by HMC or Warden
        """

        self.password = None
        self.name = name
        self.hall_ID = hall_ID
        self.monthly_salary = monthly_salary
        self.daily_wage = daily_wage
        self.monthly_attendance = monthly_attendance
        self.worker_ID = worker_ID

    # name getter and setter functions
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name
        db.update("worker", self.worker_ID, "name", self.name)

    # hall_ID getter and setter functions
    @property
    def hall_ID(self):
        return self._hall_ID

    @hall_ID.setter
    def hall_ID(self, hall_ID):
        self._hall_ID = hall_ID
        db.update("worker", self.worker_ID, "hall_ID", self.hall_ID)

    def remove(self):
        """
        Delete object from database, consequently from the system
        Delete complete database tuple
        """

        db.delete("worker", self.worker_ID)
        del self
