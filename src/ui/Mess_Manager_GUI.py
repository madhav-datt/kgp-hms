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

import sys
from PyQt4.QtGui import *
from ..database import db_func as db
from ..database import db_rebuild as dbr
from ..database import login
from PyQt4 import QtCore, QtGui
import Mess_Manager_Window

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s


class MessManagerWindowClass(QtGui.QWidget, Mess_Manager_Window.Ui_Form):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
        self.label_7.setPixmap(QtGui.QPixmap(_fromUtf8('src/ui/resources/bkd1edit2.jpg')))
        self.label_7.setScaledContents(True)

        self.label_12.setPixmap(QtGui.QPixmap(_fromUtf8('src/ui/resources/bkd1edit2.jpg')))
        self.label_12.setScaledContents(True)
        self.pushButton_2.clicked.connect(self.password_validate)
        self.pushButton.clicked.connect(self.add_mess_charge)

    def add_mess_charge(self):
        """
        Add mess charge to Student's total amount due
        """

        student_list = dbr.rebuild("student")
        student_sel_ID = 0
        if self.tableWidget.selectedItems():
            student_sel_ID = int(self.tableWidget.selectedItems()[0].text())

            for key in student_list:
                if student_sel_ID == student_list[key].student_ID:
                    amount = self.doubleSpinBox.value()
                    student_list[key].mess_charge += amount
                    db.update("hall", student_list[key].hall_ID, "mess_account",
                              float(db.get("hall", student_list[key].hall_ID, "mess_account")[0]) - amount)

            self.doubleSpinBox.setValue(0.0)
            choice = QtGui.QMessageBox.information(self, 'Success', "Mess Charge submitted")

        else:
            choice = QtGui.QMessageBox.critical(self, 'Error', "Please select student before submitting")

    def password_validate(self):
        """
        Check password for login
        """

        user_ID = int(self.lineEdit_4.text())
        password = self.lineEdit_5.text()
        if login.authenticate("mess_manager", user_ID, password):
            mess_manager_ID = user_ID

            # Set text fields with value from databases
            self.lineEdit.setText(str(mess_manager_ID))
            self.lineEdit_2.setText(str(db.get("worker", mess_manager_ID, "name")[0]))
            self.label_2.setText("Welcome " + db.get("worker", mess_manager_ID, "name")[0])
            self.lineEdit_3.setText(str(db.get("worker", mess_manager_ID, "hall_ID")[0]))

            # Build table from student database
            student_list = dbr.rebuild("student")
            for key in student_list:
                if student_list[key].hall_ID == db.get("worker", mess_manager_ID, "hall_ID")[0]:
                    rowPosition = self.tableWidget.rowCount()
                    self.tableWidget.insertRow(rowPosition)
                    self.tableWidget.setItem(rowPosition, 0, QtGui.QTableWidgetItem(str(student_list[key].student_ID)))
                    self.tableWidget.setItem(rowPosition, 1, QtGui.QTableWidgetItem(student_list[key].name))

            self.stackedWidget.setCurrentIndex(0)
        else:
            self.label_11.setText("Authentication Failed. Please try again")


app = QApplication(sys.argv)
form = MessManagerWindowClass()
form.show()
app.exec_()
