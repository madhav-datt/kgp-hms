import sys
from PyQt4.QtGui import *
from ..database import db_func as db
from ..database import db_rebuild as dbr
from ..database import login
from PyQt4 import QtCore, QtGui
import warden_window

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s


class MessManagerWindowClass(QtGui.QWidget, warden_window.Ui_Form):
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

        



app = QApplication(sys.argv)
form = MessManagerWindowClass()
form.show()
app.exec_()
