# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HMC.ui'
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
        Form.resize(630, 497)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("logo2.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.tabWidget = QtGui.QTabWidget(Form)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 751, 571))
        self.tabWidget.setTabPosition(QtGui.QTabWidget.North)
        self.tabWidget.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabWidget.setIconSize(QtCore.QSize(16, 16))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_1 = QtGui.QWidget()
        self.tab_1.setObjectName(_fromUtf8("tab_1"))
        self.tabWidget.addTab(self.tab_1, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.label_2 = QtGui.QLabel(self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(10, 20, 131, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Cambria"))
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label = QtGui.QLabel(self.tab_2)
        self.label.setGeometry(QtCore.QRect(5, 2, 621, 541))
        self.label.setText(_fromUtf8(""))
        self.label.setObjectName(_fromUtf8("label"))
        self.line = QtGui.QFrame(self.tab_2)
        self.line.setGeometry(QtCore.QRect(-10, 40, 631, 20))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.groupBox = QtGui.QGroupBox(self.tab_2)
        self.groupBox.setGeometry(QtCore.QRect(20, 90, 281, 121))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 60, 46, 13))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(10, 90, 46, 13))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(10, 30, 46, 13))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.lineEdit = QtGui.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(70, 30, 191, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(70, 60, 191, 20))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.lineEdit_3 = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_3.setGeometry(QtCore.QRect(70, 90, 191, 20))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.groupBox_2 = QtGui.QGroupBox(self.tab_2)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 260, 291, 151))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.label_6 = QtGui.QLabel(self.groupBox_2)
        self.label_6.setGeometry(QtCore.QRect(10, 30, 101, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(self.groupBox_2)
        self.label_7.setGeometry(QtCore.QRect(10, 90, 101, 16))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(self.groupBox_2)
        self.label_8.setGeometry(QtCore.QRect(10, 60, 101, 16))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(self.groupBox_2)
        self.label_9.setGeometry(QtCore.QRect(10, 120, 101, 16))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.lineEdit_4 = QtGui.QLineEdit(self.groupBox_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(120, 30, 161, 20))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.lineEdit_5 = QtGui.QLineEdit(self.groupBox_2)
        self.lineEdit_5.setGeometry(QtCore.QRect(120, 60, 161, 20))
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.lineEdit_6 = QtGui.QLineEdit(self.groupBox_2)
        self.lineEdit_6.setGeometry(QtCore.QRect(120, 90, 161, 20))
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.lineEdit_7 = QtGui.QLineEdit(self.groupBox_2)
        self.lineEdit_7.setGeometry(QtCore.QRect(120, 120, 161, 20))
        self.lineEdit_7.setObjectName(_fromUtf8("lineEdit_7"))
        self.groupBox_3 = QtGui.QGroupBox(self.tab_2)
        self.groupBox_3.setGeometry(QtCore.QRect(330, 90, 281, 151))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.label_10 = QtGui.QLabel(self.groupBox_3)
        self.label_10.setGeometry(QtCore.QRect(10, 30, 71, 16))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.label_11 = QtGui.QLabel(self.groupBox_3)
        self.label_11.setGeometry(QtCore.QRect(10, 60, 91, 16))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.label_12 = QtGui.QLabel(self.groupBox_3)
        self.label_12.setGeometry(QtCore.QRect(10, 90, 71, 16))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.label_13 = QtGui.QLabel(self.groupBox_3)
        self.label_13.setGeometry(QtCore.QRect(10, 120, 91, 16))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.lineEdit_8 = QtGui.QLineEdit(self.groupBox_3)
        self.lineEdit_8.setGeometry(QtCore.QRect(110, 30, 161, 20))
        self.lineEdit_8.setObjectName(_fromUtf8("lineEdit_8"))
        self.lineEdit_9 = QtGui.QLineEdit(self.groupBox_3)
        self.lineEdit_9.setGeometry(QtCore.QRect(110, 60, 161, 20))
        self.lineEdit_9.setObjectName(_fromUtf8("lineEdit_9"))
        self.lineEdit_10 = QtGui.QLineEdit(self.groupBox_3)
        self.lineEdit_10.setGeometry(QtCore.QRect(110, 90, 161, 20))
        self.lineEdit_10.setObjectName(_fromUtf8("lineEdit_10"))
        self.lineEdit_11 = QtGui.QLineEdit(self.groupBox_3)
        self.lineEdit_11.setGeometry(QtCore.QRect(110, 120, 161, 20))
        self.lineEdit_11.setObjectName(_fromUtf8("lineEdit_11"))
        self.pushButton = QtGui.QPushButton(self.tab_2)
        self.pushButton.setGeometry(QtCore.QRect(370, 300, 211, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.tab_2)
        self.pushButton_2.setGeometry(QtCore.QRect(370, 340, 211, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.label.raise_()
        self.label_2.raise_()
        self.line.raise_()
        self.groupBox.raise_()
        self.groupBox_2.raise_()
        self.groupBox_3.raise_()
        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.line_2 = QtGui.QFrame(self.tab_3)
        self.line_2.setGeometry(QtCore.QRect(-10, 360, 641, 20))
        self.line_2.setMidLineWidth(4)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.label_14 = QtGui.QLabel(self.tab_3)
        self.label_14.setGeometry(QtCore.QRect(10, 10, 151, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Cambria"))
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.label_21 = QtGui.QLabel(self.tab_3)
        self.label_21.setGeometry(QtCore.QRect(10, 110, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_21.setFont(font)
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.lineEdit_13 = QtGui.QLineEdit(self.tab_3)
        self.lineEdit_13.setGeometry(QtCore.QRect(90, 200, 171, 20))
        self.lineEdit_13.setStyleSheet(_fromUtf8("color : rgb(0, 0, 0)"))
        self.lineEdit_13.setReadOnly(False)
        self.lineEdit_13.setObjectName(_fromUtf8("lineEdit_13"))
        self.label_17 = QtGui.QLabel(self.tab_3)
        self.label_17.setGeometry(QtCore.QRect(10, 170, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_17.setFont(font)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.lineEdit_15 = QtGui.QLineEdit(self.tab_3)
        self.lineEdit_15.setGeometry(QtCore.QRect(90, 110, 171, 20))
        self.lineEdit_15.setStyleSheet(_fromUtf8("color : rgb(0,0,0)\n"
""))
        self.lineEdit_15.setReadOnly(False)
        self.lineEdit_15.setObjectName(_fromUtf8("lineEdit_15"))
        self.lineEdit_16 = QtGui.QLineEdit(self.tab_3)
        self.lineEdit_16.setGeometry(QtCore.QRect(90, 50, 171, 20))
        self.lineEdit_16.setStyleSheet(_fromUtf8("color : rgb(0, 0, 0)"))
        self.lineEdit_16.setReadOnly(False)
        self.lineEdit_16.setPlaceholderText(_fromUtf8(""))
        self.lineEdit_16.setObjectName(_fromUtf8("lineEdit_16"))
        self.label_15 = QtGui.QLabel(self.tab_3)
        self.label_15.setGeometry(QtCore.QRect(10, 230, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_15.setFont(font)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.label_16 = QtGui.QLabel(self.tab_3)
        self.label_16.setGeometry(QtCore.QRect(10, 140, 46, 13))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_16.setFont(font)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.label_18 = QtGui.QLabel(self.tab_3)
        self.label_18.setGeometry(QtCore.QRect(10, 50, 46, 13))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_18.setFont(font)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.label_19 = QtGui.QLabel(self.tab_3)
        self.label_19.setGeometry(QtCore.QRect(10, 80, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_19.setFont(font)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.label_20 = QtGui.QLabel(self.tab_3)
        self.label_20.setGeometry(QtCore.QRect(10, 200, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_20.setFont(font)
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.lineEdit_18 = QtGui.QLineEdit(self.tab_3)
        self.lineEdit_18.setGeometry(QtCore.QRect(90, 140, 171, 20))
        self.lineEdit_18.setStyleSheet(_fromUtf8("color : rgb(0, 0, 0)\n"
""))
        self.lineEdit_18.setReadOnly(False)
        self.lineEdit_18.setObjectName(_fromUtf8("lineEdit_18"))
        self.comboBox = QtGui.QComboBox(self.tab_3)
        self.comboBox.setGeometry(QtCore.QRect(90, 80, 171, 22))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox_2 = QtGui.QComboBox(self.tab_3)
        self.comboBox_2.setGeometry(QtCore.QRect(90, 230, 171, 22))
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_3 = QtGui.QComboBox(self.tab_3)
        self.comboBox_3.setGeometry(QtCore.QRect(90, 170, 171, 22))
        self.comboBox_3.setObjectName(_fromUtf8("comboBox_3"))
        self.label_22 = QtGui.QLabel(self.tab_3)
        self.label_22.setGeometry(QtCore.QRect(10, 260, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_22.setFont(font)
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.lineEdit_12 = QtGui.QLineEdit(self.tab_3)
        self.lineEdit_12.setGeometry(QtCore.QRect(90, 260, 171, 20))
        self.lineEdit_12.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdit_12.setObjectName(_fromUtf8("lineEdit_12"))
        self.label_23 = QtGui.QLabel(self.tab_3)
        self.label_23.setGeometry(QtCore.QRect(10, 290, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_23.setFont(font)
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.pushButton_3 = QtGui.QPushButton(self.tab_3)
        self.pushButton_3.setGeometry(QtCore.QRect(90, 290, 171, 23))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.plainTextEdit = QtGui.QPlainTextEdit(self.tab_3)
        self.plainTextEdit.setGeometry(QtCore.QRect(320, 60, 281, 241))
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.pushButton_4 = QtGui.QPushButton(self.tab_3)
        self.pushButton_4.setGeometry(QtCore.QRect(460, 320, 131, 23))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.label_24 = QtGui.QLabel(self.tab_3)
        self.label_24.setGeometry(QtCore.QRect(10, 380, 191, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Cambria"))
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_24.setFont(font)
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.pushButton_5 = QtGui.QPushButton(self.tab_3)
        self.pushButton_5.setGeometry(QtCore.QRect(30, 420, 191, 23))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.pushButton_6 = QtGui.QPushButton(self.tab_3)
        self.pushButton_6.setGeometry(QtCore.QRect(350, 420, 191, 23))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.label_25 = QtGui.QLabel(self.tab_4)
        self.label_25.setGeometry(QtCore.QRect(10, 20, 121, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Cambria"))
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_25.setFont(font)
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.line_3 = QtGui.QFrame(self.tab_4)
        self.line_3.setGeometry(QtCore.QRect(-20, 40, 641, 21))
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.label_26 = QtGui.QLabel(self.tab_4)
        self.label_26.setGeometry(QtCore.QRect(140, 90, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_26.setFont(font)
        self.label_26.setObjectName(_fromUtf8("label_26"))
        self.label_27 = QtGui.QLabel(self.tab_4)
        self.label_27.setGeometry(QtCore.QRect(140, 130, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_27.setFont(font)
        self.label_27.setObjectName(_fromUtf8("label_27"))
        self.label_28 = QtGui.QLabel(self.tab_4)
        self.label_28.setGeometry(QtCore.QRect(140, 170, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_28.setFont(font)
        self.label_28.setObjectName(_fromUtf8("label_28"))
        self.label_29 = QtGui.QLabel(self.tab_4)
        self.label_29.setGeometry(QtCore.QRect(140, 210, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_29.setFont(font)
        self.label_29.setObjectName(_fromUtf8("label_29"))
        self.label_30 = QtGui.QLabel(self.tab_4)
        self.label_30.setGeometry(QtCore.QRect(140, 250, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_30.setFont(font)
        self.label_30.setObjectName(_fromUtf8("label_30"))
        self.label_31 = QtGui.QLabel(self.tab_4)
        self.label_31.setGeometry(QtCore.QRect(140, 290, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_31.setFont(font)
        self.label_31.setObjectName(_fromUtf8("label_31"))
        self.comboBox_4 = QtGui.QComboBox(self.tab_4)
        self.comboBox_4.setGeometry(QtCore.QRect(290, 90, 181, 22))
        self.comboBox_4.setObjectName(_fromUtf8("comboBox_4"))
        self.spinBox = QtGui.QSpinBox(self.tab_4)
        self.spinBox.setGeometry(QtCore.QRect(290, 130, 181, 22))
        self.spinBox.setMaximum(1000000000)
        self.spinBox.setSingleStep(500)
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.spinBox_2 = QtGui.QSpinBox(self.tab_4)
        self.spinBox_2.setGeometry(QtCore.QRect(290, 170, 181, 22))
        self.spinBox_2.setMaximum(1000000000)
        self.spinBox_2.setSingleStep(500)
        self.spinBox_2.setObjectName(_fromUtf8("spinBox_2"))
        self.spinBox_3 = QtGui.QSpinBox(self.tab_4)
        self.spinBox_3.setGeometry(QtCore.QRect(290, 210, 181, 22))
        self.spinBox_3.setMaximum(1000000000)
        self.spinBox_3.setSingleStep(500)
        self.spinBox_3.setObjectName(_fromUtf8("spinBox_3"))
        self.spinBox_4 = QtGui.QSpinBox(self.tab_4)
        self.spinBox_4.setGeometry(QtCore.QRect(290, 250, 181, 22))
        self.spinBox_4.setMaximum(1000000000)
        self.spinBox_4.setSingleStep(500)
        self.spinBox_4.setObjectName(_fromUtf8("spinBox_4"))
        self.spinBox_5 = QtGui.QSpinBox(self.tab_4)
        self.spinBox_5.setGeometry(QtCore.QRect(290, 290, 181, 22))
        self.spinBox_5.setMaximum(1000000000)
        self.spinBox_5.setSingleStep(500)
        self.spinBox_5.setObjectName(_fromUtf8("spinBox_5"))
        self.pushButton_7 = QtGui.QPushButton(self.tab_4)
        self.pushButton_7.setGeometry(QtCore.QRect(150, 370, 331, 23))
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.tabWidget.addTab(self.tab_4, _fromUtf8(""))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.line_4 = QtGui.QFrame(self.tab)
        self.line_4.setGeometry(QtCore.QRect(-10, 40, 641, 21))
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.label_32 = QtGui.QLabel(self.tab)
        self.label_32.setGeometry(QtCore.QRect(20, 20, 121, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Cambria"))
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_32.setFont(font)
        self.label_32.setObjectName(_fromUtf8("label_32"))
        self.label_33 = QtGui.QLabel(self.tab)
        self.label_33.setGeometry(QtCore.QRect(30, 80, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_33.setFont(font)
        self.label_33.setObjectName(_fromUtf8("label_33"))
        self.label_34 = QtGui.QLabel(self.tab)
        self.label_34.setGeometry(QtCore.QRect(30, 120, 171, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_34.setFont(font)
        self.label_34.setObjectName(_fromUtf8("label_34"))
        self.label_35 = QtGui.QLabel(self.tab)
        self.label_35.setGeometry(QtCore.QRect(30, 200, 191, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_35.setFont(font)
        self.label_35.setObjectName(_fromUtf8("label_35"))
        self.label_36 = QtGui.QLabel(self.tab)
        self.label_36.setGeometry(QtCore.QRect(30, 240, 191, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_36.setFont(font)
        self.label_36.setObjectName(_fromUtf8("label_36"))
        self.label_37 = QtGui.QLabel(self.tab)
        self.label_37.setGeometry(QtCore.QRect(30, 280, 181, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_37.setFont(font)
        self.label_37.setObjectName(_fromUtf8("label_37"))
        self.label_38 = QtGui.QLabel(self.tab)
        self.label_38.setGeometry(QtCore.QRect(30, 160, 201, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_38.setFont(font)
        self.label_38.setObjectName(_fromUtf8("label_38"))
        self.label_39 = QtGui.QLabel(self.tab)
        self.label_39.setGeometry(QtCore.QRect(30, 320, 181, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_39.setFont(font)
        self.label_39.setObjectName(_fromUtf8("label_39"))
        self.spinBox_6 = QtGui.QSpinBox(self.tab)
        self.spinBox_6.setGeometry(QtCore.QRect(380, 320, 101, 22))
        self.spinBox_6.setObjectName(_fromUtf8("spinBox_6"))
        self.label_40 = QtGui.QLabel(self.tab)
        self.label_40.setGeometry(QtCore.QRect(280, 80, 211, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_40.setFont(font)
        self.label_40.setObjectName(_fromUtf8("label_40"))
        self.label_41 = QtGui.QLabel(self.tab)
        self.label_41.setGeometry(QtCore.QRect(280, 120, 211, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_41.setFont(font)
        self.label_41.setObjectName(_fromUtf8("label_41"))
        self.label_42 = QtGui.QLabel(self.tab)
        self.label_42.setGeometry(QtCore.QRect(280, 160, 211, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_42.setFont(font)
        self.label_42.setObjectName(_fromUtf8("label_42"))
        self.label_43 = QtGui.QLabel(self.tab)
        self.label_43.setGeometry(QtCore.QRect(280, 200, 211, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_43.setFont(font)
        self.label_43.setObjectName(_fromUtf8("label_43"))
        self.label_44 = QtGui.QLabel(self.tab)
        self.label_44.setGeometry(QtCore.QRect(280, 240, 211, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_44.setFont(font)
        self.label_44.setObjectName(_fromUtf8("label_44"))
        self.label_45 = QtGui.QLabel(self.tab)
        self.label_45.setGeometry(QtCore.QRect(280, 280, 211, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_45.setFont(font)
        self.label_45.setObjectName(_fromUtf8("label_45"))
        self.label_46 = QtGui.QLabel(self.tab)
        self.label_46.setGeometry(QtCore.QRect(30, 380, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_46.setFont(font)
        self.label_46.setObjectName(_fromUtf8("label_46"))
        self.pushButton_8 = QtGui.QPushButton(self.tab)
        self.pushButton_8.setGeometry(QtCore.QRect(500, 320, 111, 23))
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
        self.label_47 = QtGui.QLabel(self.tab)
        self.label_47.setGeometry(QtCore.QRect(280, 320, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_47.setFont(font)
        self.label_47.setObjectName(_fromUtf8("label_47"))
        self.label_48 = QtGui.QLabel(self.tab)
        self.label_48.setGeometry(QtCore.QRect(280, 380, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_48.setFont(font)
        self.label_48.setObjectName(_fromUtf8("label_48"))
        self.line_5 = QtGui.QFrame(self.tab)
        self.line_5.setGeometry(QtCore.QRect(-10, 350, 641, 20))
        self.line_5.setFrameShape(QtGui.QFrame.HLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "HMS - HMC Portal", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("Form", "Home", None))
        self.label_2.setText(_translate("Form", "Add New Hall", None))
        self.groupBox.setTitle(_translate("Form", "Basic Information", None))
        self.label_3.setText(_translate("Form", "Name", None))
        self.label_4.setText(_translate("Form", "Status", None))
        self.label_5.setText(_translate("Form", "ID", None))
        self.groupBox_2.setTitle(_translate("Form", "Room Information", None))
        self.label_6.setText(_translate("Form", "Single Room Count", None))
        self.label_7.setText(_translate("Form", "Double Room Count", None))
        self.label_8.setText(_translate("Form", "Single Room Rent", None))
        self.label_9.setText(_translate("Form", "Double Room Rent", None))
        self.groupBox_3.setTitle(_translate("Form", "Warden and Mess Manager", None))
        self.label_10.setText(_translate("Form", "Warden Name", None))
        self.label_11.setText(_translate("Form", "Warden Password", None))
        self.label_12.setText(_translate("Form", "Manager Name", None))
        self.label_13.setText(_translate("Form", "Manager Password", None))
        self.pushButton.setText(_translate("Form", "Setup Hall", None))
        self.pushButton_2.setText(_translate("Form", "Cancel", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "Add Hall", None))
        self.label_14.setText(_translate("Form", "Grant Admission", None))
        self.label_21.setText(_translate("Form", "Contact No.", None))
        self.label_17.setText(_translate("Form", "Hall Alloted", None))
        self.label_15.setText(_translate("Form", "Room Type", None))
        self.label_16.setText(_translate("Form", "Address", None))
        self.label_18.setText(_translate("Form", "Name", None))
        self.label_19.setText(_translate("Form", "Gender", None))
        self.label_20.setText(_translate("Form", "Room No.", None))
        self.comboBox.setItemText(0, _translate("Form", "Male", None))
        self.comboBox.setItemText(1, _translate("Form", "Female", None))
        self.comboBox.setItemText(2, _translate("Form", "Other", None))
        self.comboBox_2.setItemText(0, _translate("Form", "Single", None))
        self.comboBox_2.setItemText(1, _translate("Form", "Double", None))
        self.label_22.setText(_translate("Form", "Password", None))
        self.label_23.setText(_translate("Form", "Photograph", None))
        self.pushButton_3.setText(_translate("Form", "Upload Photo", None))
        self.pushButton_4.setText(_translate("Form", "Issue Admission Letter", None))
        self.label_24.setText(_translate("Form", "Student Due Payment ", None))
        self.pushButton_5.setText(_translate("Form", "Activate Payment Link", None))
        self.pushButton_6.setText(_translate("Form", "Deactivate Payment Link", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Form", "Student Functions", None))
        self.label_25.setText(_translate("Form", "Issue Grants", None))
        self.label_26.setText(_translate("Form", "Hall", None))
        self.label_27.setText(_translate("Form", "Mess Grant", None))
        self.label_28.setText(_translate("Form", "Amenity Grant", None))
        self.label_29.setText(_translate("Form", "Salary Grant", None))
        self.label_30.setText(_translate("Form", "Repair Grant", None))
        self.label_31.setText(_translate("Form", "Misc Grant", None))
        self.pushButton_7.setText(_translate("Form", "Issue Grant", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Form", "Issue Grant", None))
        self.label_32.setText(_translate("Form", "Finances", None))
        self.label_33.setText(_translate("Form", "Grant from Institute", None))
        self.label_34.setText(_translate("Form", "Mess Grant Expenditure", None))
        self.label_35.setText(_translate("Form", "Salary Grant Expenditure", None))
        self.label_36.setText(_translate("Form", "Repair Grant Expenditure", None))
        self.label_37.setText(_translate("Form", "Misc Grant Expenditure", None))
        self.label_38.setText(_translate("Form", "Amenity Grant Expenditure", None))
        self.label_39.setText(_translate("Form", "HMC - Misc Expenses", None))
        self.label_40.setText(_translate("Form", "Sample", None))
        self.label_41.setText(_translate("Form", "Sample", None))
        self.label_42.setText(_translate("Form", "Sample", None))
        self.label_43.setText(_translate("Form", "Sample", None))
        self.label_44.setText(_translate("Form", "Sample", None))
        self.label_45.setText(_translate("Form", "Sample", None))
        self.label_46.setText(_translate("Form", "BALANCE", None))
        self.pushButton_8.setText(_translate("Form", "Add", None))
        self.label_47.setText(_translate("Form", "Sample", None))
        self.label_48.setText(_translate("Form", "Sample", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "HMC Finances", None))

