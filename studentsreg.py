import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtCore import pyqtSlot
from PyQt5.uic import loadUi

class Loginpage(QWidget):
    def __init__(self):
        super(Loginpage, self).__init__()
        loadUi("loginpage.ui", self)
        self.logWidget.selectionChanged.connect(self.login)
        self.loginButton.clicked.connect(self.studentReg)

    def login(self):
        username = str(self.userEdit.text())
        print(username)
        paxword = str(self.passwordEdit.text())
        print(paxword)

        self.loginbut()

        self.userEdit.clear()

    def loginbut(self):
        self.loginButton.clicked()
        print("Login Successful")

    def studentReg(self):
        loadUi("studentsregistration.ui", self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    log = Loginpage()
    log.show()
    sys.exit(app.exec())

