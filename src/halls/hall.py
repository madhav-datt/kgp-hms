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

class Hall(object):
    """Contains details of Hall

    Attributes:
        hall_ID: Integer to uniquely identify student
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

    def __init__(self, hall_ID, name, status, single_room_count,
                double_room_count, single_room_occupancy, double_room_occupancy,
                single_room_rent, double_room_rent, warden_ID, mess_manager_ID,
                clerk_ID, amenities_charge):
        """
        Init Hall with details from HMC
        """

        self.hall_ID = hall_ID
        self.name = name
        self.status = status
        self.single_room_count = single_room_count
        self.double_room_count = double_room_count
        self.single_room_occupancy = single_room_occupancy
        self.double_room_occupancy = double_room_occupancy
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

    
