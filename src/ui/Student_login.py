# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Student_login.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_StudentLoginWindow(object):
    def setupUi(self, StudentLoginWindow):
        StudentLoginWindow.setObjectName(_fromUtf8("StudentLoginWindow"))
        StudentLoginWindow.resize(373, 181)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../Desktop/kgplogo.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        StudentLoginWindow.setWindowIcon(icon)
        self.loginGroupBox = QtGui.QGroupBox(StudentLoginWindow)
        self.loginGroupBox.setGeometry(QtCore.QRect(9, 9, 351, 161))
        self.loginGroupBox.setObjectName(_fromUtf8("loginGroupBox"))
        self.label = QtGui.QLabel(self.loginGroupBox)
        self.label.setGeometry(QtCore.QRect(20, 40, 61, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.loginGroupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 61, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.IDTextBox = QtGui.QLineEdit(self.loginGroupBox)
        self.IDTextBox.setGeometry(QtCore.QRect(90, 40, 231, 20))
        self.IDTextBox.setObjectName(_fromUtf8("IDTextBox"))
        self.passwordTextBox = QtGui.QLineEdit(self.loginGroupBox)
        self.passwordTextBox.setGeometry(QtCore.QRect(90, 70, 231, 20))
        self.passwordTextBox.setInputMask(_fromUtf8(""))
        self.passwordTextBox.setEchoMode(QtGui.QLineEdit.Password)
        self.passwordTextBox.setObjectName(_fromUtf8("passwordTextBox"))
        self.loginButton = QtGui.QPushButton(self.loginGroupBox)
        self.loginButton.setGeometry(QtCore.QRect(40, 120, 75, 23))
        self.loginButton.setObjectName(_fromUtf8("loginButton"))
        self.label_3 = QtGui.QLabel(self.loginGroupBox)
        self.label_3.setGeometry(QtCore.QRect(-10, -10, 371, 191))
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_3.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.IDTextBox.raise_()
        self.passwordTextBox.raise_()
        self.loginButton.raise_()

        self.retranslateUi(StudentLoginWindow)
        QtCore.QMetaObject.connectSlotsByName(StudentLoginWindow)

    def retranslateUi(self, StudentLoginWindow):
        StudentLoginWindow.setWindowTitle(_translate("StudentLoginWindow", "Student Login", None))
        self.loginGroupBox.setTitle(_translate("StudentLoginWindow", " Student Login ", None))
        self.label.setText(_translate("StudentLoginWindow", "Student ID.", None))
        self.label_2.setText(_translate("StudentLoginWindow", "Password", None))
        self.loginButton.setText(_translate("StudentLoginWindow", "Login", None))

