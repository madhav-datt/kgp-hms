#
# Software Engineering Lab - Assignment 5
# IIT Kharagpur - Hall Management System
#

"""
@ authors: Madhav Datt (14CS30015), Avikalp Srivastava (14CS10008)
"""

from ..database import db_func as db
from ..database import db_rebuild as dbr


class GrantRequest(object):
    """Contains details of grant request made by warden
    Each GrantRequest corresponds to a specific Hall (hall_ID)

    Attributes:
        hall_ID: Uniquely identify created GrantRequest
        repair_charge: Float
        other_charge: Float
    """

    def __init__(self, hall_ID, repair_charge, other_charge, rebuild=False,
                 grant_ID=None):
        """
        Init GrantRequest Object with details from Warden
        """
        self.hall_ID = hall_ID
        self.repair_charge = repair_charge
        self.other_charge = other_charge
        self.salary_charge = 0.

        # The rebuild flag, if true, denotes that the object is being made from
        # data already present in the database
        # If False, a new data row is added to the specific table
        if not rebuild:
            self.grant_ID = db.add("grant_request",
                                   repair_charge=self.repair_charge,
                                   other_charge=self.other_charge,
                                   salary_charge=self.salary_charge,
                                   hall_ID=self.hall_ID)
        else:
            self.grant_ID = grant_ID

    # hall_ID getter and setter functions
    @property
    def hall_ID(self):
        return self._hall_ID

    @hall_ID.setter
    def hall_ID(self, hall_ID):
        self._hall_ID = hall_ID
        db.update("grant_request", self.grant_ID, "hall_ID", self.hall_ID)

    # repair_charge getter and setter functions
    @property
    def repair_charge(self):
        return self._repair_charge

    @repair_charge.setter
    def repair_charge(self, repair_charge):
        self._repair_charge = repair_charge
        db.update("grant_request", self.grant_ID, "repair_charge", self.repair_charge)

    # other_charge getter and setter functions
    @property
    def other_charge(self):
        return self._other_charge

    @other_charge.setter
    def other_charge(self, other_charge):
        self._other_charge = other_charge
        db.update("grant_request", self.grant_ID, "other_charge", self.other_charge)

    # salary_charge getter and setter functions
    @property
    def salary_charge(self):
        worker_table = dbr.rebuild("worker")
        total_salary = 0.

        for key in worker_table:
            if worker_table[key].hall_ID == self.hall_ID:
                if worker_table[key].daily_wage == 0:
                    total_salary = total_salary + worker_table[key].monthly_salary
                else:
                    total_salary = total_salary + \
                                   worker_table[key].daily_wage * \
                                   worker_table[key].monthly_attendance

        return total_salary

    def approve(self, salary_charge, other_charge, repair_charge):
        """
        Approve GrantRequest by HMC
        Amounts will be added to Hall Accounts based on approved request
        """

        hall_table = dbr.rebuild("hall")

        hall_table[self.hall_ID].salary_account = \
            hall_table[self.hall_ID].salary_account + salary_charge
        hall_table[self.hall_ID].other_charge = \
            hall_table[self.hall_ID].other_charge + other_charge
        hall_table[self.hall_ID].repair_charge = \
            hall_table[self.hall_ID].repair_charge + repair_charge

        db.delete("grant_request", self.grant_ID)
        del self

    def reject(self):
        """
        Reject GrantRequest by HMC
        Delete request from database and notify warden
        """

        db.delete("grant_request", self.grant_ID)
        del self
