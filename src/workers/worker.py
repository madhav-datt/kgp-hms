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

class Worker(object):
    """Contains details of Worker Instance

    Attributes:
        worker_ID: Integer to uniquely identify worker
        name: String
        hall_ID: Integer to uniquely identify hall
    """

    def __init__(self, name, hall_ID, rebuild = false, worker_ID = None):
        """
        Init Worker with details as recruited by HMC or Warden
        """
        self.name = name
        self.hall_ID = hall_ID
        self.worker_ID = None

    
