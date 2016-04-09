import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtCore, QtGui
import HMC_Window
from ..actors import student, warden
from ..workers import clerk, mess_manager
from ..requests import grant_request
from ..database import db_rebuild as dbr
from ..halls import hall
from ..database import input_validation
from ..database import login

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s


class HMCWindowClass(QtGui.QWidget, HMC_Window.Ui_Form):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)

        self.label_32.setPixmap(QtGui.QPixmap(_fromUtf8('bkd1edit2.jpg')))
        self.label_32.setScaledContents(True)
        self.label_33.setPixmap(QtGui.QPixmap(_fromUtf8('iit.jpg')))
        self.label_33.setScaledContents(True)
        self.pushButton_8.clicked.connect(self.password_validate)
        '''
        Custom UI starting, based on data available in the databases
        '''
        hmc_dict = dbr.rebuild("hmc")
        for key in hmc_dict:
            if hmc_dict[key].payment_is_active:
                self.pushButton_5.setEnabled(False)
            else:
                self.pushButton_5.setEnabled(True)

        '''
        Linking "Issue Admission Letter Button to its functionality
        '''
        self.pushButton_4.clicked.connect(self.issue_admission_letter)

    def display(self, i):
        self.stackedWidget.setCurrentIndex(i)

    def password_validate(self):
        password_entered = self.lineEdit_5.text()
        if login.authenticate("hmc", 0, password_entered):
            self.display(0)
        else:
            self.label_28.setText("Wrong Password. PLease try again")

    '''
    Adding specific ui elements for student functionality tab
    '''
    def issue_admission_letter(self):
        name = self.lineEdit_16.text()
        gender = self.comboBox.currentText()
        contact = self.lineEdit_15.text()
        address = self.lineEdit_18.text()
        student_hall = self.comboBox_2.currentText()
        student_hall_ID = 1
        room_no = self.lineEdit_13.text()
        if self.comboBox_2.currentText() == "Single":
            room_type = 'S'
        else:
            room_type = 'D'
        password = self.lineEdit_12.text()
        new_student = student.Student(password, name, address, contact, student_hall_ID, room_no, room_type)

    def activate_payment_link(self):
        hmc_obj = dbr.rebuild("hmc")
        hmc_obj.activate_payment_link()

    def deactivate_payment_link(self):
        hmc_obj = dbr.rebuild("hmc")
        hmc_obj.deactivate_payment_link()

    '''
    Adding specific ui elements for add hall tab
    '''
    def add_hall(self):
        name = self.lineEdit_4.text()
        status = self.comboBox_4.currentText()
        amenities_charge = self.doubleSpinBox_5.text()
        single_room_count = self.spinBox_8.text()
        single_room_rent = self.doubleSpinBox.text()
        double_room_count = self.spinBox_9.text()
        double_room_rent = self.doubleSpinBox_2.text()
        warden_name = self.lineEdit_8.text()
        warden_pw = self.lineEdit_9.text()
        manager_name = self.lineEdit_10.text()
        manager_pw = self.lineEdit_11.text()
        manager_salary = self.doubleSpinBox_3.text()
        clerk_name = self.lineEdit_14.text()
        clerk_pw = self.lineEdit_17.text()
        clerk_salary = self.doubleSpinBox_4.text()
        new_warden = warden.Warden(warden_pw, warden_name, "warden_kgp@gmail.com",
                                   0)
        new_mess_manager = mess_manager.MessManager(manager_name, 0, manager_pw, manager_salary)
        new_clerk = clerk.Clerk(clerk_name, 0, clerk_pw, clerk_salary)
        new_hall = hall.Hall(name, status, single_room_count, double_room_count,
                             single_room_rent, double_room_rent, new_warden.warden_ID, new_mess_manager.mess_manager_ID,
                             new_clerk.worker_ID, amenities_charge)
        new_warden.hall_ID = new_hall.hall_ID
        new_mess_manager.hall_ID = new_hall.hall_ID
        new_clerk.hall_ID = new_hall.hall_ID

    '''
    Adding custom ui for grant request tab
    '''

    def set_list(self):
        """
        Setting up the listWidget, showing hall names with a pending grant request
        """
        hall_dict = dbr.rebuild("hall")
        grant_req_dict = dbr.rebuild("grant_request")
        self.listWidget.clear()
        hall_names = [grant_req_dict[req].name for req in grant_req_dict]
        self.listWidget.addItems(hall_names)

    def get_warden_req(self):
        """
        To be invoked upon pushing "View Request" button
        """
        grant_req_dict = dbr.rebuild("grant_request")
        if self.listWidget.currentItem() is None:
            return
        else:
            hall_name = self.listWidget.currentItem().text()
            hall_ID = find_hall_ID_by_name(hall_name)
            self.label_23.setText(hall_name)
            for req in grant_req_dict:
                if grant_req_dict[req].hall_ID == hall_ID:
                    self.lineEdit.setText(grant_req_dict[req].salary_charge())
                    self.doubleSpinBox_6.setValue(input_validation.float_input(self.lineEdit.text()))
                    self.lineEdit_3.setText(grant_req_dict[req].repair_charge())
                    self.doubleSpinBox_7.setValue(input_validation.float_input(self.lineEdit_3.text()))
                    self.lineEdit_4.setText(grant_req_dict[req].other_charge())
                    self.doubleSpinBox_8.setValue(input_validation.float_input(self.lineEdit_4.text()))

    '''
    To be invoked on  pushing the issue grant button
    '''
    def issue_grant(self):
        if self.label_23.text() == "":
            return
        grant_req_dict = dbr.rebuild("grant_request")
        hall_name = self.label_23.text()
        hall_ID = find_hall_ID_by_name(hall_name)
        for req in grant_req_dict:
            if grant_req_dict[req].hall_ID == hall_ID:
                grant_req_dict[req].approve(self.doubleSpinBox_6.value(), self.doubleSpinBox_8.value(),
                                            self.doubleSpinBox_7.value())  # TODO : check if value works and change .text() above
                self.set_list()
                self.label_23.setText("")

    def reject_grant(self):
        if self.label_23.text() == "":
            return
        grant_req_dict = dbr.rebuild("grant_request")
        hall_name = self.label_23.text()
        hall_ID = find_hall_ID_by_name(hall_name)
        for req in grant_req_dict:
            if grant_req_dict[req].hall_ID == hall_ID:
                grant_req_dict[req].reject()
                self.set_list()
                self.label_23.setText("")

def find_hall_ID_by_name(self, name):
    hall_dict = dbr.rebuild("hall")
    for key in hall_dict:
        if hall_dict[key].name == name:
            return key
    return -1


app = QApplication(sys.argv)
form = HMCWindowClass()
form.show()
app.exec_()