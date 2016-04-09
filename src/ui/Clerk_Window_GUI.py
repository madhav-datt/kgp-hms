import sys
from PyQt4 import QtCore, QtGui
from ..database import db_func as db
from ..database import db_rebuild as dbr
from ..workers import attendant
import Clerk_Window
import time

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

clerk_ID = 0


class ClerkWindowClass(QtGui.QWidget, Clerk_Window.Ui_Form):
    """
    Clerk Window Class
    Contain GUI and Functionality
    """

    def __init__(self):
        """
        Init Clerk Window GUI
        Create and launch instance
        """

        QtGui.QWidget.__init__(self)
        self.setupUi(self)
        self.bkdLabel.setPixmap(QtGui.QPixmap(_fromUtf8('src/ui/bkd4.jpg')))
        self.bkdLabel.setScaledContents(True)
        self.label_8.setText("Today's Date : " + time.strftime("%x"))

        # Set text fields with value from databases
        self.lineEdit.setText(str(clerk_ID))
        if clerk_ID:
            self.lineEdit_2.setText(str(db.get("worker", clerk_ID, "name")))
            self.label_2.setText("Welcome " + str(db.get("worker", clerk_ID, "name")))
            self.lineEdit_3.setText(str(db.get("worker", clerk_ID, "hall_ID")))
        else:
            self.lineEdit_2.setText("Name")
            self.lineEdit_3.setText("Hall_ID")

        # Build table from worker database
        worker_list = dbr.rebuild("worker")
        for key in worker_list:
            if isinstance(worker_list[key], attendant.Attendant):
                i = 0
                item = self.tableWidget.verticalHeaderItem(i)
                item.setText("0")
                item = self.tableWidget.item(i, 0)
                item.setText(str(worker_list[key].worker_ID))
                item = self.tableWidget.item(i, 1)
                item.setText(worker_list[key].name)
                i += 1

        # Deactivate attendance button if last attendance recorded is on same day
        if db.get_attend_date() == time.strftime('%Y-%m-%d'):
            self.pushButton.isEnabled(False)

        self.pushButton.clicked.connect(self.give_attendance)

    def give_attendance(self):
        """
        Mark attendance for present date for all selected workers
        Can be called only once in a day
        """

        worker_list = dbr.rebuild("worker")

        for i in range(self.tableWidget.rowCount()):
            worker_sel_ID = self.tableWidget.item(i, 0)
            for key in worker_list:
                if worker_sel_ID == worker_list[key].worker_ID:
                    worker_list[key].monthly_attendance += 1

        self.pushButton.isEnabled(False)
        db.update_attend_date()

app = QtGui.QApplication(sys.argv)
Form = ClerkWindowClass()
Form.show()
app.exec_()
