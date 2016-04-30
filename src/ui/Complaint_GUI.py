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

from PyQt4 import QtCore, QtGui
import Complaint

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s


class ComplaintWindowClass(QtGui.QWidget, Complaint.Ui_complaintWindow):
    """Complaint Window Interface

    Part of Integrated Student Interface
    """

    def __init__(self):
        """
        Init Complaint functionalities
        """

        QtGui.QWidget.__init__(self)
        self.setupUi(self)


'''
app = QApplication(sys.argv)
form = ComplaintWindowClass()
form.show()
app.exec_()
'''
