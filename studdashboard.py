import sys
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtCore import pyqtSlot
from PyQt5.uic import loadUi


class Dashboard(QWidget):
    def __init__(self):
        super(Dashboard, self).__init__()
