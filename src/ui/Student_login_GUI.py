import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtCore, QtGui
import Student_login


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s


class StudentLoginClass(QtGui.QWidget, Student_login.Ui_StudentLoginWindow):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.setupUi(self)
        '''
        myPixmap = QtGui.QPixmap(_fromUtf8('calma.jpg'))
        myScaledPixmap = myPixmap.scaled(self.label.size())
        self.label_3.setPixmap(myScaledPixmap)

        self.label_3.setPixmap(QtGui.QPixmap(_fromUtf8('calma.jpg')))
        self.label_3.setScaledContents(True)
        '''

app = QApplication(sys.argv)
form = StudentLoginClass()
form.show()
app.exec_()