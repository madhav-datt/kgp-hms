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
from PyQt4 import QtCore, QtGui
import HMC_Window
from ..actors import student, warden
from ..workers import clerk, mess_manager
from ..database import db_rebuild as dbr
from ..halls import hall
from ..database import input_validation
from ..database import login
from ..requests import printer

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s


class HMCWindowClass(QtGui.QWidget, HMC_Window.Ui_Form):
    """Clerk Window GUI and Functionality

    Opens with login screen
    """

    def __init__(self):
        """
        Init HMC GUI Window
        """

        QtGui.QWidget.__init__(self)
        self.setupUi(self)

        self.label_32.setPixmap(QtGui.QPixmap(_fromUtf8('src/ui/resources/bkd1edit2.jpg')))
        self.label_32.setScaledContents(True)
        self.label_33.setPixmap(QtGui.QPixmap(_fromUtf8('src/ui/resources/iit.jpg')))
        self.label_33.setScaledContents(True)
        self.pushButton_8.clicked.connect(self.password_validate)
        self.pushButton_2.clicked.connect(self.cancel)
        self.pushButton.clicked.connect(self.add_hall)
        self.pushButton_5.clicked.connect(self.activate_payment_link)
        self.pushButton_6.clicked.connect(self.deactivate_payment_link)
        self.pushButton_7.clicked.connect(self.issue_grant)
        self.pushButton_9.clicked.connect(self.reject_grant)
        self.pushButton_3.clicked.connect(self.get_warden_req)

        # Start Custom UI based on data available in the databases
        hmc_dict = dbr.rebuild("hmc")
        for key in hmc_dict:
            if hmc_dict[key].payment_is_active:
                self.pushButton_5.setEnabled(False)
                self.pushButton_6.setEnabled(True)
            else:
                self.pushButton_5.setEnabled(True)
                self.pushButton_6.setEnabled(False)

        # Linking "Issue Admission Letter Button to its functionality
        self.pushButton_4.clicked.connect(self.issue_admission_letter)

    def cancel(self):
        """
        Cancel hall setup
        Clear all text fields
        """

        self.set_hall_options()
        self.lineEdit_4.setText("")
        self.doubleSpinBox_5.setValue(0.0)
        self.spinBox_8.setValue(0.0)
        self.doubleSpinBox.setValue(0.00)
        self.spinBox_9.setValue(0.0)
        self.doubleSpinBox_2.setValue(0.00)
        self.lineEdit_8.setText("")
        self.lineEdit_9.setText("")
        self.lineEdit_10.setText("")
        self.lineEdit_11.setText("")
        self.doubleSpinBox_3.setValue(0.00)
        self.lineEdit_14.setText("")
        self.lineEdit_17.setText("")
        self.doubleSpinBox_4.setValue(0.00)

    def display_home(self):
        """
        Display Home Screen from stacked deck
        """

        self.display(0)

    def display(self, i):
        """
        Display i th screen from stacked deck
        Args: i = Number of screen to be displayed
        """

        self.stackedWidget.setCurrentIndex(i)

    def password_validate(self):
        """
        Validate password and login
        """

        password_entered = self.lineEdit_5.text()
        if login.authenticate("hmc", 0, password_entered):
            self.display(0)
            self.set_list()
            self.set_hall_options()
            hmc_dict = dbr.rebuild("hmc")
            for key in hmc_dict:
                if hmc_dict[key].payment_is_active == 'T':
                    self.pushButton_5.setEnabled(False)
                    self.pushButton_6.setEnabled(True)
                else:
                    self.pushButton_6.setEnabled(False)
                    self.pushButton_5.setEnabled(True)
        else:
            self.label_28.setText("Wrong Password. Please try again")

    def set_hall_options(self):
        """
        Build hall drop-down list with hall names
        """

        hall_dict = dbr.rebuild("hall")
        hall_names = []
        for key in hall_dict:
            hall_names.append(hall_dict[key].name)
        self.comboBox_3.clear()
        self.comboBox_3.addItems(hall_names)

    def issue_admission_letter(self):
        """
        Add new student, allot hall
        Print admission letter in PDF
        """

        name = self.lineEdit_16.text()
        gender = self.comboBox.currentText()
        contact = self.lineEdit_15.text()
        address = self.lineEdit_18.text()
        student_hall = str(self.comboBox_3.currentText())
        student_hall_ID = find_hall_ID_by_name(student_hall)
        room_no = self.lineEdit_13.text()

        if self.comboBox_2.currentText() == "Single":
            room_type = 'S'
        else:
            room_type = 'D'

        password = str(self.lineEdit_12.text())

        if name == "" or address == "" or contact == "" or room_no == "" or room_type == "":
            choice = QtGui.QMessageBox.question(self, 'Error', "No Field can be left blank")
        elif not input_validation.valid_phone(contact):
            choice = QtGui.QMessageBox.question(self, 'Error', "Invalid contact number")
        else:
            new_student = student.Student(password, name, address, contact, student_hall_ID, room_no, room_type, 0)
            choice = QtGui.QMessageBox.information(self, 'Success', "Student Letter successfully issued.")
            printer.issue_student_admission_letter(new_student, str(self.plainTextEdit.toPlainText()))
            self.lineEdit_16.setText("")
            self.lineEdit_15.setText("")
            self.lineEdit_18.setText("")
            self.lineEdit_13.setText("")
            self.lineEdit_12.setText("")
            self.plainTextEdit.setPlainText("")

    def activate_payment_link(self):
        """
        Activate payment link in student interfaces
        """

        hmc_obj = dbr.rebuild("hmc")
        for key in hmc_obj:
            hmc_obj[key].activate_payment_link()
        self.pushButton_6.setEnabled(True)
        self.pushButton_5.setEnabled(False)

    def deactivate_payment_link(self):
        """
        Deactivate payment link in student interfaces
        """

        hmc_obj = dbr.rebuild("hmc")
        for key in hmc_obj:
            hmc_obj[key].deactivate_payment_link()
        self.pushButton_6.setEnabled(False)
        self.pushButton_5.setEnabled(True)

    def add_hall(self):
        """
        Add ui elements for add hall tab
        Create new hall
        Assign warden, mess manager and hall office clerk
        """

        name = self.lineEdit_2.text()
        status = self.comboBox_4.currentText()
        amenities_charge = self.doubleSpinBox_5.value()
        single_room_count = self.spinBox_8.value()
        single_room_rent = self.doubleSpinBox.value()
        double_room_count = self.spinBox_9.value()
        double_room_rent = self.doubleSpinBox_2.value()
        warden_name = self.lineEdit_8.text()
        warden_pw = str(self.lineEdit_9.text())

        # No previous controlling warden is previously existing
        is_control_warden = self.checkBox.isChecked()
        warden_dict = dbr.rebuild("warden")
        for key in warden_dict:
            if warden_dict[key].controlling_warden == "True":
                is_control_warden = False
                break

        manager_name = self.lineEdit_10.text()
        manager_pw = str(self.lineEdit_11.text())
        manager_salary = self.doubleSpinBox_3.value()
        clerk_name = self.lineEdit_14.text()
        clerk_pw = str(self.lineEdit_17.text())
        clerk_salary = self.doubleSpinBox_4.value()

        # Validate hall creation inputs
        if name == "" or amenities_charge == 0. or single_room_count == 0 or single_room_rent == 0 \
                or double_room_count == 0 or double_room_rent == 0 or warden_name == "" or warden_pw == "" or \
                manager_name == "" or manager_pw == "" or manager_salary == 0. or clerk_name == "" or clerk_pw == "" \
                or clerk_salary == 0.:
            choice = QtGui.QMessageBox.question(self, 'Error', "No Field can be left blank")
        else:
            new_warden = warden.Warden(warden_pw, warden_name, "warden_kgp@gmail.com", 0, is_control_warden)
            new_mess_manager = mess_manager.MessManager(manager_name, 0, manager_pw, manager_salary)
            new_clerk = clerk.Clerk(clerk_name, 0, clerk_pw, clerk_salary)
            new_hall = hall.Hall(name, status, single_room_count, double_room_count,
                                 single_room_rent, double_room_rent, new_warden.warden_ID, new_mess_manager.worker_ID,
                                 new_clerk.worker_ID, amenities_charge)
            new_warden.hall_ID = new_hall.hall_ID
            new_mess_manager.hall_ID = new_hall.hall_ID
            new_clerk.hall_ID = new_hall.hall_ID
            choice = QtGui.QMessageBox.information(self, 'Success', "Hall Successfully setup")

            # Reset labels to blanks and text fields to blank on success
            self.set_hall_options()
            self.lineEdit_4.setText("")
            self.doubleSpinBox_5.setValue(0.0)
            self.spinBox_8.setValue(0.0)
            self.doubleSpinBox.setValue(0.00)
            self.spinBox_9.setValue(0.0)
            self.doubleSpinBox_2.setValue(0.00)
            self.lineEdit_8.setText("")
            self.lineEdit_9.setText("")
            self.lineEdit_10.setText("")
            self.lineEdit_11.setText("")
            self.doubleSpinBox_3.setValue(0.00)
            self.lineEdit_14.setText("")
            self.lineEdit_17.setText("")
            self.doubleSpinBox_4.setValue(0.00)

    def set_list(self):
        """
        Add custom ui for grant request tab
        Set up listWidget
        Show hall names with a pending grant request
        """

        hall_dict = dbr.rebuild("hall")
        grant_req_dict = dbr.rebuild("grant_request")
        self.listWidget.clear()
        hall_IDS = [grant_req_dict[req].hall_ID for req in grant_req_dict]
        hall_names = [hall_dict[hall_ID].name for hall_ID in hall_IDS]
        self.listWidget.addItems(hall_names)
        self.label_23.setText("")

    def get_warden_req(self):
        """
        Invoked upon pushing "View Request" button
        Display selected grant request
        """

        grant_req_dict = dbr.rebuild("grant_request")
        if self.listWidget.currentItem() is None:
            choice = QtGui.QMessageBox.question(self, 'Error', "Please select a grant request!")
            return
        else:
            hall_name = self.listWidget.currentItem().text()
            hall_ID = find_hall_ID_by_name(hall_name)
            self.label_23.setText(hall_name)
            for req in grant_req_dict:
                if grant_req_dict[req].hall_ID == hall_ID:
                    self.lineEdit.setText(str(grant_req_dict[req].salary_charge))
                    self.doubleSpinBox_6.setValue(float(self.lineEdit.text()))
                    self.lineEdit_3.setText(str(grant_req_dict[req].repair_charge))
                    self.doubleSpinBox_7.setValue(float(self.lineEdit_3.text()))
                    self.lineEdit_4.setText(str(grant_req_dict[req].other_charge))
                    self.doubleSpinBox_8.setValue(float(self.lineEdit_4.text()))
                    break

    def reset_grant_request(self):
        """
        Clear grant request table
        """

        self.lineEdit.setText("")
        self.doubleSpinBox_6.setValue(0.00)
        self.lineEdit_3.setText("")
        self.doubleSpinBox_7.setValue(0.00)
        self.lineEdit_4.setText("")
        self.doubleSpinBox_8.setValue(0.00)
        self.set_list()
        self.label_23.setText("")

    def issue_grant(self):
        """
        Invoked on  pushing the issue grant button
        Change grant request status
        Add issued amounts to hall accounts
        """

        if self.label_23.text() == "":
            choice = QtGui.QMessageBox.question(self, 'Error', "Please select a grant request to approve!")
            return
        grant_req_dict = dbr.rebuild("grant_request")
        hall_name = self.label_23.text()
        hall_ID = find_hall_ID_by_name(hall_name)
        for req in grant_req_dict:
            if grant_req_dict[req].hall_ID == hall_ID:
                grant_req_dict[req].approve(self.doubleSpinBox_6.value(), self.doubleSpinBox_8.value(),
                                            self.doubleSpinBox_7.value(), dbr.rebuild("hall"))
        self.reset_grant_request()
        choice = QtGui.QMessageBox.information(self, 'Success', "Grant Issued")

    def reject_grant(self):
        """
        Reject grant request
        Remove from database
        """

        if self.label_23.text() == "":
            return
        grant_req_dict = dbr.rebuild("grant_request")
        hall_name = self.label_23.text()
        hall_ID = find_hall_ID_by_name(hall_name)
        for req in grant_req_dict:
            if grant_req_dict[req].hall_ID == hall_ID:
                grant_req_dict[req].reject()
                self.reset_grant_request()
                choice = QtGui.QMessageBox.information(self, 'Success', "Grant Rejected")


def find_hall_ID_by_name(name):
    """
    Return hall ID for passed hall name
    """

    hall_dict = dbr.rebuild("hall")
    for key in hall_dict:
        if hall_dict[key].name == name:
            return key
    return -1


app = QApplication(sys.argv)
form = HMCWindowClass()
form.show()
app.exec_()
