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
from PyQt4 import QtCore, QtGui
from ..database import db_func as db
from ..database import db_rebuild as dbr
from ..database import login
from ..workers import attendant
import Clerk_Window
import time

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s


class ClerkWindowClass(QtGui.QWidget, Clerk_Window.Ui_Form):
    """
    Clerk Window Class
    Contain GUI and Functionality
    """

    def __init__(self):
        """
        Init Clerk Window GUI
        Create and launch instance
        """

        QtGui.QWidget.__init__(self)
        self.setupUi(self)
        self.bkdLabel.setPixmap(QtGui.QPixmap(_fromUtf8('src/ui/bkd1edit2.jpg')))
        self.bkdLabel.setScaledContents(True)
        self.bkdLabel_2.setPixmap(QtGui.QPixmap(_fromUtf8('src/ui/bkd1edit2.jpg')))
        self.bkdLabel_2.setScaledContents(True)
        self.label_8.setText("Today's Date : " + time.strftime("%x"))
        self.pushButton_2.clicked.connect(self.password_validate)

        # Deactivate attendance button if last attendance recorded is on same day
        if db.get_attend_date() == time.strftime('%Y-%m-%d'):
            self.pushButton.setEnabled(False)

        self.pushButton.clicked.connect(self.give_attendance)

    def give_attendance(self):
        """
        Mark attendance for present date for all selected workers
        Can be called only once in a day
        """

        worker_list = dbr.rebuild("worker")
        rows = sorted(set(index.row() for index in self.tableWidget.selectedIndexes()))

        for row in rows:
            worker_sel_ID = self.tableWidget.item(row, 0).text()
            worker_list[int(worker_sel_ID)].monthly_attendance += 1

        self.pushButton.setEnabled(False)
        db.update_attend_date()
        choice = QtGui.QMessageBox.information(self, 'Success', "Attendance for today submitted")

    def password_validate(self):
        """
        Check password for login
        """
        user_ID = int(self.lineEdit_4.text())
        password = self.lineEdit_5.text()
        if login.authenticate("clerk", user_ID, password):
            clerk_ID = user_ID

            # Set text fields with value from databases
            self.lineEdit.setText(str(clerk_ID))
            self.lineEdit_2.setText(str(db.get("worker", clerk_ID, "name")[0]))
            self.label_2.setText("Welcome " + db.get("worker", clerk_ID, "name")[0])
            self.lineEdit_3.setText(str(db.get("worker", clerk_ID, "hall_ID")[0]))

            # Build table from worker database
            worker_list = dbr.rebuild("worker")
            i = 0
            for key in worker_list:
                if isinstance(worker_list[key], attendant.Attendant) and \
                                worker_list[key].hall_ID == db.get("worker", clerk_ID, "hall_ID")[0]:
                    rowPosition = self.tableWidget.rowCount()
                    self.tableWidget.insertRow(rowPosition)
                    self.tableWidget.setItem(rowPosition, 0, QtGui.QTableWidgetItem(str(worker_list[key].worker_ID)))
                    self.tableWidget.setItem(rowPosition, 1, QtGui.QTableWidgetItem(worker_list[key].name))

            self.stackedWidget.setCurrentIndex(0)
        else:
            self.label.setText("Authentication Failed. Please try again")


app = QtGui.QApplication(sys.argv)
Form = ClerkWindowClass()
Form.show()
app.exec_()
