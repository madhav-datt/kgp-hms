
import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtCore, QtGui
import Student_Main_Window
from Complaint_GUI import ComplaintWindowClass
from ..database import login
from ..database import db_rebuild as dbr

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

student_ID = 0
curr_complaint_ID = 0

class StudentMainWindowClass(QtGui.QWidget, Student_Main_Window.Ui_Form):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)

        self.label.setPixmap(QtGui.QPixmap(_fromUtf8('bkd1edit2.jpg')))
        self.label.setScaledContents(True)

        self.label_10.setPixmap(QtGui.QPixmap(_fromUtf8('bkd1edit2.jpg')))
        self.label_10.setScaledContents(True)

        self.label_31.setPixmap(QtGui.QPixmap(_fromUtf8('bkd1edit2.jpg')))
        self.label_31.setScaledContents(True)

        #self.pushButton_3.clicked.connect(self.show_complaint_window)
        self.pushButton_4.clicked.connect(self.display_dues_frame)
        self.pushButton_7.clicked.connect(self.display_student_main_win)
        self.pushButton_5.clicked.connect(self.display_pwchange_frame)
        self.pushButton_9.clicked.connect(self.display_student_main_win)
        self.pushButton_3.clicked.connect(self.display_complaint_frame)
        self.buttonBox.rejected.connect(self.display_student_main_win)
        self.pushButton_10.clicked.connect(self.password_validate)

    def password_validate(self):
        id = self.lineEdit_19.text()
        pwd = self.lineEdit_20.text()
        if login.authenticate("student", id, pwd):
            student_ID = id
            self.display(0)
        else:
            self.label_36.setText("Wrong ID or Password. Please try again.")

    def display_complaint_frame(self):
        self.display(3)

    def display_pwchange_frame(self):
        self.display(2)
        self.resize(581, 344)

    def display_student_main_win(self):
        self.resize(581, 544)
        self.display(0)

    def show_complaint_window(self):
        self.window = ComplaintWindowClass()
        self.window.show()

    def display_dues_frame(self):
        #self.resize(400, 490)
        self.display(1)


    def display(self, i):
        self.stackedWidget.setCurrentIndex(i)
        student_dict = dbr.rebuild("student")
        if i == 0:
            self.label_2.setText("WELCOME " + student_dict[student_ID].name)
            self.lineEdit.setText(student_dict[student_ID].name)
            self.lineEdit_2.setText(student_dict[student_ID].address)
            self.lineEdit_3.setText(student_dict[student_ID].contact_number)
            hall_name = find_hall_ID_by_name(student_dict[student_ID].hall_ID)
            self.lineEdit_4.setText(hall_name)
            self.lineEdit_5.setText(student_dict[student_ID].room_no)
            self.lineEdit_6.setText(student_dict[student_ID].room_type)
            self.lineEdit_7.setText(student_ID)

    def set_list(self):
        self.listWidget.clear()
        complaint_ids = []
        complaint_dict = dbr.rebuild("comaplaint")
        for key in complaint_dict:
            if complaint_dict[key].student_ID == student_ID:
                complaint_ids.append(complaint_dict[key].complaint_ID)
        self.listWidget.addItems(complaint_ids)

    def view_complaint(self):
        if self.listWidget.currentItem() is None:
            return
        else:
            curr_complaint_ID = int(self.listWidget.currentItem().text())
            self.display_complaint_frame()

def find_hall_ID_by_name(self, name):
    hall_dict = dbr.rebuild("hall")
    for key in hall_dict:
        if hall_dict[key].name == name:
            return key
    return -1
'''
app = QApplication(sys.argv)
form = StudentMainWindowClass()
form.show()
app.exec_()
'''