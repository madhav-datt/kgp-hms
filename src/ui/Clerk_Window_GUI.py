import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtCore, QtGui
import Clerk_Window, time

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s


class ClerkWindowClass(QtGui.QWidget, Clerk_Window.Ui_Form):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
        self.bkdLabel.setPixmap(QtGui.QPixmap(_fromUtf8('bkd4.jpg')))
        self.bkdLabel.setScaledContents(True)
        self.label_8.setText("Today's Date : " + time.strftime("%x"))


app = QtGui.QApplication(sys.argv)
Form = ClerkWindowClass()
Form.show()
app.exec_()