#
# Software Engineering Lab - Assignment 5
# IIT Kharagpur - Hall Management System
#

"""
@ authors: Madhav Datt (14CS30015), Avikalp Srivastava (14CS10008)
"""

from ..database import db_func as db


class Hall(object):
    """Contains details of Hall

    Attributes:
        hall_ID: Integer to uniquely identify hall
        name: String
        status: Character "N" for New, "O" for Old Hall
        single_room_count: Integer
        double_room_count: Integer
        single_room_occupancy: Integer
        double_room_occupancy: Integer
        single_room_rent: Float
        double_room_rent: Float
        warden_ID: Integer to uniquely identify Hall's Warden
        mess_manager_ID: Identify Hall's MessManager
        clerk_ID: Identify Hall's Clerk
        amenities_charge: Float with fixed amenities charges
        mess_account: Float with mess account remaining
        amenities_account: Float with amenities account remaining
        repair_account: Float with repair account remaining
        salary_account: Float with salary account remaining
        rent_account: Float with rent account remaining
        others_account: Float with miscellaneous account remaining
    """

    def __init__(self, name, status, single_room_count,
                 double_room_count, single_room_rent, double_room_rent,
                 warden_ID, mess_manager_ID, clerk_ID, amenities_charge,
                 rebuild=False, hall_ID=None):
        """
        Init Hall with details from HMC
        """

        # The rebuild flag, if true, denotes that the object is being made from
        # data already present in the database
        # If False, a new data row is added to the specific table
        if not rebuild:
            self.hall_ID = db.add("hall")
        else:
            self.hall_ID = hall_ID

        self.name = name
        self.status = status
        self.single_room_count = single_room_count
        self.double_room_count = double_room_count
        self.single_room_occupancy = 0
        self.double_room_occupancy = 0
        self.single_room_rent = single_room_rent
        self.double_room_rent = double_room_rent
        self.warden_ID = warden_ID
        self.mess_manager_ID = mess_manager_ID
        self.clerk_ID = clerk_ID
        self.amenities_charge = amenities_charge

        # Initialize accounts with 0.
        self.mess_account = 0.
        self.amenities_account = 0.
        self.repair_account = 0.
        self.salary_account = 0.
        self.rent_account = 0.
        self.others_account = 0.

    # name getter and setter functions
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name
        db.update("hall", self.hall_ID, "name", self.name)

    # hall_ID getter and setter functions
    @property
    def hall_ID(self):
        return self._hall_ID

    @hall_ID.setter
    def hall_ID(self, hall_ID):
        self._hall_ID = hall_ID

    # warden_ID getter and setter functions
    @property
    def warden_ID(self):
        return self._warden_ID

    @warden_ID.setter
    def warden_ID(self, warden_ID):
        self._warden_ID = warden_ID
        db.update("hall", self.hall_ID, "warden_ID", self.warden_ID)

    # clerk_ID getter and setter functions
    @property
    def clerk_ID(self):
        return self._clerk_ID

    @clerk_ID.setter
    def clerk_ID(self, clerk_ID):
        self._clerk_ID = clerk_ID
        db.update("hall", self.hall_ID, "clerk_ID", self.clerk_ID)

    # mess_manager_ID getter and setter functions
    @property
    def mess_manager_ID(self):
        return self._mess_manager_ID

    @mess_manager_ID.setter
    def mess_manager_ID(self, mess_manager_ID):
        self._mess_manager_ID = mess_manager_ID
        db.update("hall", self.hall_ID, "mess_manager_ID", self.mess_manager_ID)

    # status getter and setter functions
    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        self._status = status
        db.update("hall", self.hall_ID, "status", self.status)

    # single_room_count getter and setter functions
    @property
    def single_room_count(self):
        return self._single_room_count

    @single_room_count.setter
    def single_room_count(self, single_room_count):
        self._single_room_count = single_room_count
        db.update("hall", self.hall_ID, "single_room_count", self.single_room_count)

    # double_room_count getter and setter functions
    @property
    def double_room_count(self):
        return self._double_room_count

    @double_room_count.setter
    def double_room_count(self, double_room_count):
        self._double_room_count = double_room_count
        db.update("hall", self.hall_ID, "double_room_count", self.double_room_count)

    # single_room_occupancy getter and setter functions
    @property
    def single_room_occupancy(self):
        return self._single_room_occupancy

    @single_room_occupancy.setter
    def single_room_occupancy(self, single_room_occupancy):
        self._single_room_occupancy = single_room_occupancy
        db.update("hall", self.hall_ID, "single_room_occupancy", self.single_room_occupancy)

    # double_room_occupancy getter and setter functions
    @property
    def double_room_occupancy(self):
        return self._double_room_occupancy

    @double_room_occupancy.setter
    def double_room_occupancy(self, double_room_occupancy):
        self._double_room_occupancy = double_room_occupancy
        db.update("hall", self.hall_ID, "double_room_occupancy", self.double_room_occupancy)

    # single_room_rent getter and setter functions
    @property
    def single_room_rent(self):
        return self._single_room_rent

    @single_room_rent.setter
    def single_room_rent(self, single_room_rent):
        self._single_room_rent = single_room_rent
        db.update("hall", self.hall_ID, "single_room_rent", self.single_room_rent)

    # double_room_rent getter and setter functions
    @property
    def double_room_rent(self):
        return self._double_room_rent

    @double_room_rent.setter
    def double_room_rent(self, double_room_rent):
        self._double_room_rent = double_room_rent
        db.update("hall", self.hall_ID, "double_room_rent", self.double_room_rent)

    # amenities_charge getter and setter functions
    @property
    def amenities_charge(self):
        return self._amenities_charge

    @amenities_charge.setter
    def amenities_charge(self, amenities_charge):
        self._amenities_charge = amenities_charge
        db.update("hall", self.hall_ID, "amenities_charge", self.amenities_charge)

    # mess_account getter and setter functions
    @property
    def mess_account(self):
        return self._mess_account

    @mess_account.setter
    def mess_account(self, mess_account):
        self._mess_account = mess_account
        db.update("hall", self.hall_ID, "mess_account", self.mess_account)

    # amenities_account getter and setter functions
    @property
    def amenities_account(self):
        return self._amenities_account

    @amenities_account.setter
    def amenities_account(self, amenities_account):
        self._amenities_account = amenities_account
        db.update("hall", self.hall_ID, "amenities_account", self.amenities_account)

    # repair_account getter and setter functions
    @property
    def repair_account(self):
        return self._repair_account

    @repair_account.setter
    def repair_account(self, repair_account):
        self._repair_account = repair_account
        db.update("hall", self.hall_ID, "repair_account", self.repair_account)

    # salary_account getter and setter functions
    @property
    def salary_account(self):
        return self._salary_account

    @salary_account.setter
    def salary_account(self, salary_account):
        self._salary_account = salary_account
        db.update("hall", self.hall_ID, "salary_account", self.salary_account)

    # others_account getter and setter functions
    @property
    def others_account(self):
        return self._others_account

    @others_account.setter
    def others_account(self, others_account):
        self._others_account = others_account
        db.update("hall", self.hall_ID, "others_account", self.others_account)

    # rent_account getter and setter functions
    @property
    def rent_account(self):
        return self._rent_account

    @rent_account.setter
    def rent_account(self, rent_account):
        self._rent_account = rent_account
        db.update("hall", self.hall_ID, "rent_account", self.rent_account)
