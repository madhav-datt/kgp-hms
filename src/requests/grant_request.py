#
# Software Engineering Lab - Assignment 5
# IIT Kharagpur - Hall Management System
#

"""
@ authors: Madhav Datt (14CS30015), Avikalp Srivastava (14CS10008)
"""

from __future__ import division
from database import db_func as db

class GrantRequest(object):
    """Contains details of grant request made by warden
    Each GrantRequest corresponds to a specific Hall (hall_ID)

    Attributes:
        hall_ID: Uniquely identify created GrantRequest
        clerk_salary: Float
        attendant_salary: Float
        gardener_salary: Float
        other_charges: Float
        attendant_count: Integer
        gardener_count: Integer
    """

    def __init__(self, hall_ID, clerk_salary, gardener_salary, attendant_salary,
                other_charges, attendant_count, gardener_count, rebuild = false,
                grant_ID = None):
        """
        Init GrantRequest Object with details from Warden
        """
        self.hall_ID = hall_ID
        self.clerk_salary = clerk_salary
        self.attendant_salary = attendant_salary
        self.gardener_salary = gardener_salary
        self.other_charges = other_charges
        self.attendant_count = attendant_count
        self.gardener_count = gardener_count

        # The rebuild flag, if true, denotes that the object is being made from
        # data already present in the database
        # If false, a new data row is added to the specific table
        if rebuild == false:
            self.grant_ID = db.add("grant_request",
            "clerk_salary" = self.clerk_salary,
            "gardener_salary" = self.gardener_salary,
            "attendant_salary" = self.attendant_salary,
            "other_charges" = self.other_charges,
            "attendant_count" = self.attendant_count,
            "gardener_count" = self.gardener_count,
            "hall_ID" = self.hall_ID)
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

    # clerk_salary getter and setter functions
    @property
    def clerk_salary(self):
        return self._clerk_salary

    @clerk_salary.setter
    def clerk_salary(self, clerk_salary):
        self._clerk_salary = clerk_salary
        db.update("grant_request", self.grant_ID, "clerk_salary", self.clerk_salary)

    # attendant_salary getter and setter functions
    @property
    def attendant_salary(self):
        return self._attendant_salary

    @attendant_salary.setter
    def attendant_salary(self, attendant_salary):
        self._attendant_salary = attendant_salary
        db.update("grant_request", self.grant_ID, "attendant_salary", self.attendant_salary)

    # gardener_salary getter and setter functions
    @property
    def gardener_salary(self):
        return self._gardener_salary

    @gardener_salary.setter
    def gardener_salary(self, gardener_salary):
        self._gardener_salary = gardener_salary
        db.update("grant_request", self.grant_ID, "gardener_salary", self.gardener_salary)

    # other_charges getter and setter functions
    @property
    def other_charges(self):
        return self._other_charges

    @other_charges.setter
    def other_charges(self, other_charges):
        self._other_charges = other_charges
        db.update("grant_request", self.grant_ID, "other_charges", self.other_charges)

    # attendant_count getter and setter functions
    @property
    def attendant_count(self):
        return self._attendant_count

    @attendant_count.setter
    def attendant_count(self, attendant_count):
        self._attendant_count = attendant_count
        db.update("grant_request", self.grant_ID, "attendant_count", self.attendant_count)

    # gardener_count getter and setter functions
    @property
    def gardener_count(self):
        return self._gardener_count

    @gardener_count.setter
    def gardener_count(self, gardener_count):
        self._gardener_count = gardener_count
        db.update("grant_request", self.grant_ID, "gardener_count", self.gardener_count)


    def approve():
        """
        Approve GrantRequest by HMC
        Amounts will be added to Hall Accounts based on approved request
        """

        Hall.mess_account += 
        Hall.amenities_account
        Hall.salary_account
        Hall.repair_account
        Hall.others_account
        Hall.rent_account

    def reject():
        """
        Reject GrantRequest by HMC
        Delete request from database and notify warden
        """


    def view():
        """
        Return formatted string with details of grant request
        String includes grant_ID, hall_ID and provided details
        """

        grant_string = ("%d: %s\n" \
                        "Clerk Salary: %s\n \
                        Gardener Salary: %s\n \
                        Attendant Salary: %s\n \
                        Other Charges: %s\n \
                        Attendant Count: %s\n \
                        Gardener Count: %s\n")

    return grant_string, (self.grant_ID, self.hall_ID, self.clerk_salary,
            self.gardener_salary, self.attendant_salary, self.other_charges,
            self.attendant_count, self.gardener_count)
