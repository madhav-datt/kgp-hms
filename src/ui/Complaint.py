# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Complaint.ui'
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

class Ui_complaintWindow(object):
    def setupUi(self, complaintWindow):
        complaintWindow.setObjectName(_fromUtf8("complaintWindow"))
        complaintWindow.setWindowModality(QtCore.Qt.ApplicationModal)
        complaintWindow.resize(384, 441)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("../../Desktop/logo2.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        complaintWindow.setWindowIcon(icon)
        self.formLayout = QtGui.QFormLayout(complaintWindow)
        self.formLayout.setFieldGrowthPolicy(QtGui.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setVerticalSpacing(12)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.formLayout.setLayout(0, QtGui.QFormLayout.LabelRole, self.verticalLayout)
        self.label = QtGui.QLabel(complaintWindow)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Cambria"))
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.SpanningRole, self.label)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.formLayout.setLayout(2, QtGui.QFormLayout.LabelRole, self.horizontalLayout)
        self.label_2 = QtGui.QLabel(complaintWindow)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.label_2)
        self.lineEdit = QtGui.QLineEdit(complaintWindow)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.lineEdit)
        self.label_6 = QtGui.QLabel(complaintWindow)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label_6)
        self.lineEdit_2 = QtGui.QLineEdit(complaintWindow)
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.lineEdit_2)
        self.label_7 = QtGui.QLabel(complaintWindow)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.label_7)
        self.lineEdit_3 = QtGui.QLineEdit(complaintWindow)
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.lineEdit_3)
        self.label_3 = QtGui.QLabel(complaintWindow)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.LabelRole, self.label_3)
        self.lineEdit_4 = QtGui.QLineEdit(complaintWindow)
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.formLayout.setWidget(6, QtGui.QFormLayout.FieldRole, self.lineEdit_4)
        self.label_4 = QtGui.QLabel(complaintWindow)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.formLayout.setWidget(7, QtGui.QFormLayout.LabelRole, self.label_4)
        self.comboBox = QtGui.QComboBox(complaintWindow)
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.comboBox.addItem(_fromUtf8(""))
        self.formLayout.setWidget(7, QtGui.QFormLayout.FieldRole, self.comboBox)
        self.label_5 = QtGui.QLabel(complaintWindow)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.formLayout.setWidget(8, QtGui.QFormLayout.LabelRole, self.label_5)
        self.label_8 = QtGui.QLabel(complaintWindow)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.formLayout.setWidget(9, QtGui.QFormLayout.LabelRole, self.label_8)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.formLayout.setItem(10, QtGui.QFormLayout.LabelRole, spacerItem)
        self.buttonBox = QtGui.QDialogButtonBox(complaintWindow)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Save)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.formLayout.setWidget(11, QtGui.QFormLayout.LabelRole, self.buttonBox)
        self.plainTextEdit = QtGui.QPlainTextEdit(complaintWindow)
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.formLayout.setWidget(8, QtGui.QFormLayout.FieldRole, self.plainTextEdit)
        self.plainTextEdit_2 = QtGui.QPlainTextEdit(complaintWindow)
        self.plainTextEdit_2.setReadOnly(True)
        self.plainTextEdit_2.setObjectName(_fromUtf8("plainTextEdit_2"))
        self.formLayout.setWidget(9, QtGui.QFormLayout.FieldRole, self.plainTextEdit_2)

        self.retranslateUi(complaintWindow)
        QtCore.QMetaObject.connectSlotsByName(complaintWindow)

    def retranslateUi(self, complaintWindow):
        complaintWindow.setWindowTitle(_translate("complaintWindow", "HMS - Student Complaint", None))
        self.label.setText(_translate("complaintWindow", "Student Complaint", None))
        self.label_2.setText(_translate("complaintWindow", "Complaint ID ", None))
        self.label_6.setText(_translate("complaintWindow", "Student ID", None))
        self.label_7.setText(_translate("complaintWindow", "Concerned Hall", None))
        self.label_3.setText(_translate("complaintWindow", "Complaint Subject", None))
        self.label_4.setText(_translate("complaintWindow", "Complaint Type", None))
        self.comboBox.setItemText(0, _translate("complaintWindow", "Repair", None))
        self.comboBox.setItemText(1, _translate("complaintWindow", "Worker Complaint", None))
        self.comboBox.setItemText(2, _translate("complaintWindow", "Other", None))
        self.label_5.setText(_translate("complaintWindow", "Complaint Description", None))
        self.label_8.setText(_translate("complaintWindow", "Action Taken Report (ATR)", None))

