# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'warden.ui'
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
        Form.resize(709, 455)
        self.stackedWidget = QtGui.QStackedWidget(Form)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 701, 461))
        self.stackedWidget.setObjectName(_fromUtf8("stackedWidget"))
        self.page = QtGui.QWidget()
        self.page.setObjectName(_fromUtf8("page"))
        self.tabWidget = QtGui.QTabWidget(self.page)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 711, 461))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.label_33 = QtGui.QLabel(self.tab)
        self.label_33.setGeometry(QtCore.QRect(10, 20, 201, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Cambria"))
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_33.setFont(font)
        self.label_33.setStyleSheet(_fromUtf8("color : rgb(255, 255, 255)"))
        self.label_33.setObjectName(_fromUtf8("label_33"))
        self.label_6 = QtGui.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(0, 0, 701, 431))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_6.raise_()
        self.label_33.raise_()
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_7 = QtGui.QWidget()
        self.tab_7.setObjectName(_fromUtf8("tab_7"))
        self.label_8 = QtGui.QLabel(self.tab_7)
        self.label_8.setGeometry(QtCore.QRect(60, 60, 121, 20))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet(_fromUtf8("color : rgb(255, 255, 255)"))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_48 = QtGui.QLabel(self.tab_7)
        self.label_48.setGeometry(QtCore.QRect(10, 10, 201, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Cambria"))
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label_48.setFont(font)
        self.label_48.setStyleSheet(_fromUtf8("color : rgb(255, 255, 255)"))
        self.label_48.setObjectName(_fromUtf8("label_48"))
        self.line_3 = QtGui.QFrame(self.tab_7)
        self.line_3.setGeometry(QtCore.QRect(0, 40, 701, 21))
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.label_49 = QtGui.QLabel(self.tab_7)
        self.label_49.setGeometry(QtCore.QRect(70, 250, 121, 20))
        self.label_49.setText(_fromUtf8(""))
        self.label_49.setObjectName(_fromUtf8("label_49"))
        self.listWidget = QtGui.QListWidget(self.tab_7)
        self.listWidget.setGeometry(QtCore.QRect(10, 90, 221, 101))
        self.listWidget.setViewMode(QtGui.QListView.ListMode)
        self.listWidget.setUniformItemSizes(False)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.pushButton_7 = QtGui.QPushButton(self.tab_7)
        self.pushButton_7.setGeometry(QtCore.QRect(60, 210, 121, 23))
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.label_50 = QtGui.QLabel(self.tab_7)
        self.label_50.setGeometry(QtCore.QRect(308, 60, 64, 20))
        self.label_50.setStyleSheet(_fromUtf8("color : rgb(255, 255, 255)"))
        self.label_50.setObjectName(_fromUtf8("label_50"))
        self.lineEdit_23 = QtGui.QLineEdit(self.tab_7)
        self.lineEdit_23.setGeometry(QtCore.QRect(470, 100, 204, 20))
        self.lineEdit_23.setReadOnly(True)
        self.lineEdit_23.setObjectName(_fromUtf8("lineEdit_23"))
        self.label_51 = QtGui.QLabel(self.tab_7)
        self.label_51.setGeometry(QtCore.QRect(310, 100, 52, 20))
        self.label_51.setStyleSheet(_fromUtf8("color : rgb(255, 255, 255)"))
        self.label_51.setObjectName(_fromUtf8("label_51"))
        self.label_52 = QtGui.QLabel(self.tab_7)
        self.label_52.setGeometry(QtCore.QRect(310, 160, 103, 22))
        self.label_52.setStyleSheet(_fromUtf8("color : rgb(255, 255, 255)"))
        self.label_52.setObjectName(_fromUtf8("label_52"))
        self.label_53 = QtGui.QLabel(self.tab_7)
        self.label_53.setGeometry(QtCore.QRect(310, 270, 151, 22))
        self.label_53.setStyleSheet(_fromUtf8("color : rgb(255, 255, 255)"))
        self.label_53.setObjectName(_fromUtf8("label_53"))
        self.plainTextEdit = QtGui.QPlainTextEdit(self.tab_7)
        self.plainTextEdit.setGeometry(QtCore.QRect(480, 270, 204, 111))
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.lineEdit_15 = QtGui.QLineEdit(self.tab_7)
        self.lineEdit_15.setGeometry(QtCore.QRect(470, 60, 204, 20))
        self.lineEdit_15.setReadOnly(True)
        self.lineEdit_15.setObjectName(_fromUtf8("lineEdit_15"))
        self.plainTextEdit_2 = QtGui.QPlainTextEdit(self.tab_7)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(480, 160, 204, 81))
        self.plainTextEdit_2.setReadOnly(True)
        self.plainTextEdit_2.setObjectName(_fromUtf8("plainTextEdit_2"))
        self.line_2 = QtGui.QFrame(self.tab_7)
        self.line_2.setGeometry(QtCore.QRect(253, 50, 20, 381))
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.pushButton_8 = QtGui.QPushButton(self.tab_7)
        self.pushButton_8.setGeometry(QtCore.QRect(320, 400, 161, 23))
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
        self.label_9 = QtGui.QLabel(self.tab_7)
        self.label_9.setGeometry(QtCore.QRect(0, 0, 701, 431))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_9.raise_()
        self.label_8.raise_()
        self.label_48.raise_()
        self.line_3.raise_()
        self.label_49.raise_()
        self.listWidget.raise_()
        self.pushButton_7.raise_()
        self.label_50.raise_()
        self.lineEdit_23.raise_()
        self.label_51.raise_()
        self.label_52.raise_()
        self.label_53.raise_()
        self.plainTextEdit.raise_()
        self.lineEdit_15.raise_()
        self.plainTextEdit_2.raise_()
        self.line_2.raise_()
        self.pushButton_8.raise_()
        self.tabWidget.addTab(self.tab_7, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.groupBox_4 = QtGui.QGroupBox(self.tab_2)
        self.groupBox_4.setGeometry(QtCore.QRect(30, 60, 331, 131))
        self.groupBox_4.setStyleSheet(_fromUtf8("color : rgb(255, 255, 255)"))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.label_12 = QtGui.QLabel(self.groupBox_4)
        self.label_12.setGeometry(QtCore.QRect(10, 30, 121, 16))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.label_13 = QtGui.QLabel(self.groupBox_4)
        self.label_13.setGeometry(QtCore.QRect(10, 60, 121, 16))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.label_14 = QtGui.QLabel(self.groupBox_4)
        self.label_14.setGeometry(QtCore.QRect(10, 90, 131, 16))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.lineEdit_8 = QtGui.QLineEdit(self.groupBox_4)
        self.lineEdit_8.setGeometry(QtCore.QRect(160, 30, 161, 20))
        self.lineEdit_8.setStyleSheet(_fromUtf8("color : rgb(0, 0, 0)"))
        self.lineEdit_8.setReadOnly(True)
        self.lineEdit_8.setObjectName(_fromUtf8("lineEdit_8"))
        self.lineEdit_9 = QtGui.QLineEdit(self.groupBox_4)
        self.lineEdit_9.setGeometry(QtCore.QRect(160, 60, 161, 20))
        self.lineEdit_9.setStyleSheet(_fromUtf8("color : rgb(0, 0, 0)"))
        self.lineEdit_9.setReadOnly(True)
        self.lineEdit_9.setObjectName(_fromUtf8("lineEdit_9"))
        self.lineEdit_10 = QtGui.QLineEdit(self.groupBox_4)
        self.lineEdit_10.setGeometry(QtCore.QRect(160, 90, 161, 20))
        self.lineEdit_10.setStyleSheet(_fromUtf8("color : rgb(0, 0, 0)"))
        self.lineEdit_10.setReadOnly(True)
        self.lineEdit_10.setObjectName(_fromUtf8("lineEdit_10"))
        self.label = QtGui.QLabel(self.tab_2)
        self.label.setGeometry(QtCore.QRect(0, 0, 701, 431))
        self.label.setObjectName(_fromUtf8("label"))
        self.groupBox_5 = QtGui.QGroupBox(self.tab_2)
        self.groupBox_5.setGeometry(QtCore.QRect(30, 230, 331, 131))
        self.groupBox_5.setStyleSheet(_fromUtf8("color : rgb(255, 255, 255)"))
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.label_21 = QtGui.QLabel(self.groupBox_5)
        self.label_21.setGeometry(QtCore.QRect(10, 30, 121, 16))
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.label_22 = QtGui.QLabel(self.groupBox_5)
        self.label_22.setGeometry(QtCore.QRect(10, 60, 121, 16))
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.label_23 = QtGui.QLabel(self.groupBox_5)
        self.label_23.setGeometry(QtCore.QRect(10, 90, 131, 16))
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.lineEdit_17 = QtGui.QLineEdit(self.groupBox_5)
        self.lineEdit_17.setGeometry(QtCore.QRect(160, 30, 161, 20))
        self.lineEdit_17.setStyleSheet(_fromUtf8("color : rgb(0, 0, 0)"))
        self.lineEdit_17.setReadOnly(True)
        self.lineEdit_17.setObjectName(_fromUtf8("lineEdit_17"))
        self.lineEdit_18 = QtGui.QLineEdit(self.groupBox_5)
        self.lineEdit_18.setGeometry(QtCore.QRect(160, 60, 161, 20))
        self.lineEdit_18.setStyleSheet(_fromUtf8("color : rgb(0, 0, 0)"))
        self.lineEdit_18.setReadOnly(True)
        self.lineEdit_18.setObjectName(_fromUtf8("lineEdit_18"))
        self.lineEdit_21 = QtGui.QLineEdit(self.groupBox_5)
        self.lineEdit_21.setGeometry(QtCore.QRect(160, 90, 161, 20))
        self.lineEdit_21.setStyleSheet(_fromUtf8("color : rgb(0, 0, 0)"))
        self.lineEdit_21.setReadOnly(True)
        self.lineEdit_21.setObjectName(_fromUtf8("lineEdit_21"))
        self.label_38 = QtGui.QLabel(self.tab_2)
        self.label_38.setGeometry(QtCore.QRect(20, 20, 321, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Cambria"))
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_38.setFont(font)
        self.label_38.setStyleSheet(_fromUtf8("color : rgb(255, 255, 255)"))
        self.label_38.setObjectName(_fromUtf8("label_38"))
        self.label.raise_()
        self.groupBox_4.raise_()
        self.groupBox_5.raise_()
        self.label_38.raise_()
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.label_39 = QtGui.QLabel(self.tab_3)
        self.label_39.setGeometry(QtCore.QRect(10, 10, 291, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Cambria"))
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_39.setFont(font)
        self.label_39.setStyleSheet(_fromUtf8("color : rgb(255, 255, 255)"))
        self.label_39.setObjectName(_fromUtf8("label_39"))
        self.label_26 = QtGui.QLabel(self.tab_3)
        self.label_26.setGeometry(QtCore.QRect(20, 140, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_26.setFont(font)
        self.label_26.setStyleSheet(_fromUtf8("color : rgb(255, 255, 255)"))
        self.label_26.setObjectName(_fromUtf8("label_26"))
        self.label_27 = QtGui.QLabel(self.tab_3)
        self.label_27.setGeometry(QtCore.QRect(20, 100, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_27.setFont(font)
        self.label_27.setStyleSheet(_fromUtf8("color : rgb(255, 255, 255)"))
        self.label_27.setObjectName(_fromUtf8("label_27"))
        self.label_28 = QtGui.QLabel(self.tab_3)
        self.label_28.setGeometry(QtCore.QRect(20, 60, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_28.setFont(font)
        self.label_28.setStyleSheet(_fromUtf8("color : rgb(255, 255, 255)"))
        self.label_28.setObjectName(_fromUtf8("label_28"))
        self.doubleSpinBox_2 = QtGui.QDoubleSpinBox(self.tab_3)
        self.doubleSpinBox_2.setGeometry(QtCore.QRect(140, 100, 171, 22))
        self.doubleSpinBox_2.setMaximum(4999999.99)
        self.doubleSpinBox_2.setSingleStep(1000.0)
        self.doubleSpinBox_2.setObjectName(_fromUtf8("doubleSpinBox_2"))
        self.doubleSpinBox_3 = QtGui.QDoubleSpinBox(self.tab_3)
        self.doubleSpinBox_3.setGeometry(QtCore.QRect(140, 140, 171, 22))
        self.doubleSpinBox_3.setMaximum(4999999.99)
        self.doubleSpinBox_3.setSingleStep(1000.0)
        self.doubleSpinBox_3.setObjectName(_fromUtf8("doubleSpinBox_3"))
        self.lineEdit = QtGui.QLineEdit(self.tab_3)
        self.lineEdit.setGeometry(QtCore.QRect(140, 60, 171, 20))
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.pushButton = QtGui.QPushButton(self.tab_3)
        self.pushButton.setGeometry(QtCore.QRect(20, 220, 301, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.label_29 = QtGui.QLabel(self.tab_3)
        self.label_29.setGeometry(QtCore.QRect(20, 310, 661, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_29.setFont(font)
        self.label_29.setStyleSheet(_fromUtf8("color : rgb(255, 255, 255)"))
        self.label_29.setText(_fromUtf8(""))
        self.label_29.setObjectName(_fromUtf8("label_29"))
        self.label_2 = QtGui.QLabel(self.tab_3)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 701, 431))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_2.raise_()
        self.label_39.raise_()
        self.label_26.raise_()
        self.label_27.raise_()
        self.label_28.raise_()
        self.doubleSpinBox_2.raise_()
        self.doubleSpinBox_3.raise_()
        self.lineEdit.raise_()
        self.pushButton.raise_()
        self.label_29.raise_()
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.tableWidget = QtGui.QTableWidget(self.tab_4)
        self.tableWidget.setGeometry(QtCore.QRect(10, 70, 261, 121))
        self.tableWidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget.verticalHeader().setMinimumSectionSize(19)
        self.label_3 = QtGui.QLabel(self.tab_4)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 701, 431))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_40 = QtGui.QLabel(self.tab_4)
        self.label_40.setGeometry(QtCore.QRect(20, 20, 201, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Cambria"))
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_40.setFont(font)
        self.label_40.setStyleSheet(_fromUtf8("color : rgb(255, 255, 255)"))
        self.label_40.setObjectName(_fromUtf8("label_40"))
        self.pushButton_2 = QtGui.QPushButton(self.tab_4)
        self.pushButton_2.setGeometry(QtCore.QRect(310, 120, 161, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.label_41 = QtGui.QLabel(self.tab_4)
        self.label_41.setGeometry(QtCore.QRect(10, 220, 201, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Cambria"))
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_41.setFont(font)
        self.label_41.setStyleSheet(_fromUtf8("color : rgb(255, 255, 255)"))
        self.label_41.setObjectName(_fromUtf8("label_41"))
        self.line = QtGui.QFrame(self.tab_4)
        self.line.setGeometry(QtCore.QRect(0, 200, 701, 16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.groupBox_6 = QtGui.QGroupBox(self.tab_4)
        self.groupBox_6.setGeometry(QtCore.QRect(10, 260, 331, 131))
        self.groupBox_6.setStyleSheet(_fromUtf8("color : rgb(255, 255, 255)"))
        self.groupBox_6.setObjectName(_fromUtf8("groupBox_6"))
        self.label_24 = QtGui.QLabel(self.groupBox_6)
        self.label_24.setGeometry(QtCore.QRect(10, 30, 121, 16))
        self.label_24.setObjectName(_fromUtf8("label_24"))
        self.label_25 = QtGui.QLabel(self.groupBox_6)
        self.label_25.setGeometry(QtCore.QRect(10, 60, 121, 16))
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.label_30 = QtGui.QLabel(self.groupBox_6)
        self.label_30.setGeometry(QtCore.QRect(10, 90, 131, 16))
        self.label_30.setObjectName(_fromUtf8("label_30"))
        self.lineEdit_22 = QtGui.QLineEdit(self.groupBox_6)
        self.lineEdit_22.setGeometry(QtCore.QRect(160, 30, 161, 20))
        self.lineEdit_22.setStyleSheet(_fromUtf8("color : rgb(0, 0, 0)"))
        self.lineEdit_22.setReadOnly(False)
        self.lineEdit_22.setObjectName(_fromUtf8("lineEdit_22"))
        self.comboBox = QtGui.QComboBox(self.groupBox_6)
        self.comboBox.setGeometry(QtCore.QRect(160, 90, 161, 22))
        self.comboBox.setStyleSheet(_fromUtf8("color : rgb(0, 0, 0)"))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.doubleSpinBox = QtGui.QDoubleSpinBox(self.groupBox_6)
        self.doubleSpinBox.setGeometry(QtCore.QRect(160, 60, 161, 22))
        self.doubleSpinBox.setStyleSheet(_fromUtf8("color : rgb(0, 0, 0)"))
        self.doubleSpinBox.setMaximum(9999.99)
        self.doubleSpinBox.setSingleStep(100.0)
        self.doubleSpinBox.setObjectName(_fromUtf8("doubleSpinBox"))
        self.pushButton_3 = QtGui.QPushButton(self.tab_4)
        self.pushButton_3.setGeometry(QtCore.QRect(390, 320, 161, 23))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.pushButton_5 = QtGui.QPushButton(self.tab_4)
        self.pushButton_5.setGeometry(QtCore.QRect(510, 10, 171, 23))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.label_3.raise_()
        self.tableWidget.raise_()
        self.label_40.raise_()
        self.pushButton_2.raise_()
        self.label_41.raise_()
        self.line.raise_()
        self.groupBox_6.raise_()
        self.pushButton_3.raise_()
        self.pushButton_5.raise_()
        self.tabWidget.addTab(self.tab_4, _fromUtf8(""))
        self.tab_5 = QtGui.QWidget()
        self.tab_5.setObjectName(_fromUtf8("tab_5"))
        self.pushButton_4 = QtGui.QPushButton(self.tab_5)
        self.pushButton_4.setGeometry(QtCore.QRect(230, 230, 181, 21))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.label_5 = QtGui.QLabel(self.tab_5)
        self.label_5.setGeometry(QtCore.QRect(0, 0, 701, 431))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.pushButton_6 = QtGui.QPushButton(self.tab_5)
        self.pushButton_6.setGeometry(QtCore.QRect(230, 170, 181, 21))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.label_5.raise_()
        self.pushButton_4.raise_()
        self.pushButton_6.raise_()
        self.tabWidget.addTab(self.tab_5, _fromUtf8(""))
        self.tab_6 = QtGui.QWidget()
        self.tab_6.setObjectName(_fromUtf8("tab_6"))
        self.label_4 = QtGui.QLabel(self.tab_6)
        self.label_4.setGeometry(QtCore.QRect(10, 0, 661, 71))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(_fromUtf8("color : rgb(255, 255, 255)"))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_7 = QtGui.QLabel(self.tab_6)
        self.label_7.setGeometry(QtCore.QRect(0, 0, 701, 431))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.groupBox_7 = QtGui.QGroupBox(self.tab_6)
        self.groupBox_7.setGeometry(QtCore.QRect(30, 80, 331, 131))
        self.groupBox_7.setStyleSheet(_fromUtf8("color : rgb(255, 255, 255)"))
        self.groupBox_7.setObjectName(_fromUtf8("groupBox_7"))
        self.label_31 = QtGui.QLabel(self.groupBox_7)
        self.label_31.setGeometry(QtCore.QRect(10, 30, 121, 16))
        self.label_31.setObjectName(_fromUtf8("label_31"))
        self.label_43 = QtGui.QLabel(self.groupBox_7)
        self.label_43.setGeometry(QtCore.QRect(10, 60, 121, 16))
        self.label_43.setObjectName(_fromUtf8("label_43"))
        self.label_44 = QtGui.QLabel(self.groupBox_7)
        self.label_44.setGeometry(QtCore.QRect(10, 90, 131, 16))
        self.label_44.setObjectName(_fromUtf8("label_44"))
        self.lineEdit_24 = QtGui.QLineEdit(self.groupBox_7)
        self.lineEdit_24.setGeometry(QtCore.QRect(160, 30, 161, 20))
        self.lineEdit_24.setStyleSheet(_fromUtf8("color : rgb(0, 0, 0)"))
        self.lineEdit_24.setReadOnly(True)
        self.lineEdit_24.setObjectName(_fromUtf8("lineEdit_24"))
        self.lineEdit_25 = QtGui.QLineEdit(self.groupBox_7)
        self.lineEdit_25.setGeometry(QtCore.QRect(160, 60, 161, 20))
        self.lineEdit_25.setStyleSheet(_fromUtf8("color : rgb(0, 0, 0)"))
        self.lineEdit_25.setReadOnly(True)
        self.lineEdit_25.setObjectName(_fromUtf8("lineEdit_25"))
        self.lineEdit_26 = QtGui.QLineEdit(self.groupBox_7)
        self.lineEdit_26.setGeometry(QtCore.QRect(160, 90, 161, 20))
        self.lineEdit_26.setStyleSheet(_fromUtf8("color : rgb(0, 0, 0)"))
        self.lineEdit_26.setReadOnly(True)
        self.lineEdit_26.setObjectName(_fromUtf8("lineEdit_26"))
        self.groupBox_8 = QtGui.QGroupBox(self.tab_6)
        self.groupBox_8.setGeometry(QtCore.QRect(30, 250, 331, 131))
        self.groupBox_8.setStyleSheet(_fromUtf8("color : rgb(255, 255, 255)"))
        self.groupBox_8.setObjectName(_fromUtf8("groupBox_8"))
        self.label_45 = QtGui.QLabel(self.groupBox_8)
        self.label_45.setGeometry(QtCore.QRect(10, 30, 121, 16))
        self.label_45.setObjectName(_fromUtf8("label_45"))
        self.label_46 = QtGui.QLabel(self.groupBox_8)
        self.label_46.setGeometry(QtCore.QRect(10, 60, 121, 16))
        self.label_46.setObjectName(_fromUtf8("label_46"))
        self.label_47 = QtGui.QLabel(self.groupBox_8)
        self.label_47.setGeometry(QtCore.QRect(10, 90, 131, 16))
        self.label_47.setObjectName(_fromUtf8("label_47"))
        self.lineEdit_27 = QtGui.QLineEdit(self.groupBox_8)
        self.lineEdit_27.setGeometry(QtCore.QRect(160, 30, 161, 20))
        self.lineEdit_27.setStyleSheet(_fromUtf8("color : rgb(0, 0, 0)"))
        self.lineEdit_27.setReadOnly(True)
        self.lineEdit_27.setObjectName(_fromUtf8("lineEdit_27"))
        self.lineEdit_28 = QtGui.QLineEdit(self.groupBox_8)
        self.lineEdit_28.setGeometry(QtCore.QRect(160, 60, 161, 20))
        self.lineEdit_28.setStyleSheet(_fromUtf8("color : rgb(0, 0, 0)"))
        self.lineEdit_28.setReadOnly(True)
        self.lineEdit_28.setObjectName(_fromUtf8("lineEdit_28"))
        self.lineEdit_29 = QtGui.QLineEdit(self.groupBox_8)
        self.lineEdit_29.setGeometry(QtCore.QRect(160, 90, 161, 20))
        self.lineEdit_29.setStyleSheet(_fromUtf8("color : rgb(0, 0, 0)"))
        self.lineEdit_29.setReadOnly(True)
        self.lineEdit_29.setObjectName(_fromUtf8("lineEdit_29"))
        self.label_7.raise_()
        self.label_4.raise_()
        self.groupBox_7.raise_()
        self.groupBox_8.raise_()
        self.tabWidget.addTab(self.tab_6, _fromUtf8(""))
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtGui.QWidget()
        self.page_2.setObjectName(_fromUtf8("page_2"))
        self.label_37 = QtGui.QLabel(self.page_2)
        self.label_37.setGeometry(QtCore.QRect(30, 120, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_37.setFont(font)
        self.label_37.setStyleSheet(_fromUtf8("color : rgb(255, 255, 255)"))
        self.label_37.setObjectName(_fromUtf8("label_37"))
        self.lineEdit_20 = QtGui.QLineEdit(self.page_2)
        self.lineEdit_20.setGeometry(QtCore.QRect(120, 120, 201, 20))
        self.lineEdit_20.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEdit_20.setReadOnly(False)
        self.lineEdit_20.setObjectName(_fromUtf8("lineEdit_20"))
        self.label_35 = QtGui.QLabel(self.page_2)
        self.label_35.setGeometry(QtCore.QRect(30, 80, 81, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_35.setFont(font)
        self.label_35.setStyleSheet(_fromUtf8("color : rgb(255, 255, 255)"))
        self.label_35.setObjectName(_fromUtf8("label_35"))
        self.label_36 = QtGui.QLabel(self.page_2)
        self.label_36.setGeometry(QtCore.QRect(30, 250, 511, 16))
        self.label_36.setStyleSheet(_fromUtf8("color : rgb(255, 255, 255)"))
        self.label_36.setText(_fromUtf8(""))
        self.label_36.setObjectName(_fromUtf8("label_36"))
        self.label_32 = QtGui.QLabel(self.page_2)
        self.label_32.setGeometry(QtCore.QRect(0, 0, 701, 451))
        self.label_32.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 0);"))
        self.label_32.setObjectName(_fromUtf8("label_32"))
        self.pushButton_10 = QtGui.QPushButton(self.page_2)
        self.pushButton_10.setGeometry(QtCore.QRect(40, 180, 241, 23))
        self.pushButton_10.setObjectName(_fromUtf8("pushButton_10"))
        self.label_34 = QtGui.QLabel(self.page_2)
        self.label_34.setGeometry(QtCore.QRect(30, 20, 201, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Cambria"))
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(True)
        font.setWeight(50)
        self.label_34.setFont(font)
        self.label_34.setStyleSheet(_fromUtf8("color : rgb(255, 255, 255)"))
        self.label_34.setObjectName(_fromUtf8("label_34"))
        self.lineEdit_19 = QtGui.QLineEdit(self.page_2)
        self.lineEdit_19.setGeometry(QtCore.QRect(120, 80, 201, 20))
        self.lineEdit_19.setObjectName(_fromUtf8("lineEdit_19"))
        self.label_42 = QtGui.QLabel(self.page_2)
        self.label_42.setGeometry(QtCore.QRect(40, 270, 641, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_42.setFont(font)
        self.label_42.setStyleSheet(_fromUtf8("color : rgb(255, 255, 255)"))
        self.label_42.setText(_fromUtf8(""))
        self.label_42.setObjectName(_fromUtf8("label_42"))
        self.label_32.raise_()
        self.label_37.raise_()
        self.lineEdit_20.raise_()
        self.label_35.raise_()
        self.label_36.raise_()
        self.pushButton_10.raise_()
        self.label_34.raise_()
        self.lineEdit_19.raise_()
        self.label_42.raise_()
        self.stackedWidget.addWidget(self.page_2)

        self.retranslateUi(Form)
        self.stackedWidget.setCurrentIndex(1)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label_33.setText(_translate("Form", "Welcome", None))
        self.label_6.setText(_translate("Form", "TextLabel", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Home", None))
        self.label_8.setText(_translate("Form", "List of Complaints", None))
        self.label_48.setText(_translate("Form", "Student Complaints", None))
        self.pushButton_7.setText(_translate("Form", "View Complaint", None))
        self.label_50.setText(_translate("Form", "Complaint ID ", None))
        self.label_51.setText(_translate("Form", "Student ID", None))
        self.label_52.setText(_translate("Form", "Complaint Description", None))
        self.label_53.setText(_translate("Form", "Action Taken Report (ATR)", None))
        self.pushButton_8.setText(_translate("Form", "Post ATR", None))
        self.label_9.setText(_translate("Form", "TextLabel", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), _translate("Form", "Complaints", None))
        self.groupBox_4.setTitle(_translate("Form", "Single Rooms", None))
        self.label_12.setText(_translate("Form", "Single Room Count", None))
        self.label_13.setText(_translate("Form", "Single Rooms Occupied", None))
        self.label_14.setText(_translate("Form", "Single Rooms Vacant", None))
        self.label.setText(_translate("Form", "TextLabel", None))
        self.groupBox_5.setTitle(_translate("Form", "Double Rooms", None))
        self.label_21.setText(_translate("Form", "Double Room Count", None))
        self.label_22.setText(_translate("Form", "Double Rooms Occupied", None))
        self.label_23.setText(_translate("Form", "Double Rooms Vacant", None))
        self.label_38.setText(_translate("Form", "Room Occupancy Information", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "View Room Occupancy", None))
        self.label_39.setText(_translate("Form", "Submit New Grant Request", None))
        self.label_26.setText(_translate("Form", "Repair Grant", None))
        self.label_27.setText(_translate("Form", "Misc Grant", None))
        self.label_28.setText(_translate("Form", "Salary Grant", None))
        self.pushButton.setText(_translate("Form", "Submit Request", None))
        self.label_2.setText(_translate("Form", "TextLabel", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Form", "Grant Request", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Worker ID", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Worker Name", None))
        self.label_3.setText(_translate("Form", "TextLabel", None))
        self.label_40.setText(_translate("Form", "Hall Worker List", None))
        self.pushButton_2.setText(_translate("Form", "Fire Worker", None))
        self.label_41.setText(_translate("Form", "Hire New Worker", None))
        self.groupBox_6.setTitle(_translate("Form", "Worker Details", None))
        self.label_24.setText(_translate("Form", "Worker Name", None))
        self.label_25.setText(_translate("Form", "Worker Daily Wage", None))
        self.label_30.setText(_translate("Form", "Worker Type", None))
        self.comboBox.setItemText(0, _translate("Form", "Attendant", None))
        self.comboBox.setItemText(1, _translate("Form", "Gardener", None))
        self.pushButton_3.setText(_translate("Form", "Hire Worker", None))
        self.pushButton_5.setText(_translate("Form", "Pay Salaries", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Form", "Hire / Fire Workers", None))
        self.pushButton_4.setText(_translate("Form", "Print Account Statement", None))
        self.label_5.setText(_translate("Form", "TextLabel", None))
        self.pushButton_6.setText(_translate("Form", "Generate Salary List", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("Form", "Print Account Statement", None))
        self.label_4.setText(_translate("Form", "Sorry, you don\'t have the permissio to access this information", None))
        self.label_7.setText(_translate("Form", "TextLabel", None))
        self.groupBox_7.setTitle(_translate("Form", "Single Rooms", None))
        self.label_31.setText(_translate("Form", "Single Room Count", None))
        self.label_43.setText(_translate("Form", "Single Rooms Occupied", None))
        self.label_44.setText(_translate("Form", "Single Rooms Vacant", None))
        self.groupBox_8.setTitle(_translate("Form", "Double Rooms", None))
        self.label_45.setText(_translate("Form", "Double Room Count", None))
        self.label_46.setText(_translate("Form", "Double Rooms Occupied", None))
        self.label_47.setText(_translate("Form", "Double Rooms Vacant", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), _translate("Form", "View Overall Room Occupancy", None))
        self.label_37.setText(_translate("Form", "Password", None))
        self.label_35.setText(_translate("Form", "Warden ID", None))
        self.label_32.setText(_translate("Form", "TextLabel", None))
        self.pushButton_10.setText(_translate("Form", "Login", None))
        self.label_34.setText(_translate("Form", "Warden Login", None))

