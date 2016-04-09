import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
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
        self.label_7.setPixmap(QtGui.QPixmap(_fromUtf8('bkd1edit2.jpg')))
        self.label_7.setScaledContents(True)

        self.label_12.setPixmap(QtGui.QPixmap(_fromUtf8('bkd1edit2.jpg')))
        self.label_12.setScaledContents(True)

app = QApplication(sys.argv)
form = MessManagerWindowClass()
form.show()
app.exec_()