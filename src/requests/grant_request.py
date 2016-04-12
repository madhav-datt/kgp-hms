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


class GrantRequest(object):
    """Contains details of grant request made by warden
    Each GrantRequest corresponds to a specific Hall (hall_ID)

    Attributes:
        hall_ID: Uniquely identify created GrantRequest
        repair_charge: Float
        other_charge: Float
    """

    def __init__(self, hall_ID, salary_charge, repair_charge, other_charge, rebuild=False,
                 grant_ID=None):
        """
        Init GrantRequest Object with details from Warden
        """

        # The rebuild flag, if true, denotes that the object is being made from
        # data already present in the database
        # If False, a new data row is added to the specific table
        if not rebuild:
            self.grant_ID = db.add("grant_request")
            self.hall_ID = hall_ID
            self.repair_charge = repair_charge
            self.other_charge = other_charge
            self.salary_charge = salary_charge
        else:
            self.grant_ID = grant_ID
            self._hall_ID = hall_ID
            self._repair_charge = repair_charge
            self._other_charge = other_charge
            self._salary_charge = salary_charge

    # grant_ID getter and setter functions
    @property
    def grant_ID(self):
        return self._grant_ID

    @grant_ID.setter
    def grant_ID(self, grant_ID):
        self._grant_ID = grant_ID

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
        return self._salary_charge

    @salary_charge.setter
    def salary_charge(self, salary_charge):
        self._salary_charge = salary_charge
        db.update("grant_request", self.grant_ID, "salary_charge", self.salary_charge)

    def approve(self, salary_charge, other_charge, repair_charge, hall_table):
        """
        Approve GrantRequest by HMC
        Amounts will be added to Hall Accounts based on approved request
        Pass parameter hall_table = dbr.rebuild("hall")
        """

        hall_table[self.hall_ID].salary_account = \
            hall_table[self.hall_ID].salary_account + salary_charge
        hall_table[self.hall_ID].others_account = \
            hall_table[self.hall_ID].others_account + other_charge
        hall_table[self.hall_ID].repair_account = \
            hall_table[self.hall_ID].repair_account + repair_charge

        db.delete("grant_request", self.grant_ID)
        del self

    def reject(self):
        """
        Reject GrantRequest by HMC
        Delete request from database and notify warden
        """

        db.delete("grant_request", self.grant_ID)
        del self
