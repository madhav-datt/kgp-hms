# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Student_Main_Window.ui'
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(581, 544)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../Desktop/logo2.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.stackedWidget = QtGui.QStackedWidget(Form)
        self.stackedWidget.setGeometry(QtCore.QRect(-1, 0, 581, 541))
        self.stackedWidget.setObjectName(_fromUtf8("stackedWidget"))
        self.page_5 = QtGui.QWidget()
        self.page_5.setObjectName(_fromUtf8("page_5"))
        self.label_32 = QtGui.QLabel(self.page_5)
        self.label_32.setGeometry(QtCore.QRect(0, 0, 571, 561))
        self.label_32.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 0);"))
        self.label_32.setObjectName(_fromUtf8("label_32"))
        self.label_33 = QtGui.QLabel(self.page_5)
        self.label_33.setGeometry(QtCore.QRect(30, 20, 201, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Cambria"))
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_33.setFont(font)
        self.label_33.setStyleSheet(_fromUtf8("color : rgb(255, 255, 255)"))
        self.label_33.setObjectName(_fromUtf8("label_33"))
        self.label_34 = QtGui.QLabel(self.page_5)
        self.label_34.setGeometry(QtCore.QRect(30, 80, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_34.setFont(font)
        self.label_34.setStyleSheet(_fromUtf8("color : rgb(255, 255, 255)"))
        self.label_34.setObjectName(_fromUtf8("label_34"))
        self.label_35 = QtGui.QLabel(self.page_5)
        self.label_35.setGeometry(QtCore.QRect(30, 120, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_35.setFont(font)
        self.label_35.setStyleSheet(_fromUtf8("color : rgb(255, 255, 255)"))
        self.label_35.setObjectName(_fromUtf8("label_35"))
        self.lineEdit_19 = QtGui.QLineEdit(self.page_5)
        self.lineEdit_19.setGeometry(QtCore.QRect(120, 80, 201, 20))
        self.lineEdit_19.setObjectName(_fromUtf8("lineEdit_19"))
        self.lineEdit_20 = QtGui.QLineEdit(self.page_5)
        self.lineEdit_20.setGeometry(QtCore.QRect(120, 120, 201, 20))
        self.lineEdit_20.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdit_20.setObjectName(_fromUtf8("lineEdit_20"))
        self.pushButton_10 = QtGui.QPushButton(self.page_5)
        self.pushButton_10.setGeometry(QtCore.QRect(40, 180, 241, 23))
        self.pushButton_10.setObjectName(_fromUtf8("pushButton_10"))
        self.label_36 = QtGui.QLabel(self.page_5)
        self.label_36.setGeometry(QtCore.QRect(20, 240, 511, 16))
        self.label_36.setStyleSheet(_fromUtf8("color : rgb(255, 255, 255)"))
        self.label_36.setObjectName(_fromUtf8("label_36"))
        self.stackedWidget.addWidget(self.page_5)
        self.page = QtGui.QWidget()
        self.page.setObjectName(_fromUtf8("page"))
        self.label = QtGui.QLabel(self.page)
        self.label.setGeometry(QtCore.QRect(5, 3, 571, 561))
        self.label.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 0);"))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.page)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 201, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Cambria"))
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(_fromUtf8("color : rgb(255, 255, 255)"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.groupBox_3 = QtGui.QGroupBox(self.page)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 470, 541, 61))
        self.groupBox_3.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255)"))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.horizontalLayoutWidget = QtGui.QWidget(self.groupBox_3)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(9, 10, 521, 51))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButton_5 = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_5.setStyleSheet(_fromUtf8("color : rgb(0, 0, 0)"))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.horizontalLayout.addWidget(self.pushButton_5)
        self.pushButton_4 = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_4.setStyleSheet(_fromUtf8("color : rgb(0, 0, 0)"))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.pushButton_3 = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_3.setStyleSheet(_fromUtf8("color : rgb(0, 0, 0)"))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.groupBox_2 = QtGui.QGroupBox(self.page)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 330, 391, 131))
        self.groupBox_2.setStyleSheet(_fromUtf8("color : rgb(255, 255, 255)"))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.listWidget = QtGui.QListWidget(self.groupBox_2)
        self.listWidget.setGeometry(QtCore.QRect(10, 20, 171, 101))
        self.listWidget.setStyleSheet(_fromUtf8("background-color : rgb(204,204,204);\n"
"color : rgb(0, 0, 0)"))
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        item = QtGui.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        self.listWidget.addItem(item)
        self.pushButton = QtGui.QPushButton(self.groupBox_2)
        self.pushButton.setGeometry(QtCore.QRect(230, 30, 131, 23))
        self.pushButton.setStyleSheet(_fromUtf8("color : rgb(0,0,0);\n"
""))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.groupBox_2)
        self.pushButton_2.setGeometry(QtCore.QRect(230, 80, 131, 23))
        self.pushButton_2.setStyleSheet(_fromUtf8("color : rgb(0,0,0);\n"
""))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.groupBox = QtGui.QGroupBox(self.page)
        self.groupBox.setEnabled(True)
        self.groupBox.setGeometry(QtCore.QRect(20, 60, 271, 251))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet(_fromUtf8("color : rgb(255, 255, 255)"))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 30, 46, 13))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(10, 60, 46, 13))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(10, 90, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(10, 120, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(10, 150, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(10, 180, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_8.setFont(font)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(10, 210, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_9.setFont(font)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.lineEdit = QtGui.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(90, 30, 171, 20))
        self.lineEdit.setStyleSheet(_fromUtf8("color : rgb(0, 0, 0)"))
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setPlaceholderText(_fromUtf8(""))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(90, 60, 171, 20))
        self.lineEdit_2.setStyleSheet(_fromUtf8("color : rgb(0, 0, 0)"))
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.lineEdit_3 = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_3.setGeometry(QtCore.QRect(90, 90, 171, 20))
        self.lineEdit_3.setStyleSheet(_fromUtf8("color : rgb(0,0,0)\n"
""))
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.lineEdit_4 = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_4.setGeometry(QtCore.QRect(90, 120, 171, 20))
        self.lineEdit_4.setStyleSheet(_fromUtf8("color : rgb(0, 0, 0)\n"
""))
        self.lineEdit_4.setReadOnly(True)
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.lineEdit_5 = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_5.setGeometry(QtCore.QRect(90, 150, 171, 20))
        self.lineEdit_5.setStyleSheet(_fromUtf8("color : rgb(0, 0, 0)"))
        self.lineEdit_5.setReadOnly(True)
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.lineEdit_6 = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_6.setGeometry(QtCore.QRect(90, 180, 171, 20))
        self.lineEdit_6.setStyleSheet(_fromUtf8("color : rgb(0, 0, 0)"))
        self.lineEdit_6.setReadOnly(True)
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.lineEdit_7 = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_7.setGeometry(QtCore.QRect(90, 210, 171, 20))
        self.lineEdit_7.setStyleSheet(_fromUtf8("color : rgb(0, 0, 0)"))
        self.lineEdit_7.setReadOnly(True)
        self.lineEdit_7.setObjectName(_fromUtf8("lineEdit_7"))
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtGui.QWidget()
        self.page_2.setObjectName(_fromUtf8("page_2"))
        self.label_10 = QtGui.QLabel(self.page_2)
        self.label_10.setGeometry(QtCore.QRect(0, 0, 581, 561))
        self.label_10.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 0);"))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.label_11 = QtGui.QLabel(self.page_2)
        self.label_11.setGeometry(QtCore.QRect(20, 20, 131, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Cambria"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet(_fromUtf8("color : rgb(255, 255, 255)"))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.groupBox_4 = QtGui.QGroupBox(self.page_2)
        self.groupBox_4.setGeometry(QtCore.QRect(20, 50, 291, 201))
        self.groupBox_4.setStyleSheet(_fromUtf8("color : rgb(255, 255, 255)"))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.label_12 = QtGui.QLabel(self.groupBox_4)
        self.label_12.setGeometry(QtCore.QRect(10, 30, 81, 16))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.label_13 = QtGui.QLabel(self.groupBox_4)
        self.label_13.setGeometry(QtCore.QRect(10, 60, 91, 16))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.label_14 = QtGui.QLabel(self.groupBox_4)
        self.label_14.setGeometry(QtCore.QRect(10, 90, 91, 16))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.line = QtGui.QFrame(self.groupBox_4)
        self.line.setGeometry(QtCore.QRect(0, 120, 291, 20))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.lineEdit_8 = QtGui.QLineEdit(self.groupBox_4)
        self.lineEdit_8.setGeometry(QtCore.QRect(110, 30, 161, 20))
        self.lineEdit_8.setStyleSheet(_fromUtf8("color : rgb(255, 255, 255)"))
        self.lineEdit_8.setReadOnly(True)
        self.lineEdit_8.setObjectName(_fromUtf8("lineEdit_8"))
        self.lineEdit_9 = QtGui.QLineEdit(self.groupBox_4)
        self.lineEdit_9.setGeometry(QtCore.QRect(110, 60, 161, 20))
        self.lineEdit_9.setStyleSheet(_fromUtf8("color : rgb(255, 255, 255)"))
        self.lineEdit_9.setReadOnly(True)
        self.lineEdit_9.setObjectName(_fromUtf8("lineEdit_9"))
        self.lineEdit_10 = QtGui.QLineEdit(self.groupBox_4)
        self.lineEdit_10.setGeometry(QtCore.QRect(110, 90, 161, 20))
        self.lineEdit_10.setStyleSheet(_fromUtf8("color : rgb(255, 255, 255)"))
        self.lineEdit_10.setReadOnly(True)
        self.lineEdit_10.setObjectName(_fromUtf8("lineEdit_10"))
        self.label_15 = QtGui.QLabel(self.groupBox_4)
        self.label_15.setGeometry(QtCore.QRect(10, 150, 61, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.lineEdit_11 = QtGui.QLineEdit(self.groupBox_4)
        self.lineEdit_11.setGeometry(QtCore.QRect(110, 150, 161, 20))
        self.lineEdit_11.setStyleSheet(_fromUtf8("color : rgb(255, 255, 255)"))
        self.lineEdit_11.setReadOnly(True)
        self.lineEdit_11.setObjectName(_fromUtf8("lineEdit_11"))
        self.pushButton_6 = QtGui.QPushButton(self.page_2)
        self.pushButton_6.setGeometry(QtCore.QRect(20, 290, 291, 23))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.groupBox_5 = QtGui.QGroupBox(self.page_2)
        self.groupBox_5.setGeometry(QtCore.QRect(20, 390, 401, 121))
        self.groupBox_5.setStyleSheet(_fromUtf8("color : rgb(255, 255, 255)"))
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.label_16 = QtGui.QLabel(self.groupBox_5)
        self.label_16.setGeometry(QtCore.QRect(10, 30, 391, 21))
        self.label_16.setWordWrap(True)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.label_17 = QtGui.QLabel(self.groupBox_5)
        self.label_17.setGeometry(QtCore.QRect(10, 60, 391, 21))
        self.label_17.setWordWrap(True)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.label_18 = QtGui.QLabel(self.groupBox_5)
        self.label_18.setGeometry(QtCore.QRect(10, 90, 391, 21))
        self.label_18.setWordWrap(True)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.pushButton_7 = QtGui.QPushButton(self.page_2)
        self.pushButton_7.setGeometry(QtCore.QRect(20, 320, 291, 23))
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtGui.QWidget()
        self.page_3.setObjectName(_fromUtf8("page_3"))
        self.label_19 = QtGui.QLabel(self.page_3)
        self.label_19.setGeometry(QtCore.QRect(20, 20, 171, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Cambria"))
        font.setPointSize(16)
        self.label_19.setFont(font)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.label_20 = QtGui.QLabel(self.page_3)
        self.label_20.setGeometry(QtCore.QRect(30, 70, 121, 16))
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.label_21 = QtGui.QLabel(self.page_3)
        self.label_21.setGeometry(QtCore.QRect(30, 110, 121, 16))
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.label_22 = QtGui.QLabel(self.page_3)
        self.label_22.setGeometry(QtCore.QRect(30, 150, 121, 16))
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.lineEdit_12 = QtGui.QLineEdit(self.page_3)
        self.lineEdit_12.setGeometry(QtCore.QRect(190, 70, 241, 20))
        self.lineEdit_12.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdit_12.setObjectName(_fromUtf8("lineEdit_12"))
        self.lineEdit_13 = QtGui.QLineEdit(self.page_3)
        self.lineEdit_13.setGeometry(QtCore.QRect(190, 110, 241, 20))
        self.lineEdit_13.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdit_13.setObjectName(_fromUtf8("lineEdit_13"))
        self.lineEdit_14 = QtGui.QLineEdit(self.page_3)
        self.lineEdit_14.setGeometry(QtCore.QRect(190, 150, 241, 20))
        self.lineEdit_14.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdit_14.setObjectName(_fromUtf8("lineEdit_14"))
        self.pushButton_8 = QtGui.QPushButton(self.page_3)
        self.pushButton_8.setGeometry(QtCore.QRect(30, 220, 221, 23))
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
        self.pushButton_9 = QtGui.QPushButton(self.page_3)
        self.pushButton_9.setGeometry(QtCore.QRect(30, 260, 221, 23))
        self.pushButton_9.setObjectName(_fromUtf8("pushButton_9"))
        self.label_23 = QtGui.QLabel(self.page_3)
        self.label_23.setGeometry(QtCore.QRect(30, 190, 401, 16))
        self.label_23.setText(_fromUtf8(""))
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtGui.QWidget()
        self.page_4.setObjectName(_fromUtf8("page_4"))
        self.lineEdit_15 = QtGui.QLineEdit(self.page_4)
        self.lineEdit_15.setGeometry(QtCore.QRect(190, 70, 204, 20))
        self.lineEdit_15.setReadOnly(True)
        self.lineEdit_15.setObjectName(_fromUtf8("lineEdit_15"))
        self.plainTextEdit_2 = QtGui.QPlainTextEdit(self.page_4)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(190, 350, 204, 81))
        self.plainTextEdit_2.setReadOnly(True)
        self.plainTextEdit_2.setObjectName(_fromUtf8("plainTextEdit_2"))
        self.label_24 = QtGui.QLabel(self.page_4)
        self.label_24.setGeometry(QtCore.QRect(28, 134, 72, 20))
        self.label_24.setStyleSheet(_fromUtf8("color : rgb(255, 255, 255)"))
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.label_25 = QtGui.QLabel(self.page_4)
        self.label_25.setGeometry(QtCore.QRect(28, 22, 366, 22))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Cambria"))
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_25.setFont(font)
        self.label_25.setStyleSheet(_fromUtf8("color : rgb(255, 255, 255)"))
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.label_26 = QtGui.QLabel(self.page_4)
        self.label_26.setGeometry(QtCore.QRect(28, 70, 64, 20))
        self.label_26.setStyleSheet(_fromUtf8("color : rgb(255, 255, 255)"))
        self.label_26.setObjectName(_fromUtf8("label_26"))
        self.buttonBox = QtGui.QDialogButtonBox(self.page_4)
        self.buttonBox.setGeometry(QtCore.QRect(30, 460, 156, 23))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Save)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.lineEdit_17 = QtGui.QLineEdit(self.page_4)
        self.lineEdit_17.setGeometry(QtCore.QRect(190, 134, 204, 20))
        self.lineEdit_17.setReadOnly(True)
        self.lineEdit_17.setObjectName(_fromUtf8("lineEdit_17"))
        self.label_27 = QtGui.QLabel(self.page_4)
        self.label_27.setGeometry(QtCore.QRect(20, 180, 103, 22))
        self.label_27.setStyleSheet(_fromUtf8("color : rgb(255, 255, 255)"))
        self.label_27.setObjectName(_fromUtf8("label_27"))
        self.label_28 = QtGui.QLabel(self.page_4)
        self.label_28.setGeometry(QtCore.QRect(20, 350, 127, 22))
        self.label_28.setStyleSheet(_fromUtf8("color : rgb(255, 255, 255)"))
        self.label_28.setObjectName(_fromUtf8("label_28"))
        self.plainTextEdit = QtGui.QPlainTextEdit(self.page_4)
        self.plainTextEdit.setGeometry(QtCore.QRect(190, 180, 204, 111))
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.label_29 = QtGui.QLabel(self.page_4)
        self.label_29.setGeometry(QtCore.QRect(28, 102, 52, 20))
        self.label_29.setStyleSheet(_fromUtf8("color : rgb(255, 255, 255)"))
        self.label_29.setObjectName(_fromUtf8("label_29"))
        self.lineEdit_18 = QtGui.QLineEdit(self.page_4)
        self.lineEdit_18.setGeometry(QtCore.QRect(190, 102, 204, 20))
        self.lineEdit_18.setReadOnly(True)
        self.lineEdit_18.setObjectName(_fromUtf8("lineEdit_18"))
        self.label_31 = QtGui.QLabel(self.page_4)
        self.label_31.setGeometry(QtCore.QRect(10, 0, 571, 561))
        self.label_31.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 0);"))
        self.label_31.setObjectName(_fromUtf8("label_31"))
        self.label_30 = QtGui.QLabel(self.page_4)
        self.label_30.setGeometry(QtCore.QRect(20, 310, 103, 22))
        self.label_30.setStyleSheet(_fromUtf8("color : rgb(255, 255, 255)"))
        self.label_30.setObjectName(_fromUtf8("label_30"))
        self.lineEdit_16 = QtGui.QLineEdit(self.page_4)
        self.lineEdit_16.setGeometry(QtCore.QRect(190, 310, 204, 20))
        self.lineEdit_16.setReadOnly(True)
        self.lineEdit_16.setObjectName(_fromUtf8("lineEdit_16"))
        self.pushButton_11 = QtGui.QPushButton(self.page_4)
        self.pushButton_11.setGeometry(QtCore.QRect(30, 490, 131, 23))
        self.pushButton_11.setObjectName(_fromUtf8("pushButton_11"))
        self.label_31.raise_()
        self.lineEdit_15.raise_()
        self.plainTextEdit_2.raise_()
        self.label_24.raise_()
        self.label_25.raise_()
        self.label_26.raise_()
        self.buttonBox.raise_()
        self.lineEdit_17.raise_()
        self.label_27.raise_()
        self.label_28.raise_()
        self.plainTextEdit.raise_()
        self.label_29.raise_()
        self.lineEdit_18.raise_()
        self.label_30.raise_()
        self.lineEdit_16.raise_()
        self.pushButton_11.raise_()
        self.stackedWidget.addWidget(self.page_4)

        self.retranslateUi(Form)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "HMS - Student Portal", None))
        self.label_32.setText(_translate("Form", "TextLabel", None))
        self.label_33.setText(_translate("Form", "Student Login", None))
        self.label_34.setText(_translate("Form", "Student ID", None))
        self.label_35.setText(_translate("Form", "Password", None))
        self.pushButton_10.setText(_translate("Form", "Login", None))
        self.label_36.setText(_translate("Form", "TextLabel", None))
        self.label.setText(_translate("Form", "TextLabel", None))
        self.label_2.setText(_translate("Form", "WELCOME TORVALTZ!", None))
        self.groupBox_3.setTitle(_translate("Form", "Actions", None))
        self.pushButton_5.setText(_translate("Form", "Change Password", None))
        self.pushButton_4.setText(_translate("Form", "Pay Dues", None))
        self.pushButton_3.setText(_translate("Form", "Register New Complaint", None))
        self.groupBox_2.setTitle(_translate("Form", "Active Complaints", None))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("Form", "Complaint 1", None))
        item = self.listWidget.item(1)
        item.setText(_translate("Form", "Complaint 2", None))
        item = self.listWidget.item(2)
        item.setText(_translate("Form", "Complaint 3", None))
        item = self.listWidget.item(3)
        item.setText(_translate("Form", "Complaint 4", None))
        item = self.listWidget.item(4)
        item.setText(_translate("Form", "Complaint 6", None))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton.setText(_translate("Form", "View Complaint", None))
        self.pushButton_2.setText(_translate("Form", "Delete Complaint", None))
        self.groupBox.setTitle(_translate("Form", "Your Information", None))
        self.label_3.setText(_translate("Form", "Name", None))
        self.label_4.setText(_translate("Form", "Address", None))
        self.label_5.setText(_translate("Form", "Contact No.", None))
        self.label_6.setText(_translate("Form", "Hall Alloted", None))
        self.label_7.setText(_translate("Form", "Room No.", None))
        self.label_8.setText(_translate("Form", "Room Type", None))
        self.label_9.setText(_translate("Form", "Student ID", None))
        self.label_10.setText(_translate("Form", "TextLabel", None))
        self.label_11.setText(_translate("Form", "DUE PAYMENT", None))
        self.groupBox_4.setTitle(_translate("Form", "Your Due Information", None))
        self.label_12.setText(_translate("Form", "Mess Charges", None))
        self.label_13.setText(_translate("Form", "Amenity Charges", None))
        self.label_14.setText(_translate("Form", "Room Rent", None))
        self.label_15.setText(_translate("Form", "Total Dues", None))
        self.pushButton_6.setText(_translate("Form", "Pay Dues", None))
        self.groupBox_5.setTitle(_translate("Form", "Important Information", None))
        self.label_16.setText(_translate("Form", "1. The total due amount will be deducted from the amount in your Institute Account.", None))
        self.label_17.setText(_translate("Form", "2. Payment once made cannot be refunded. Please be sure before due payment", None))
        self.label_18.setText(_translate("Form", "3. You\'ll receive a printed receipt from your Warden once the payment is confirmed.", None))
        self.pushButton_7.setText(_translate("Form", "Go Back", None))
        self.label_19.setText(_translate("Form", "Change Password", None))
        self.label_20.setText(_translate("Form", "Enter Current Password", None))
        self.label_21.setText(_translate("Form", "Enter New Password", None))
        self.label_22.setText(_translate("Form", "Confirm Password", None))
        self.pushButton_8.setText(_translate("Form", "Save New Password", None))
        self.pushButton_9.setText(_translate("Form", "Cancel", None))
        self.label_24.setText(_translate("Form", "Concerned Hall", None))
        self.label_25.setText(_translate("Form", "Student Complaint", None))
        self.label_26.setText(_translate("Form", "Complaint ID ", None))
        self.label_27.setText(_translate("Form", "Complaint Description", None))
        self.label_28.setText(_translate("Form", "Action Taken Report (ATR)", None))
        self.label_29.setText(_translate("Form", "Student ID", None))
        self.label_31.setText(_translate("Form", "TextLabel", None))
        self.label_30.setText(_translate("Form", "Complaint Status", None))
        self.pushButton_11.setText(_translate("Form", "Back", None))

