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
        self.label_7.setPixmap(QtGui.QPixmap(_fromUtf8('src/ui/bkd1edit2.jpg')))
        self.label_7.setScaledContents(True)

        self.label_12.setPixmap(QtGui.QPixmap(_fromUtf8('src/ui/bkd1edit2.jpg')))
        self.label_12.setScaledContents(True)
        self.pushButton_2.clicked.connect(self.password_validate)
        self.pushButton.clicked.connect(self.add_mess_charge)

    def add_mess_charge(self):
        """
        Add mess charge to Student's total amount due
        """

        student_list = dbr.rebuild("worker")

        student_sel_ID = self.tableWidget.selectedItems()[0][0]
        for key in student_list:
            if student_sel_ID == student_list[key].student_ID:
                amount = self.doubleSpinBox.value()
                student_list[key].mess_charge += amount
                db.update("hall", student_list[key].hall_ID, "mess_account",
                          float(db.get("hall", student_list[key].hall_ID, "mess_account")) - amount)

    def password_validate(self):
        """
        Check password for login
        """

        user_ID = self.lineEdit_4.text()
        password = self.lineEdit_5.text()
        if login.authenticate("clerk", user_ID, password):
            mess_manager_ID = user_ID

            # Set text fields with value from databases
            self.lineEdit.setText(str(mess_manager_ID))
            self.lineEdit_2.setText(str(db.get("worker", mess_manager_ID, "name")))
            self.label_2.setText("Welcome " + str(db.get("worker", mess_manager_ID, "name")))
            self.lineEdit_3.setText(str(db.get("worker", mess_manager_ID, "hall_ID")))

            # Build table from student database
            student_list = dbr.rebuild("student")
            i = 0
            for key in student_list:
                if student_list[key].hall_ID == db.get("worker", mess_manager_ID, "hall_ID"):
                    item = self.tableWidget.verticalHeaderItem(i)
                    item.setText("0")
                    item = self.tableWidget.item(i, 0)
                    item.setText(str(student_list[key].student_ID))
                    item = self.tableWidget.item(i, 1)
                    item.setText(student_list[key].name)
                    i += 1

            self.display(0)
        else:
            self.label_11.setText("Authentication Failed. Please try again")

app = QApplication(sys.argv)
form = MessManagerWindowClass()
form.show()
app.exec_()