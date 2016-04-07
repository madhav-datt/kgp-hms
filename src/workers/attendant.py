
# Software Engineering Lab - Assignment 5
# IIT Kharagpur - Hall Management System
#

"""
@ authors: Madhav Datt (14CS30015), Avikalp Srivastava (14CS10008)
"""

from database import db_func as db
import warnings
import worker

class Attendant(worker.Worker):
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

    def __init__(self, name, hall_ID, daily_wage, monthly_attendance,
                rebuild = False, worker_ID = None):
        """
        Init MessManager with details as recruited by HMC or Warden
        """

        worker.Worker.__init__(self, name, hall_ID, 0, 0, daily_wage, monthly_attendance)
        self.total_wage = 0.

        # The rebuild flag, if true, denotes that the object is being made from
        # data already present in the database
        # If False, a new data row is added to the specific table
        if rebuild == False:
            self.worker_ID = db.add("Worker", name = self.name,
            worker_type = "A", monthly_salary = 0, daily_wage = self.daily_wage,
            hall_ID = self.hall_ID, monthly_attendance = self.monthly_attendance)
        else:
            self.worker_ID = worker_ID

    # daily_wage getter and setter functions
    @property
    def daily_wage(self):
        return self._daily_wage

    @daily_wage.setter
    def daily_wage(self, daily_wage):
        self._daily_wage = daily_wage
        db.update("worker", self.worker_ID, "daily_wage", self.daily_wage)

    # monthly_attendance getter and setter functions
    @property
    def monthly_attendance(self):
        return self._monthly_attendance

    @monthly_attendance.setter
    def monthly_attendance(self, monthly_attendance):
        self._monthly_attendance = monthly_attendance
        db.update("worker", self.worker_ID, "monthly_attendance", self.monthly_attendance)

    # total_wage getter functions
    @property
    def total_wage(self):
        return self.daily_wage * self.monthly_attendance
