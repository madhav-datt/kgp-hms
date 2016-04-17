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
from ..requests import grant_request, printer
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

        self.label_9.setPixmap(QtGui.QPixmap(_fromUtf8('src/ui/bkd1edit2.jpg')))
        self.label_9.setScaledContents(True)

        self.label_32.setPixmap(QtGui.QPixmap(_fromUtf8('src/ui/bkd1edit2.jpg')))
        self.label_32.setScaledContents(True)

        self.pushButton_10.clicked.connect(self.password_validate)
        self.pushButton.clicked.connect(self.submit_grant_request)
        self.pushButton_2.clicked.connect(self.fire_worker)
        self.pushButton_3.clicked.connect(self.hire_new_worker)
        self.pushButton_4.clicked.connect(self.print_account_statement)
        self.pushButton_5.clicked.connect(self.pay_salaries)
        self.pushButton_6.clicked.connect(self.gen_salary_list)
        self.pushButton_7.clicked.connect(self.view_complaint_button)
        self.pushButton_8.clicked.connect(self.post_atr_button)

    def view_complaint_button(self):
        comp_dict = dbr.rebuild("complaint")
        if self.listWidget.currentItem() is None:
            choice = QtGui.QMessageBox.question(self, 'Error', "Please select a complaint first!")
            return

        comp_id = int(self.listWidget.currentItem().text())
        comp_obj = comp_dict[comp_id]
        self.lineEdit_15.setText(str(comp_obj.complaint_ID))
        self.lineEdit_23.setText(str(comp_obj.student_ID))
        self.plainTextEdit_2.setPlainText(str(comp_obj.description))
        self.plainTextEdit.setPlainText("")

    def post_atr_button(self):
        comp_dict = dbr.rebuild("complaint")
        atr = self.plainTextEdit.toPlainText()

        if self.lineEdit_15.text() == "":
            choice = QtGui.QMessageBox.question(self, 'Error', "Please select a complaint first!")
            return

        elif atr == "":
            choice = QtGui.QMessageBox.critical(self, 'Error', "ATR cannot be blank")
            return

        comp_id = int(self.lineEdit_15.text())
        comp_obj = comp_dict[comp_id]
        comp_obj.action_report = atr
        comp_obj.action_status = "T"
        choice = QtGui.QMessageBox.information(self, 'Success', "ATR Successfully posted")
        self.update_comp_list()
        self.lineEdit_15.setText("")
        self.lineEdit_23.setText("")
        self.plainTextEdit_2.setPlainText("")
        self.plainTextEdit.setPlainText("")

    def gen_salary_list(self):
        hall_dict = dbr.rebuild("hall")
        hall_obj = hall_dict[this_warden.hall_ID]
        printer.generate_salary_list(hall_obj)
        choice = QtGui.QMessageBox.information(self, 'Success', "PDF of salary list has been generated.")

    def pay_salaries(self):
        hall_ID = this_warden.hall_ID
        hall_dict = dbr.rebuild("hall")
        hall_obj = hall_dict[hall_ID]
        total_salary = this_warden.salary_charge(dbr.rebuild("worker"))

        if total_salary > hall_obj.salary_account:
            choice = QtGui.QMessageBox.question(self, 'Error',
                                                "Insufficient funds in hall's salary account. Consider a grant request.")
        else:
            hall_obj.salary_account -= total_salary
            printer.issue_cheque("Workers", total_salary)
            choice = QtGui.QMessageBox.information(self, 'Success',
                                                   "An amount of " + str(total_salary) +
                                                   " Rs has been deducted from hall's salary account. Print command "
                                                   "for cheques has been given.")
            worker_dict = dbr.rebuild("worker")
            for key in worker_dict:
                worker = worker_dict[key]
                if worker.hall_ID == hall_ID and isinstance(worker, attendant.Attendant):
                    worker.monthly_attendance = 0

    def fire_worker(self):
        """
        Fire selected worker from Hall
        Update worker table
        """

        worker_table = dbr.rebuild("worker")
        worker_ID = 0
        if self.tableWidget.selectedItems():
            worker_ID = int(self.tableWidget.selectedItems()[0].text())

        if worker_ID in worker_table:
            # Remove worker from table and database
            worker_table[worker_ID].remove()
            self.update_worker_table()

    def print_account_statement(self):
        """
        Print Hall Account Statement
        """

        hall_dict = dbr.rebuild("hall")
        printer.print_statement(hall_dict[this_warden.hall_ID])
        choice = QtGui.QMessageBox.information(self, 'Success', "PDF Generated")

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
            choice = QtGui.QMessageBox.information(self, 'Success', "Grant Request submitted")
            self.doubleSpinBox_2.setValue(0.00)
            self.doubleSpinBox_3.setValue(0.00)

    def password_validate(self):
        """
        Check password for login
        Set labels for various fields
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
            student_table = dbr.rebuild("student")
            single_count = 0
            double_count = 0
            total_single_count = 0
            total_double_count = 0
            for key in student_table:
                if student_table[key].room_type == "S":
                    total_single_count += 1
                else:
                    total_double_count += 1
                if student_table[key].hall_ID == hall_ID:
                    if student_table[key].room_type == "S":
                        single_count += 1
                    else:
                        double_count += 1

            self.lineEdit_8.setText(str(db.get("hall", hall_ID, "single_room_count")[0]))
            self.lineEdit_9.setText(str(single_count))
            self.lineEdit_10.setText(str(int(self.lineEdit_8.text()) - int(self.lineEdit_9.text())))

            self.lineEdit_17.setText(str(db.get("hall", hall_ID, "double_room_count")[0]))
            self.lineEdit_18.setText(str(double_count))
            self.lineEdit_21.setText(str(int(self.lineEdit_17.text()) - int(self.lineEdit_18.text())))

            # Worker Details Table - add labels and values from database
            worker_table = dbr.rebuild("worker")
            for key in worker_table:
                if worker_table[key].hall_ID == this_warden.hall_ID \
                        and isinstance(worker_table[key], attendant.Attendant):
                    rowPosition = self.tableWidget.rowCount()
                    self.tableWidget.insertRow(rowPosition)
                    self.tableWidget.setItem(rowPosition, 0, QtGui.QTableWidgetItem(str(worker_table[key].worker_ID)))
                    self.tableWidget.setItem(rowPosition, 1, QtGui.QTableWidgetItem(worker_table[key].name))

            # Grant Request Tab - add labels and values from database
            self.lineEdit.setText(str(this_warden.salary_charge(worker_table)))
            self.check_grant_button()

            # View Complaints Tab - add conditions
            student_dict = student_table
            comp_dict = dbr.rebuild("complaint")
            comp_ids_strs = []
            for key in comp_dict:
                if student_dict[comp_dict[key].student_ID].hall_ID == hall_ID and comp_dict[key].action_status == "P":
                    comp_ids_strs.append(str(comp_dict[key].complaint_ID))
            self.listWidget.addItems(comp_ids_strs)
            self.label_49.setText("")

            # View Overall Occupancy Tab - add conditions
            if this_warden.controlling_warden == "False":
                self.label_4.setVisible(True)
                self.groupBox_7.setVisible(False)
                self.groupBox_8.setVisible(False)
            else:
                self.label_4.setVisible(False)
                self.groupBox_7.setVisible(True)
                self.groupBox_8.setVisible(True)

                # Set data for total occupancies
                total_occ = this_warden.total_occupancy(dbr.rebuild("hall"))
                self.lineEdit_24.setText(str(total_occ['single_total']))
                self.lineEdit_25.setText(str(total_single_count))
                self.lineEdit_26.setText(str(int(self.lineEdit_24.text()) - int(self.lineEdit_25.text())))

                self.lineEdit_27.setText(str(total_occ['double_total']))
                self.lineEdit_28.setText(str(total_double_count))
                self.lineEdit_29.setText(str(int(self.lineEdit_27.text()) - int(self.lineEdit_28.text())))

            self.stackedWidget.setCurrentIndex(0)
        else:
            self.label_42.setText("Authentication Failed. Please try again")

    def update_comp_list(self):
        self.listWidget.clear()
        student_dict = dbr.rebuild("student")
        comp_dict = dbr.rebuild("complaint")
        hall_ID = this_warden.hall_ID
        comp_ids_strs = []
        for key in comp_dict:
            if student_dict[comp_dict[key].student_ID].hall_ID == hall_ID and comp_dict[key].action_status == "P":
                comp_ids_strs.append(str(comp_dict[key].complaint_ID))
        self.listWidget.addItems(comp_ids_strs)
        self.label_49.setText("")

    def update_worker_table(self):
        self.clear_worker_table()
        worker_table = dbr.rebuild("worker")
        for key in worker_table:
            if worker_table[key].hall_ID == this_warden.hall_ID \
                    and isinstance(worker_table[key], attendant.Attendant):
                rowPosition = self.tableWidget.rowCount()
                self.tableWidget.insertRow(rowPosition)
                self.tableWidget.setItem(rowPosition, 0, QtGui.QTableWidgetItem(str(worker_table[key].worker_ID)))
                self.tableWidget.setItem(rowPosition, 1, QtGui.QTableWidgetItem(worker_table[key].name))

    def clear_worker_table(self):
        while(self.tableWidget.rowCount()>0):
            self.tableWidget.removeRow(0)

    def hire_new_worker(self):
        global this_warden
        hall_ID = this_warden.hall_ID
        worker_name = self.lineEdit_22.text()
        worker_wage = self.doubleSpinBox.value()
        if worker_name == "":
            choice = QtGui.QMessageBox.question(self, 'Error', "Worker name can't be blank")
        elif worker_wage == 0.:
            choice = QtGui.QMessageBox.question(self, 'Error', "Worker wage can't be 0")
        else:
            attendant.Attendant(worker_name, hall_ID, worker_wage, 0)
            choice = QtGui.QMessageBox.information(self, 'Success', "Worker successfully hired.")
            self.update_worker_table()
            self.lineEdit_22.setText("")
            self.doubleSpinBox.setValue(0.00)


app = QApplication(sys.argv)
form = WardenWindowClass()
form.show()
app.exec_()
