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

from PyQt4 import QtCore, QtGui
import Student_Main_Window
from Complaint_GUI import ComplaintWindowClass
from ..database import login
from ..database import db_rebuild as dbr
from ..database import db_func as db
from ..requests import complaint, printer

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

global student_ID
global curr_complaint_ID


class StudentMainWindowClass(QtGui.QWidget, Student_Main_Window.Ui_Form):
    """Student Window GUI and Functionality

        Opens with login screen
    """

    def __init__(self):
        """
        Init Student GUI as part of Integrated
        """

        QtGui.QWidget.__init__(self)
        self.setupUi(self)

        self.label.setPixmap(QtGui.QPixmap(_fromUtf8('src/ui/resources/bkd1edit2.jpg')))
        self.label.setScaledContents(True)

        self.label_10.setPixmap(QtGui.QPixmap(_fromUtf8('src/ui/resources/bkd1edit2.jpg')))
        self.label_10.setScaledContents(True)

        self.label_32.setPixmap(QtGui.QPixmap(_fromUtf8('src/ui/resources/bkd1edit2.jpg')))
        self.label_32.setScaledContents(True)

        self.label_31.setPixmap(QtGui.QPixmap(_fromUtf8('src/ui/resources/bkd1edit2.jpg')))
        self.label_31.setScaledContents(True)
        self.label_36.setText(" ")

        # self.pushButton_3.clicked.connect(self.show_complaint_window)
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
        self.pushButton.clicked.connect(self.view_complaint_button)
        self.pushButton_2.clicked.connect(self.delete_complaint_button)

    def pay_dues_button(self):
        """
        Pay calculated dues by student
        Add amount to hall accounts
        """

        stud_dict = dbr.rebuild("student")
        stud_obj = stud_dict[student_ID]
        hall_dict = dbr.rebuild("hall")
        hall_obj = hall_dict[stud_obj.hall_ID]
        printer.print_receipt(stud_obj)
        hall_obj.mess_account = float(hall_obj.mess_account) + float(self.lineEdit_8.text())
        stud_obj.mess_charge -= float(self.lineEdit_8.text())
        hall_obj.amenities_account = float(hall_obj.amenities_account) + float(self.lineEdit_9.text())
        hall_obj.rent_account = float(hall_obj.rent_account) + float(self.lineEdit_10.text())
        self.set_dues()

    def new_complaint_button(self):
        """
        Set labels for complaint creation interface
        Switch display to complaint interface
        """

        self.display_complaint_frame()
        self.label_26.setVisible(False)
        self.lineEdit_15.setVisible(False)
        self.lineEdit_18.setText(self.lineEdit_7.text())
        self.lineEdit_17.setText(self.lineEdit_4.text())
        self.lineEdit_16.setText("P")
        self.plainTextEdit_2.setPlainText("")
        self.buttonBox.setVisible(True)
        self.pushButton_11.setVisible(False)
        self.buttonBox.accepted.connect(self.create_new_complaint)
        self.plainTextEdit.setPlainText("")

    def create_new_complaint(self):
        """
        Create new complaint
        """

        description = str(self.plainTextEdit.toPlainText())
        action_report = ""
        new_complaint = complaint.Complaint(student_ID, "P", description, action_report)
        self.display_student_main_win()
        self.set_list()

    def password_validate(self):
        """
        Authenticate password for login
        """

        global student_ID
        hmc_dict = dbr.rebuild("hmc")
        user_ID = int(self.lineEdit_19.text())
        password = self.lineEdit_20.text()
        self.label_36.setText(" ")
        if login.authenticate("student", user_ID, password):
            student_ID = user_ID
            self.display(1)
            self.set_list()
            self.set_dues()
            for key in hmc_dict:
                if hmc_dict[key].payment_is_active == "T":
                    self.pushButton_6.setEnabled(True)
                else:
                    self.pushButton_6.setEnabled(False)
            if db.get("student", student_ID, "mess_charge")[0] == 0.:
                self.pushButton_6.setEnabled(False)
        else:
            self.label_36.setText("Wrong ID or Password. Please try again.")

    def set_dues(self):
        """
        Set amounts due to student payment interface
        """

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

            if stud_obj.room_type == "S":
                self.lineEdit_10.setText(str(hall_dict[hall_ID].single_room_rent))
            else:
                self.lineEdit_10.setText(str(hall_dict[hall_ID].double_room_rent))

            self.lineEdit_11.setText(str(float(self.lineEdit_8.text()) + float(self.lineEdit_9.text()) + \
                                         float(self.lineEdit_10.text())))

    def display_complaint_frame(self):
        """
        Switch to complaint display in stacked frames
        """

        self.display(4)

    def display_pwchange_frame(self):
        """
        Switch to password change display in stacked frames
        """

        self.display(3)
        self.resize(581, 344)

    def display_student_main_win(self):
        """
        Switch to main menu display in stacked frames
        """

        self.resize(581, 544)
        self.display(1)

    def show_complaint_window(self):
        """
        Switch to complaint display in stacked frames
        """

        self.window = ComplaintWindowClass()
        self.window.show()

    def display_dues_frame(self):
        """
        Switch to payment display in stacked frames
        """

        # self.resize(400, 490)
        self.display(2)

    def display(self, i):
        """
        Display i th screen from stacked deck
        Args: i = Number of screen to be displayed
        """

        self.stackedWidget.setCurrentIndex(i)
        hall_dict = dbr.rebuild("hall")
        student_dict = dbr.rebuild("student")
        if i == 1:
            self.label_2.setText("WELCOME " + student_dict[student_ID].name)
            self.lineEdit.setText(student_dict[student_ID].name)
            self.lineEdit_2.setText(student_dict[student_ID].address)
            self.lineEdit_3.setText(student_dict[student_ID].contact_number)
            hall_name = hall_dict[student_dict[student_ID].hall_ID].name
            self.lineEdit_4.setText(str(hall_name))
            self.lineEdit_5.setText(student_dict[student_ID].room_no)
            self.lineEdit_6.setText(student_dict[student_ID].room_type)
            self.lineEdit_7.setText(str(student_ID))

    def set_list(self):
        """
        Build complaints list from database
        """

        self.listWidget.clear()
        complaint_ids = []
        complaint_dict = dbr.rebuild("complaint")
        for key in complaint_dict:
            if complaint_dict[key].student_ID == student_ID:
                complaint_ids.append(str(complaint_dict[key].complaint_ID))
        self.listWidget.addItems(complaint_ids)

    def view_complaint_button(self):
        """
        Display selected complaint
        """

        global curr_complaint_ID
        self.pushButton_11.setVisible(True)
        self.buttonBox.setVisible(False)
        if self.listWidget.currentItem() is None:
            return
        else:
            curr_complaint_ID = int(self.listWidget.currentItem().text())
            self.display(4)
            self.set_complaint_details(curr_complaint_ID)

    def set_complaint_details(self, complaint_ID):
        """
        Set labels with details of complaint from passed ID
        """

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
        """
        Delete selected complaint from database
        Update complaint list interface
        """

        global curr_complaint_ID
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
        """
        Update student password to entered one
        """

        student_dict = dbr.rebuild("student")
        pwd_entered = str(self.lineEdit_12.text())
        new_pwd = str(self.lineEdit_13.text())
        new_pwd_1 = str(self.lineEdit_14.text())
        if login.authenticate("student", student_ID, pwd_entered) and new_pwd == new_pwd_1:
            self.label_23.setText("Password Successfully Changed!")
            student_dict[student_ID].password = new_pwd
            self.lineEdit_12.setText(" ")
            self.lineEdit_13.setText(" ")
            self.lineEdit_14.setText(" ")
            self.label_23.setText(" ")
        elif new_pwd == new_pwd_1:
            self.label_23.setText("Original password doesn't match entered password")
        else:
            self.label_23.setText("Password don't match")


def find_hall_ID_by_name(name):
    """
    Return hall ID for passed hall name
    """

    hall_dict = dbr.rebuild("hall")
    for key in hall_dict:
        if hall_dict[key].name == name:
            return key
    return 0


'''
app = QApplication(sys.argv)
form = StudentMainWindowClass()
form.show()
app.exec_()
'''
