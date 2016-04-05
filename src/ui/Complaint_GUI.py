import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtCore, QtGui
import Complaint
import Student_Main_Window

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s


class ComplaintWindowClass(QtGui.QWidget, Complaint.Ui_complaintWindow):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)


'''
app = QApplication(sys.argv)
form = ComplaintWindowClass()
form.show()
app.exec_()
'''
