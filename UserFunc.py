import sys
from PyQt5 import QtCore, QtWidgets, QtGui

class UserFunc(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.title = QtWidgets.QLabel()
        self.title.setText("User Functionality")
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.title)
        self.takeTransitButton = QtWidgets.QPushButton('Take Transit', self)
        self.ViewTransitButton = QtWidgets.QPushButton('View Transit History', self)
        self.back = QtWidgets.QPushButton('Back', self)
        layout.addWidget(self.takeTransitButton)
        layout.addWidget(self.ViewTransitButton)
        layout.addWidget(self.back)
        self.setLayout(layout)
        self.resize(600, 150)
    
