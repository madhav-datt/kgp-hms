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


class Complaint(object):
    """Contains details of Complaint lodged by Student

    Attributes:
        complaint_ID: Integer to uniquely identify complaint
        student_ID: Integer to uniquely identify student who lodged the complaint
        action_status: "P" for pending, "T" for action taken
        description: String with Complaint description
        action_report: String with ATR
    """

    def __init__(self, student_ID, action_status, description, action_report,
                 rebuild=False, complaint_ID=None):
        """
        Init Complaint with details given by Student
        """

        # The rebuild flag, if true, denotes that the object is being made from
        # data already present in the database
        # If False, a new data row is added to the specific table
        if not rebuild:
            self.complaint_ID = db.add("complaint")
        else:
            self.complaint_ID = complaint_ID

        self.student_ID = student_ID
        self.action_status = action_status
        self.description = description
        self.action_report = action_report

    # complaint_ID getter functions
    @property
    def complaint_ID(self):
        return self._complaint_ID

    @complaint_ID.setter
    def complaint_ID(self, complaint_ID):
        self._complaint_ID = complaint_ID

    # student_ID getter and setter functions
    @property
    def student_ID(self):
        return self._student_ID

    @student_ID.setter
    def student_ID(self, student_ID):
        self._student_ID = student_ID
        db.update("complaint", self.complaint_ID, "student_ID", self.student_ID)

    # action_status getter and setter functions
    @property
    def action_status(self):
        return self._action_status

    @action_status.setter
    def action_status(self, action_status):
        self._action_status = action_status
        db.update("complaint", self.complaint_ID, "action_status", self.action_status)

    # description getter and setter functions
    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        self._description = description
        db.update("complaint", self.complaint_ID, "description", self.description)

    # action_report getter and setter functions
    @property
    def action_report(self):
        return self._action_report

    @action_report.setter
    def action_report(self, action_report):
        self._action_report = action_report
        db.update("complaint", self.complaint_ID, "action_report", self.action_report)

    def view(self):
        """
        Return formatted string with details of complaint
        String includes complaint_ID, description, action_status & action_report
        """

        complaint_string = ("%d: %s\n\n"
                            "Action Status: %s\n"
                            "Action Report: %s")

        # Designate Action Status details
        if self.action_status == "P":
            action_status_report = "Pending"
        else:
            action_status_report = "Taken"

        return (complaint_string, (self.complaint_ID, self.description,
                                   action_status_report, self.action_report))

    def remove(self):
        """
        Delete object from database, consequently from the system
        Delete complete database tuple
        """

        db.delete("complaint", self.complaint_ID)
        del self
