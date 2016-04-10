
import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtCore, QtGui
import Student_Main_Window
from Complaint_GUI import ComplaintWindowClass
from ..database import login
from ..database import db_rebuild as dbr
from ..requests import complaint

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
        self.pushButton_8.clicked.connect(self.save_button_new_password)
        self.pushButton_3.clicked.connect(self.display_complaint_frame)
        self.buttonBox.rejected.connect(self.display_student_main_win)
        self.pushButton_10.clicked.connect(self.password_validate)
        self.pushButton_11.clicked.connect(self.display_student_main_win)
        self.pushButton_3.clicked.connect(self.new_complaint_button)
        self.pushButton_7.clicked.connect(self.display_student_main_win)
        self.pushButton_6.clicked.connect(self.pay_dues_button)

    def pay_dues_button(self):
        stud_dict = dbr.rebuild("student")
        stud_obj = stud_dict[student_ID]
        hall_dict = dbr.rebuild("hall")
        hall_obj =  hall_dict[stud_obj.hall_ID]
        hall_obj.mess_account = float(hall_obj.mess_account) + float(self.lineEdit_11.text())
        hall_obj.amenities_account

    def new_complaint_button(self):
        self.display_complaint_frame()
        self.label_26.setVisible(True)
        self.lineEdit_15.setVisible(False)
        self.lineEdit_18.setText(self.lineEdit_7.text())
        self.lineEdit_17.setText(self.lineEdit_4.text())
        self.lineEdit_16.setText("P")
        self.plainTextEdit_2.setPlainText("")
        self.buttonBox.setVisible(True)
        self.pushButton_11.setVisible(False)
        self.buttonBox.accepted.connect(self.create_new_complaint)

    def create_new_complaint(self):
        description = self.plainTextEdit.toPlainText()
        action_report = ""
        new_complaint = complaint(student_ID, "P", description, action_report)
        self.display_student_main_win()
        self.set_list()


    def password_validate(self):
        id = self.lineEdit_19.text()
        pwd = self.lineEdit_20.text()
        if login.authenticate("student", id, pwd):
            student_ID = id
            self.display(0)
            self.set_list()
            self.set_dues()
        else:
            self.label_36.setText("Wrong ID or Password. Please try again.")

    def set_dues(self):
        student_dict = dbr.rebuild("student")
        stud_obj = student_dict[student_ID]
        hall_dict = dbr.rebuild("hall")
        hall_ID = student_dict[student_ID].hall_ID
        if stud_obj.mess_charge == 0:
            self.lineEdit_8.setText(str(stud_obj.mess_charge))
            self.lineEdit_9.setText("0")
            self.lineEdit_10.setText("0")
            self.lineEdit_11.setText("0")
            self.pushButton_6.setEnabled(False)
        else:
            self.lineEdit_8.setText(str(stud_obj.mess_charge))
            self.lineEdit_9.setText(str(hall_dict[hall_ID].amenities_charge))
            if(stud_obj.room_type == "S"):
                self.lineEdit_10.setText(str(hall_dict[hall_ID].single_room_rent))
            else:
                self.lineEdit_10.setText(str(hall_dict[hall_ID].double_room_rent))
            self.lineEdit_11.setText(str(float(self.lineEdit_8) + float(self.lineEdit_9) + float(self.lineEdit_10)))
            self.pushButton_6.setEnabled(True)

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
        complaint_dict = dbr.rebuild("complaint")
        for key in complaint_dict:
            if complaint_dict[key].student_ID == student_ID:
                complaint_ids.append(complaint_dict[key].complaint_ID)
        self.listWidget.addItems(complaint_ids)

    def view_complaint_button(self):
        self.pushButton_11.setVisible(True)
        self.buttonBox.setVisible(False)
        if self.listWidget.currentItem() is None:
            return
        else:
            curr_complaint_ID = int(self.listWidget.currentItem().text())
            self.display_complaint_frame()
            self.set_complaint_details(curr_complaint_ID)

    def set_complaint_details(self, complaint_ID):
        complaint_dict = dbr.rebuild("complaint")
        student_dict = dbr.rebuild("student")
        hall_dict = dbr.rebuild("hall")
        self.lineEdit_15.setText(str(complaint_ID))
        self.lineEdit_18.setText(str(complaint_dict[complaint_ID].student_ID))
        self.lineEdit_17.setText(str(hall_dict[student_dict[complaint_dict[complaint_ID].student_ID].hall_ID].name))
        self.plainTextEdit.setPlainText(str(complaint_dict[complaint_ID].description))
        self.lineEdit_16.setText(str(complaint_dict[complaint_ID].action_status))
        self.plainTextEdit_2.setPlainText(str(complaint_dict[complaint_ID].action_report))

    def delete_complaint_button(self):
        if self.listWidget.currentItem() is None:
            return
        else:
            curr_complaint_ID = int(self.listWidget.currentItem().text())
            complaint_dict = dbr.rebuild("complaint")
            complaint_dict[curr_complaint_ID].remove()
            del complaint_dict[curr_complaint_ID]
            item = self.listWidget.takeItem(self.listWidget.currentRow())
            item = None

    def save_button_new_password(self):
        student_dict = dbr.rebuild("student")
        pwd_entered = str(self.lineEdit_12.text())
        new_pwd = str(self.lineEdit_13.text())
        new_pwd_1 = str(self.lineEdit_14.text())
        if login.authenticate("student", student_ID, pwd_entered) and new_pwd == new_pwd_1:
            self.label_23.setText("Password Successfully Changed!")
            student_dict[student_ID].password = pwd_entered
        elif new_pwd == new_pwd_1:
            self.label_23.setText("Original password doesn't match entered password")
        else:
            self.label_23.setText("Password don not match")

def find_hall_ID_by_name(name):
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