
import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtCore, QtGui
import Student_Main_Window
from Complaint_GUI import ComplaintWindowClass

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s


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

'''
app = QApplication(sys.argv)
form = StudentMainWindowClass()
form.show()
app.exec_()
'''