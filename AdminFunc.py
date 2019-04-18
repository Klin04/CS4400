import sys
from PyQt5 import QtCore, QtWidgets, QtGui

class AdminFunc(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.title = QtWidgets.QLabel()
        self.title.setText("Administrator Functionality")
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.title)
        self.manageProfileButton = QtWidgets.QPushButton('Manage Profile', self)
        self.takeTransitButton = QtWidgets.QPushButton('Take Transit', self)
        self.manageUserButton = QtWidgets.QPushButton('Manage User', self)
        self.ViewTransitButton = QtWidgets.QPushButton('View Transit History', self)
        self.manageTransitButton = QtWidgets.QPushButton('Manage Transit', self)
        self.back = QtWidgets.QPushButton('Back', self)
        self.manageSiteButton = QtWidgets.QPushButton('Manage Site', self)
        layout.addWidget(self.manageProfileButton)
        layout.addWidget(self.takeTransitButton)
        layout.addWidget(self.manageUserButton)
        layout.addWidget(self.ViewTransitButton)
        layout.addWidget(self.manageTransitButton)
        layout.addWidget(self.back)
        layout.addWidget(self.manageSiteButton)
        self.setLayout(layout)
        self.resize(600, 150)
    
