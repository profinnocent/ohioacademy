import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLineEdit
from PyQt5.QtCore import pyqtSlot, pyqtSignal
from PyQt5 import QtCore, QtGui
from PyQt5 import uic
# from PyQt5.uic import loadUi
from loginpg import Loginpage


class Studreg(QWidget):
    # switch_window = pyqtSignal()

    def __init__(self):
        super(Studreg, self).__init__()
        uic.loadUi("studentsregistration.ui", self)
        self.w = None

        # self.firstname = self.findChild(QLineEdit, "fnametext")
        # self.backbtn = self.findChild(QPushButton, "backbtn")
        # self.pushButton = self.findChild(QPushButton, "pushButton_2")

        self.pushButton_2.clicked.connect(self.display)
        # self.backbtn.clicked.connect(lambda:Loginpage())
        # self.backbtn.clicked.connect(self.w)
        # self.w.show()

        self.show()

    def display(self):
        self.firstname.setText("Hello World")

        print("submitted")

        # print(txt)
        # lastname = self.lnametext.text(QLineEdit)
        # email = self.emailtext.text(QLineEdit)
        # pword = self.passtext.text(QLineEdit)
        # confirmpword = self.cpasstext.text(QLineEdit)
        # dpartment = self.dpartmenttext.text(QLineEdit)
        # level = self.leveltext.text(QLineEdit)
        # age = self.agetext.text(QLineEdit)
        # gender = self.gendertext.text(QLineEdit)

        # print(firstname)





    def showm(self):
        print("login successful")


#
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Studreg()
    sys.exit(app.exec())



# app = QApplication(sys.argv)
# ex = Studreg()
# app.exec()