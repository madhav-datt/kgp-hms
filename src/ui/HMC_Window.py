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
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../../../../.designer/backup/logo2.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.stackedWidget = QtGui.QStackedWidget(Form)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 631, 501))
        self.stackedWidget.setObjectName(_fromUtf8("stackedWidget"))
        self.page = QtGui.QWidget()
        self.page.setObjectName(_fromUtf8("page"))
        self.tabWidget = QtGui.QTabWidget(self.page)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 631, 501))
        self.tabWidget.setTabPosition(QtGui.QTabWidget.North)
        self.tabWidget.setTabShape(QtGui.QTabWidget.Rounded)
        self.tabWidget.setIconSize(QtCore.QSize(16, 16))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_1 = QtGui.QWidget()
        self.tab_1.setObjectName(_fromUtf8("tab_1"))
        self.label_33 = QtGui.QLabel(self.tab_1)
        self.label_33.setGeometry(QtCore.QRect(0, 50, 621, 421))
        self.label_33.setObjectName(_fromUtf8("label_33"))
        self.label_34 = QtGui.QLabel(self.tab_1)
        self.label_34.setGeometry(QtCore.QRect(20, 10, 191, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Cambria"))
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_34.setFont(font)
        self.label_34.setObjectName(_fromUtf8("label_34"))
        self.line_4 = QtGui.QFrame(self.tab_1)
        self.line_4.setGeometry(QtCore.QRect(0, 30, 631, 20))
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
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
        self.groupBox.setGeometry(QtCore.QRect(20, 90, 281, 131))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 30, 46, 13))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(10, 60, 46, 13))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.lineEdit_2 = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(100, 30, 171, 20))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.comboBox_4 = QtGui.QComboBox(self.groupBox)
        self.comboBox_4.setGeometry(QtCore.QRect(100, 60, 171, 22))
        self.comboBox_4.setObjectName(_fromUtf8("comboBox_4"))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.comboBox_4.addItem(_fromUtf8(""))
        self.label_54 = QtGui.QLabel(self.groupBox)
        self.label_54.setGeometry(QtCore.QRect(10, 90, 81, 16))
        self.label_54.setObjectName(_fromUtf8("label_54"))
        self.doubleSpinBox_5 = QtGui.QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox_5.setGeometry(QtCore.QRect(100, 90, 171, 22))
        self.doubleSpinBox_5.setMaximum(10000000.99)
        self.doubleSpinBox_5.setSingleStep(1000.0)
        self.doubleSpinBox_5.setObjectName(_fromUtf8("doubleSpinBox_5"))
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
        self.spinBox_8 = QtGui.QSpinBox(self.groupBox_2)
        self.spinBox_8.setGeometry(QtCore.QRect(120, 30, 161, 22))
        self.spinBox_8.setMaximum(1000)
        self.spinBox_8.setObjectName(_fromUtf8("spinBox_8"))
        self.doubleSpinBox = QtGui.QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox.setGeometry(QtCore.QRect(120, 60, 161, 22))
        self.doubleSpinBox.setMaximum(10000000.99)
        self.doubleSpinBox.setSingleStep(1000.0)
        self.doubleSpinBox.setObjectName(_fromUtf8("doubleSpinBox"))
        self.spinBox_9 = QtGui.QSpinBox(self.groupBox_2)
        self.spinBox_9.setGeometry(QtCore.QRect(120, 90, 161, 22))
        self.spinBox_9.setMaximum(1000)
        self.spinBox_9.setObjectName(_fromUtf8("spinBox_9"))
        self.doubleSpinBox_2 = QtGui.QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_2.setGeometry(QtCore.QRect(120, 120, 161, 22))
        self.doubleSpinBox_2.setMaximum(10000000.99)
        self.doubleSpinBox_2.setSingleStep(1000.0)
        self.doubleSpinBox_2.setObjectName(_fromUtf8("doubleSpinBox_2"))
        self.groupBox_3 = QtGui.QGroupBox(self.tab_2)
        self.groupBox_3.setGeometry(QtCore.QRect(330, 90, 281, 271))
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
        self.lineEdit_9.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdit_9.setObjectName(_fromUtf8("lineEdit_9"))
        self.lineEdit_10 = QtGui.QLineEdit(self.groupBox_3)
        self.lineEdit_10.setGeometry(QtCore.QRect(110, 90, 161, 20))
        self.lineEdit_10.setObjectName(_fromUtf8("lineEdit_10"))
        self.lineEdit_11 = QtGui.QLineEdit(self.groupBox_3)
        self.lineEdit_11.setGeometry(QtCore.QRect(110, 120, 161, 20))
        self.lineEdit_11.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdit_11.setObjectName(_fromUtf8("lineEdit_11"))
        self.label_26 = QtGui.QLabel(self.groupBox_3)
        self.label_26.setGeometry(QtCore.QRect(10, 180, 71, 16))
        self.label_26.setObjectName(_fromUtf8("label_26"))
        self.label_51 = QtGui.QLabel(self.groupBox_3)
        self.label_51.setGeometry(QtCore.QRect(10, 210, 81, 16))
        self.label_51.setObjectName(_fromUtf8("label_51"))
        self.lineEdit_14 = QtGui.QLineEdit(self.groupBox_3)
        self.lineEdit_14.setGeometry(QtCore.QRect(110, 180, 161, 20))
        self.lineEdit_14.setObjectName(_fromUtf8("lineEdit_14"))
        self.label_52 = QtGui.QLabel(self.groupBox_3)
        self.label_52.setGeometry(QtCore.QRect(10, 150, 91, 16))
        self.label_52.setObjectName(_fromUtf8("label_52"))
        self.doubleSpinBox_3 = QtGui.QDoubleSpinBox(self.groupBox_3)
        self.doubleSpinBox_3.setGeometry(QtCore.QRect(110, 150, 161, 22))
        self.doubleSpinBox_3.setMaximum(10000000.99)
        self.doubleSpinBox_3.setSingleStep(1000.0)
        self.doubleSpinBox_3.setObjectName(_fromUtf8("doubleSpinBox_3"))
        self.lineEdit_17 = QtGui.QLineEdit(self.groupBox_3)
        self.lineEdit_17.setGeometry(QtCore.QRect(110, 210, 161, 20))
        self.lineEdit_17.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdit_17.setObjectName(_fromUtf8("lineEdit_17"))
        self.label_53 = QtGui.QLabel(self.groupBox_3)
        self.label_53.setGeometry(QtCore.QRect(10, 240, 81, 16))
        self.label_53.setObjectName(_fromUtf8("label_53"))
        self.doubleSpinBox_4 = QtGui.QDoubleSpinBox(self.groupBox_3)
        self.doubleSpinBox_4.setGeometry(QtCore.QRect(110, 240, 161, 22))
        self.doubleSpinBox_4.setMaximum(10000000.99)
        self.doubleSpinBox_4.setSingleStep(1000.0)
        self.doubleSpinBox_4.setObjectName(_fromUtf8("doubleSpinBox_4"))
        self.pushButton = QtGui.QPushButton(self.tab_2)
        self.pushButton.setGeometry(QtCore.QRect(370, 410, 211, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.tab_2)
        self.pushButton_2.setGeometry(QtCore.QRect(370, 440, 211, 23))
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
        self.label_21.setGeometry(QtCore.QRect(10, 120, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_21.setFont(font)
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.lineEdit_13 = QtGui.QLineEdit(self.tab_3)
        self.lineEdit_13.setGeometry(QtCore.QRect(90, 210, 171, 20))
        self.lineEdit_13.setStyleSheet(_fromUtf8("color : rgb(0, 0, 0)"))
        self.lineEdit_13.setReadOnly(False)
        self.lineEdit_13.setObjectName(_fromUtf8("lineEdit_13"))
        self.label_17 = QtGui.QLabel(self.tab_3)
        self.label_17.setGeometry(QtCore.QRect(10, 180, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_17.setFont(font)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.lineEdit_15 = QtGui.QLineEdit(self.tab_3)
        self.lineEdit_15.setGeometry(QtCore.QRect(90, 120, 171, 20))
        self.lineEdit_15.setStyleSheet(_fromUtf8("color : rgb(0,0,0)\n"
""))
        self.lineEdit_15.setReadOnly(False)
        self.lineEdit_15.setObjectName(_fromUtf8("lineEdit_15"))
        self.lineEdit_16 = QtGui.QLineEdit(self.tab_3)
        self.lineEdit_16.setGeometry(QtCore.QRect(90, 60, 171, 20))
        self.lineEdit_16.setStyleSheet(_fromUtf8("color : rgb(0, 0, 0)"))
        self.lineEdit_16.setReadOnly(False)
        self.lineEdit_16.setPlaceholderText(_fromUtf8(""))
        self.lineEdit_16.setObjectName(_fromUtf8("lineEdit_16"))
        self.label_15 = QtGui.QLabel(self.tab_3)
        self.label_15.setGeometry(QtCore.QRect(10, 240, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_15.setFont(font)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.label_16 = QtGui.QLabel(self.tab_3)
        self.label_16.setGeometry(QtCore.QRect(10, 150, 46, 13))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_16.setFont(font)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.label_18 = QtGui.QLabel(self.tab_3)
        self.label_18.setGeometry(QtCore.QRect(10, 60, 46, 13))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_18.setFont(font)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.label_19 = QtGui.QLabel(self.tab_3)
        self.label_19.setGeometry(QtCore.QRect(10, 90, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_19.setFont(font)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.label_20 = QtGui.QLabel(self.tab_3)
        self.label_20.setGeometry(QtCore.QRect(10, 210, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_20.setFont(font)
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.lineEdit_18 = QtGui.QLineEdit(self.tab_3)
        self.lineEdit_18.setGeometry(QtCore.QRect(90, 150, 171, 20))
        self.lineEdit_18.setStyleSheet(_fromUtf8("color : rgb(0, 0, 0)\n"
""))
        self.lineEdit_18.setReadOnly(False)
        self.lineEdit_18.setObjectName(_fromUtf8("lineEdit_18"))
        self.comboBox = QtGui.QComboBox(self.tab_3)
        self.comboBox.setGeometry(QtCore.QRect(90, 90, 171, 22))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox_2 = QtGui.QComboBox(self.tab_3)
        self.comboBox_2.setGeometry(QtCore.QRect(90, 240, 171, 22))
        self.comboBox_2.setObjectName(_fromUtf8("comboBox_2"))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_2.addItem(_fromUtf8(""))
        self.comboBox_3 = QtGui.QComboBox(self.tab_3)
        self.comboBox_3.setGeometry(QtCore.QRect(90, 180, 171, 22))
        self.comboBox_3.setObjectName(_fromUtf8("comboBox_3"))
        self.label_22 = QtGui.QLabel(self.tab_3)
        self.label_22.setGeometry(QtCore.QRect(10, 270, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_22.setFont(font)
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.lineEdit_12 = QtGui.QLineEdit(self.tab_3)
        self.lineEdit_12.setGeometry(QtCore.QRect(90, 270, 171, 20))
        self.lineEdit_12.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdit_12.setObjectName(_fromUtf8("lineEdit_12"))
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
        self.label_29 = QtGui.QLabel(self.tab_4)
        self.label_29.setGeometry(QtCore.QRect(30, 280, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_29.setFont(font)
        self.label_29.setObjectName(_fromUtf8("label_29"))
        self.label_30 = QtGui.QLabel(self.tab_4)
        self.label_30.setGeometry(QtCore.QRect(30, 330, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_30.setFont(font)
        self.label_30.setObjectName(_fromUtf8("label_30"))
        self.pushButton_7 = QtGui.QPushButton(self.tab_4)
        self.pushButton_7.setGeometry(QtCore.QRect(30, 430, 281, 23))
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.label_49 = QtGui.QLabel(self.tab_4)
        self.label_49.setGeometry(QtCore.QRect(30, 390, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_49.setFont(font)
        self.label_49.setObjectName(_fromUtf8("label_49"))
        self.groupBox_4 = QtGui.QGroupBox(self.tab_4)
        self.groupBox_4.setGeometry(QtCore.QRect(340, 260, 271, 161))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.label_31 = QtGui.QLabel(self.groupBox_4)
        self.label_31.setGeometry(QtCore.QRect(10, 30, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_31.setFont(font)
        self.label_31.setObjectName(_fromUtf8("label_31"))
        self.lineEdit = QtGui.QLineEdit(self.groupBox_4)
        self.lineEdit.setGeometry(QtCore.QRect(120, 30, 141, 20))
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label_55 = QtGui.QLabel(self.groupBox_4)
        self.label_55.setGeometry(QtCore.QRect(10, 70, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_55.setFont(font)
        self.label_55.setObjectName(_fromUtf8("label_55"))
        self.lineEdit_3 = QtGui.QLineEdit(self.groupBox_4)
        self.lineEdit_3.setGeometry(QtCore.QRect(120, 70, 141, 20))
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.label_56 = QtGui.QLabel(self.groupBox_4)
        self.label_56.setGeometry(QtCore.QRect(10, 110, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_56.setFont(font)
        self.label_56.setObjectName(_fromUtf8("label_56"))
        self.lineEdit_4 = QtGui.QLineEdit(self.groupBox_4)
        self.lineEdit_4.setGeometry(QtCore.QRect(120, 110, 141, 20))
        self.lineEdit_4.setReadOnly(True)
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.pushButton_9 = QtGui.QPushButton(self.tab_4)
        self.pushButton_9.setGeometry(QtCore.QRect(340, 430, 281, 23))
        self.pushButton_9.setObjectName(_fromUtf8("pushButton_9"))
        self.doubleSpinBox_6 = QtGui.QDoubleSpinBox(self.tab_4)
        self.doubleSpinBox_6.setGeometry(QtCore.QRect(140, 280, 151, 22))
        self.doubleSpinBox_6.setMaximum(10000000.99)
        self.doubleSpinBox_6.setSingleStep(1000.0)
        self.doubleSpinBox_6.setObjectName(_fromUtf8("doubleSpinBox_6"))
        self.doubleSpinBox_7 = QtGui.QDoubleSpinBox(self.tab_4)
        self.doubleSpinBox_7.setGeometry(QtCore.QRect(140, 330, 151, 22))
        self.doubleSpinBox_7.setMaximum(10000000.99)
        self.doubleSpinBox_7.setSingleStep(1000.0)
        self.doubleSpinBox_7.setObjectName(_fromUtf8("doubleSpinBox_7"))
        self.doubleSpinBox_8 = QtGui.QDoubleSpinBox(self.tab_4)
        self.doubleSpinBox_8.setGeometry(QtCore.QRect(140, 390, 151, 22))
        self.doubleSpinBox_8.setMaximum(10000000.99)
        self.doubleSpinBox_8.setSingleStep(1000.0)
        self.doubleSpinBox_8.setObjectName(_fromUtf8("doubleSpinBox_8"))
        self.listWidget = QtGui.QListWidget(self.tab_4)
        self.listWidget.setGeometry(QtCore.QRect(210, 80, 221, 101))
        self.listWidget.setViewMode(QtGui.QListView.ListMode)
        self.listWidget.setUniformItemSizes(False)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        item = QtGui.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        self.listWidget.addItem(item)
        item = QtGui.QListWidgetItem()
        self.listWidget.addItem(item)
        self.label_5 = QtGui.QLabel(self.tab_4)
        self.label_5.setGeometry(QtCore.QRect(260, 60, 121, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_23 = QtGui.QLabel(self.tab_4)
        self.label_23.setGeometry(QtCore.QRect(260, 230, 121, 20))
        self.label_23.setText(_fromUtf8(""))
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.pushButton_3 = QtGui.QPushButton(self.tab_4)
        self.pushButton_3.setGeometry(QtCore.QRect(260, 190, 121, 23))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.tabWidget.addTab(self.tab_4, _fromUtf8(""))
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtGui.QWidget()
        self.page_2.setObjectName(_fromUtf8("page_2"))
        self.label_27 = QtGui.QLabel(self.page_2)
        self.label_27.setGeometry(QtCore.QRect(170, 200, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_27.setFont(font)
        self.label_27.setStyleSheet(_fromUtf8("color : rgb(255, 255, 255)"))
        self.label_27.setObjectName(_fromUtf8("label_27"))
        self.lineEdit_5 = QtGui.QLineEdit(self.page_2)
        self.lineEdit_5.setGeometry(QtCore.QRect(310, 200, 161, 20))
        self.lineEdit_5.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.pushButton_8 = QtGui.QPushButton(self.page_2)
        self.pushButton_8.setGeometry(QtCore.QRect(220, 250, 171, 23))
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
        self.label_28 = QtGui.QLabel(self.page_2)
        self.label_28.setGeometry(QtCore.QRect(120, 300, 491, 20))
        self.label_28.setStyleSheet(_fromUtf8("color : rgb(255, 255, 255)"))
        self.label_28.setText(_fromUtf8(""))
        self.label_28.setObjectName(_fromUtf8("label_28"))
        self.label_32 = QtGui.QLabel(self.page_2)
        self.label_32.setGeometry(QtCore.QRect(5, 2, 621, 491))
        self.label_32.setObjectName(_fromUtf8("label_32"))
        self.label_32.raise_()
        self.label_27.raise_()
        self.lineEdit_5.raise_()
        self.pushButton_8.raise_()
        self.label_28.raise_()
        self.stackedWidget.addWidget(self.page_2)

        self.retranslateUi(Form)
        self.stackedWidget.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "HMS - HMC Portal", None))
        self.label_33.setText(_translate("Form", "TextLabel", None))
        self.label_34.setText(_translate("Form", "WELCOME!", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("Form", "Home", None))
        self.label_2.setText(_translate("Form", "Add New Hall", None))
        self.groupBox.setTitle(_translate("Form", "Basic Information", None))
        self.label_3.setText(_translate("Form", "Name", None))
        self.label_4.setText(_translate("Form", "Status", None))
        self.comboBox_4.setItemText(0, _translate("Form", "Old", None))
        self.comboBox_4.setItemText(1, _translate("Form", "New", None))
        self.label_54.setText(_translate("Form", "Amenity Charge", None))
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
        self.label_26.setText(_translate("Form", "Clerk Name", None))
        self.label_51.setText(_translate("Form", "Clerk Password", None))
        self.label_52.setText(_translate("Form", "Manager Salary", None))
        self.label_53.setText(_translate("Form", "Clerk Salary", None))
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
        self.pushButton_4.setText(_translate("Form", "Issue Admission Letter", None))
        self.label_24.setText(_translate("Form", "Student Due Payment ", None))
        self.pushButton_5.setText(_translate("Form", "Activate Payment Link", None))
        self.pushButton_6.setText(_translate("Form", "Deactivate Payment Link", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Form", "Student Functions", None))
        self.label_25.setText(_translate("Form", "Issue Grants", None))
        self.label_29.setText(_translate("Form", "Salary Grant", None))
        self.label_30.setText(_translate("Form", "Repair Grant", None))
        self.pushButton_7.setText(_translate("Form", "Issue Grant", None))
        self.label_49.setText(_translate("Form", "Misc. Grant", None))
        self.groupBox_4.setTitle(_translate("Form", "Warden\'s Request Grant", None))
        self.label_31.setText(_translate("Form", "Salary Grant", None))
        self.label_55.setText(_translate("Form", "Repair Grant", None))
        self.label_56.setText(_translate("Form", "Misc Grant", None))
        self.pushButton_9.setText(_translate("Form", "Reject Grant", None))
        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        item = self.listWidget.item(0)
        item.setText(_translate("Form", "Model 1", None))
        item = self.listWidget.item(1)
        item.setText(_translate("Form", "Model 2", None))
        item = self.listWidget.item(2)
        item.setText(_translate("Form", "Model 3", None))
        self.listWidget.setSortingEnabled(__sortingEnabled)
        self.label_5.setText(_translate("Form", "Requests from Halls", None))
        self.pushButton_3.setText(_translate("Form", "View Request", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Form", "Issue Grant", None))
        self.label_27.setText(_translate("Form", "Password", None))
        self.pushButton_8.setText(_translate("Form", "Login", None))
        self.label_32.setText(_translate("Form", "TextLabel", None))

