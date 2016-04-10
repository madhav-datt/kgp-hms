import sys
from PyQt4.QtGui import *
from ..database import db_func as db
from ..database import db_rebuild as dbr
from ..database import login
from ..actors import warden
from PyQt4 import QtCore, QtGui
import warden_window

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s


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

<<<<<<< HEAD
        warden.Warden("a", "War", "who cares", 0)
        self.pushButton_10.clicked.connect(self.password_validate)

    def password_validate(self):
        """
        Check password for login
        """

        user_ID = int(self.lineEdit_19.text())
        password = self.lineEdit_20.text()
        if login.authenticate("warden", user_ID, password):
            
        else:
            self.label_42.setText("Authentication Failed. Please try again")
=======
        


>>>>>>> a4776a1fa2e77439e0bd96787bedf74d535c81be

app = QApplication(sys.argv)
form = WardenWindowClass()
form.show()
app.exec_()
