#
# IIT Kharagpur - Hall Management System
# System to manage Halls of residences, Warden grant requests, student complaints
# hall worker attendances and salary payments
#
# MIT License
#

"""
@ authors: Madhav Datt, Avikalp Srivastava
"""

from ..database import db_func as db
from ..database import password_validation as pv
import worker


class Clerk(worker.Worker):
    """Contains details of Worker Instance

    Attributes:
        worker_ID: Integer to uniquely identify worker
        name: String
        hall_ID: Integer to uniquely identify hall
        monthly_salary: Float
    """

    def __init__(self, name, hall_ID, password, monthly_salary, rebuild=False,
                 worker_ID=None):
        """
        Init Clerk with details as recruited by HMC or Warden
        """

        # The rebuild flag, if true, denotes that the object is being made from
        # data already present in the database
        # If False, a new data row is added to the specific table
        if not rebuild:
            self.worker_ID = db.add("worker")
            db.update("worker", self.worker_ID, "worker_type", "C")
            self.password = password
        else:
            self.worker_ID = worker_ID
            self._password = password

        self.monthly_salary = monthly_salary
        worker.Worker.__init__(self, self.worker_ID, name, hall_ID)

    # password getter and setter functions
    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = pv.hash_password(password)
        db.update("worker", self.worker_ID, "password", self.password)

    # monthly_salary getter and setter functions
    @property
    def monthly_salary(self):
        return self._monthly_salary

    @monthly_salary.setter
    def monthly_salary(self, monthly_salary):
        self._monthly_salary = monthly_salary
        db.update("worker", self.worker_ID, "monthly_salary", self.monthly_salary)
