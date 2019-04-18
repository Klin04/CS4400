import sys
from PyQt5 import QtCore, QtWidgets, QtGui

class UserFunc(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.title = QtWidgets.QLabel()
        self.title.setText("User Functionality")