import sys
from PyQt4.QtGui import *
from ..database import db_func as db
from ..database import db_rebuild as dbr
from ..database import login
from ..requests import grant_request
from ..actors import warden
from ..workers import attendant
from PyQt4 import QtCore, QtGui
import warden_window

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s


# Build Warden Object
global this_warden


class WardenWindowClass(QtGui.QWidget, warden_window.Ui_Form):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
        self.label.setPixmap(QtGui.QPixmap(_fromUtf8('src/ui/bkd1edit2.jpg')))
        self.label.setScaledContents(True)

        self.label_2.setPixmap(QtGui.QPixmap(_fromUtf8('src/ui/bkd1edit2.jpg')))
        self.label_2.setScaledContents(True)

        self.label_3.setPixmap(QtGui.QPixmap(_fromUtf8('src/ui/bkd1edit2.jpg')))
        self.label_3.setScaledContents(True)

        self.label_5.setPixmap(QtGui.QPixmap(_fromUtf8('src/ui/bkd1edit2.jpg')))
        self.label_5.setScaledContents(True)

        self.label_6.setPixmap(QtGui.QPixmap(_fromUtf8('src/ui/bkd1edit2.jpg')))
        self.label_6.setScaledContents(True)

        self.label_7.setPixmap(QtGui.QPixmap(_fromUtf8('src/ui/bkd1edit2.jpg')))
        self.label_7.setScaledContents(True)

        self.label_32.setPixmap(QtGui.QPixmap(_fromUtf8('src/ui/bkd1edit2.jpg')))
        self.label_32.setScaledContents(True)

        self.pushButton_10.clicked.connect(self.password_validate)

        self.pushButton.clicked.connect(self.submit_grant_request)

        self.pushButton_3.clicked.connect(self.hire_new_worker)

        self.pushButton_4.clicked.connect(self.print_account_statement)

    def print_account_statement(self):
        pass
        #TODO : link to printing of account statements

    def check_grant_button(self):
        """
        Check if grant request from hall is pending in database
        Disable button if pending
        """

        grant_table = dbr.rebuild("grant_request")

        for key in grant_table:
            if grant_table[key].hall_ID == this_warden.hall_ID:
                self.pushButton.setEnabled(False)

    def submit_grant_request(self):
        """
        Submit grant request for HMC approval
        """

        other_charge = self.doubleSpinBox_2.value()
        repair_charge = self.doubleSpinBox_3.value()

        if other_charge == 0. or repair_charge == 0.:
            choice = QtGui.QMessageBox.question(self, 'Error', "No Field can be left blank")
        else:
            grant_request.GrantRequest(this_warden.hall_ID, this_warden.salary_charge(dbr.rebuild("worker")),
                                       repair_charge, other_charge)
            self.check_grant_button()

    def password_validate(self):
        """
        Check password for login
        """
        global this_warden

        user_ID = int(self.lineEdit_19.text())
        password = self.lineEdit_20.text()

        if login.authenticate("warden", user_ID, password):
            this_warden = warden.Warden(password, db.get("warden", user_ID, "name")[0],
                                        db.get("warden", user_ID, "email")[0],
                                        db.get("warden", user_ID, "hall_ID")[0],
                                        db.get("warden", user_ID, "controlling_warden")[0],
                                        True, user_ID)
            hall_ID = this_warden.hall_ID

            # View Room Occupancy Tab - add labels and values from database
            self.lineEdit_8.setText(db.get("hall", hall_ID, "single_room_count")[0])
            self.lineEdit_9.setText(db.get("hall", hall_ID, "single_room_occupancy")[0])
            self.lineEdit_8.setText(str(int(self.lineEdit_8.text()) - int(self.lineEdit_9.text())))

            self.lineEdit_17.setText(db.get("hall", hall_ID, "double_room_count")[0])
            self.lineEdit_18.setText(db.get("hall", hall_ID, "double_room_occupancy")[0])
            self.lineEdit_21.setText(str(int(self.lineEdit_17.text()) - int(self.lineEdit_18.text())))

            # Grant Request Tab - add labels and values from database
            self.lineEdit.setText(str(this_warden.salary_charge(dbr.rebuild("worker"))))
            self.check_grant_button()

            # View Overall Occupancy Tab - add conditions
            if not this_warden.controlling_warden:
                self.label_4.setVisible(True)
                self.groupBox_7.setVisible(False)
                self.groupBox_8.setVisible(False)
            else:
                self.label_4.setVisible(False)
                self.groupBox_7.setVisible(True)
                self.groupBox_8.setVisible(True)
                #TODO : set data for occupancies
                # self.label_24.setText(str())
                # self.label_25.setText(str())
                # self.label_26.setText(str(int(self.label_24.text()) - int(self.label_25.text())))
                # self.label_27.setText(str())
                # self.label_28.setText(str())
                # self.label_29.setText(str(int(self.label_24.text()) - int(self.label_25.text())))

        else:
            self.label_42.setText("Authentication Failed. Please try again")

    def hire_new_worker(self):
        global this_warden
        hall_ID = this_warden.hall_ID
        worker_name = self.lineEdit_22.text()
        worker_wage = self.doubleSpinBox.value()
        attendant.Attendant(worker_name, hall_ID, worker_wage, 0)
        self.lineEdit_22.setText("")
        self.doubleSpinBox.setValue(0.00)



app = QApplication(sys.argv)
form = WardenWindowClass()
form.show()
app.exec_()
