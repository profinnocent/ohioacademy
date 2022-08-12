import sys
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
from PyQt5.QtCore import pyqtSlot, pyqtSignal
from PyQt5.uic import loadUi

class Loginpage(QWidget):
    switch_window = pyqtSignal()


    def __init__(self):
        super(Loginpage, self).__init__()
        loadUi("loginpage.ui", self)

        # self.username = self.findChild(QLineEdit, "userEdit")
        # self.password = self.findChild(QLineEdit, "passwordEdit")
        # self.loginbtn = self.findChild(QPushButton, "loginBut")

        self.userEdit.textChanged.connect(self.duplicate1)

        # print(self.loginbtn)

        # self.textbox = QLineEdit(self)
        # self.loginbtn.clicked.connect(self.loginbutt)

        self.show()
        # self.loginButton.clicked.connect(self.studentReg)

    def duplicate1(self):
        self.passwordEdit.setText(self.userEdit.text())


    # def login(self):
    #     username = str(self.userEdit.text())
    #     print(username)
    #     paxword = str(self.passwordEdit.text())
    #     print(paxword)
    #
    #     self.loginbut()
    #
    #     self.userEdit.clear()
    def loginbutt(self):
        textboxvalue = self.textbox.text()
        self.switch_window.emit(textboxvalue)

    # def loginbut(self):
    #     print("Login Successful")
    #
    #     self.textbox.clear()

    # def studentReg(self):
    #     loadUi("studentsregistration.ui", self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Loginpage()
    sys.exit(app.exec())

