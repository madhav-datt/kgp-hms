from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QApplication

import Student_Main_Window_GUI

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

'''
class StudentPortalWindow(QtGui.QWidget, Student_Main_Window.Ui_Form):
    def __init__(self, parent=None):
        super(StudentPortalWindow, self).__init__(parent)
        self.setupUi(self)
        self.pushButton_3.clicked.connect(self.action)


    def action(self):
        self.window = ComplaintWindow()
        self.window.show()

class ComplaintWindow(QtGui.QWidget, Complaint.Ui_complaintWindow):
    def __init__(self, parent=None):
        super(ComplaintWindow, self).__init__(parent)
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)
        self.setupUi(self)
'''

if __name__ == "__main__":
    import sys
    '''
    app = QtGui.QApplication(sys.argv)
    Form = QtGui.QWidget()
    ui = Student_Main_Window.Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
    '''
    app = QApplication(sys.argv)
    form = Student_Main_Window_GUI.StudentMainWindowClass()
    form.show()
    app.exec_()