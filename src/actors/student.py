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


class Student(object):
    """Contains details of Student

    Attributes:
        student_ID: Integer to uniquely identify student
        password: Hashed string after adding salt
        name: String
        address: String
        contact_number: String
        hall_ID: Integer to identify hall of residence
        room_no: String
        room_type: "S" for single, "D" for double room
        mess_charge: Float with mess charges payable by student
        total_dues: Float with calculation of total amount due by student
    """

    def __init__(self, password, name, address, contact_number,
                 hall_ID, room_no, room_type, mess_charge, rebuild=False, student_ID=None):
        """
        Init Student with details from Admission Letter
        """

        # The rebuild flag, if true, denotes that the object is being made from
        # data already present in the database
        # If False, a new data row is added to the specific table
        if not rebuild:
            self.student_ID = db.add("student")
            self.password = password
            self.room_type = room_type
            self.hall_ID = hall_ID

            # Update hall room occupancy based on room allocation to Student if rebuild is False
            if self.room_type == "S":
                curr_occupancy = int(db.get("hall", self.hall_ID, "single_room_occupancy")[0])
                db.update("hall", self.hall_ID, "single_room_occupancy", int(curr_occupancy) + 1)
            elif self.room_type == "D":
                curr_occupancy = int(db.get("hall", self.hall_ID, "double_room_occupancy")[0])
                db.update("hall", self.hall_ID, "double_room_occupancy", int(curr_occupancy) + 1)

            self.name = name
            self.address = address
            self.contact_number = contact_number
            self.room_no = room_no
            self.room_type = room_type

            # Mess charges payable by student
            self.mess_charge = mess_charge
        else:
            self.student_ID = student_ID
            self._password = password
            self._hall_ID = hall_ID
            self._room_type = room_type
            self._name = name
            self._address = address
            self._contact_number = contact_number
            self._room_no = room_no
            self._room_type = room_type

            # Mess charges payable by student
            self._mess_charge = mess_charge

    # student_ID getter functions
    @property
    def student_ID(self):
        return self._student_ID

    @student_ID.setter
    def student_ID(self, student_ID):
        self._student_ID = student_ID

    # password getter and setter functions
    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = pv.hash_password(password)
        db.update("student", self.student_ID, "password", self.password)

    # name getter and setter functions
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name
        db.update("student", self.student_ID, "name", self.name)

    # address getter and setter functions
    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, address):
        self._address = address
        db.update("student", self.student_ID, "address", self.address)

    # contact_number getter and setter functions
    @property
    def contact_number(self):
        return self._contact_number

    @contact_number.setter
    def contact_number(self, contact_number):
        self._contact_number = contact_number
        db.update("student", self.student_ID, "contact_number", self.contact_number)

    # hall_ID getter and setter functions
    @property
    def hall_ID(self):
        return self._hall_ID

    @hall_ID.setter
    def hall_ID(self, hall_ID):
        self._hall_ID = hall_ID
        db.update("student", self.student_ID, "hall_ID", self.hall_ID)

    # room_no getter and setter functions
    @property
    def room_no(self):
        return self._room_no

    @room_no.setter
    def room_no(self, room_no):
        self._room_no = room_no
        db.update("student", self.student_ID, "room_no", self.room_no)

    # room_type getter and setter functions
    @property
    def room_type(self):
        return self._room_type

    @room_type.setter
    def room_type(self, room_type):
        self._room_type = room_type
        db.update("student", self.student_ID, "room_type", self.room_type)

    # mess_charge getter and setter functions
    @property
    def mess_charge(self):
        return self._mess_charge

    @mess_charge.setter
    def mess_charge(self, mess_charge):
        self._mess_charge = mess_charge
        db.update("student", self.student_ID, "mess_charge", self.mess_charge)

    # total_dues getter function
    @property
    def total_dues(self):
        """
        Calculate total dues payable by student
        total_dues = room_rent + mess_charges + amenities_charges
        """

        if self.room_type == "S":
            room_rent = db.get("hall", self.hall_ID, "single_room_rent")[0]
        elif self.room_type == "D":
            room_rent = db.get("hall", self.hall_ID, "double_room_rent")[0]

        return self.mess_charge + room_rent + \
               db.get("hall", self.hall_ID, "amenities_charge")[0]
