#
# Software Engineering Lab - Assignment 5
# IIT Kharagpur - Hall Management System
#

"""
@ authors: Madhav Datt (14CS30015), Avikalp Srivastava (14CS10008)
"""

from __future__ import division
from database import db_func as db
import warnings

class MessManager(Worker):
    """Contains details of Worker Instance

    Attributes:
        worker_ID: Integer to uniquely identify worker
        name: String
        hall_ID: Integer to uniquely identify hall
        email: String
        monthly_salary: Float
        daily_wage: Float
        monthly_attendance: Integer with monthly attendance count for daily workers
    """

    def __init__(self, name, hall_ID, password, monthly_salary,
                rebuild = False, worker_ID = None):
        """
        Init MessManager with details as recruited by HMC or Warden
        """

        Worker.__init__(self, name, hall_ID, password, monthly_salary, 0, 0)

        # The rebuild flag, if true, denotes that the object is being made from
        # data already present in the database
        # If False, a new data row is added to the specific table
        if rebuild == False:
            self.password = pv.hash_password(password)
            self.worker_ID = db.add("Worker", "password" = self.password, "name" = self.name,
            "worker_type" = "M", "monthly_salary" = self.monthly_salary,
            "daily_wage" = 0, "hall_ID" = self.hall_ID, "monthly_attendance" = 0)
        else:
            self.password = password
            self.worker_ID = worker_ID

    # password getter and setter functions
    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = pv.hash_password(password)
        db.update("warden", self.warden_ID, "password", self.password)

    # monthly_salary getter and setter functions
    @property
    def monthly_salary(self):
        return self._monthly_salary

    @monthly_salary.setter
    def monthly_salary(self, monthly_salary):
        self._monthly_salary = monthly_salary
        db.update("worker", self.worker_ID, "monthly_salary", self.monthly_salary)

    def compute_mess_payment(self):
        """
        Compute total money due to hall in form of mess payments
        Sum of each student resident's mess charge
        """

        student_table = db.rebuild("student")
        mess_total = 0.

        for key in student_table:
            if student_table[key].hall_ID == self.hall_ID:
                mess_total = mess_total + student_table[key].mess_charge

        return mess_total
