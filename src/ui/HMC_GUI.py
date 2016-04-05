import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtCore, QtGui
#from database import password_validation as pv
import HMC_Window

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s


class HMCWindowClass(QtGui.QWidget, HMC_Window.Ui_Form):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
        '''
        Linking "Issue Admission Letter Button to its functionality
        '''
#        self.pushButton_4.clicked.connect(self.issue_admission_letter)
'''
    def issue_admission_letter(self):
        name = self.lineEdit_16.text()
        gender = self.comboBox.currentText()
        contact = self.lineEdit_15.text()
        address = self.lineEdit_18.text()
        student_hall = self.comboBox_2.currentText()
        student_hall_ID =
        room_no = self.lineEdit_13.text()
        if self.comboBox_3.currentText() == "Single":
            room_type = 'S'
        else:
            room_type = 'D'
        password = self.lineEdit_12.text()
        <file_name.py>.student_list.append(Student(password, name, address, contact, student_hall_ID, room_no, room_type))
'''
app = QApplication(sys.argv)
form = HMCWindowClass()
form.show()
app.exec_()