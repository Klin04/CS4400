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
        self.viewsitereportButton = QtWidgets.QPushButton('View Site Report', self)
        self.manageeventButton = QtWidgets.QPushButton('Manage Event', self)
        self.taketransitButton = QtWidgets.QPushButton('Take Transit', self)
        self.viewstaffButton = QtWidgets.QPushButton('View Staff', self)
        self.viewTransitHistButton = QtWidgets.QPushButton('View Transit History', self)
        self.backButton = QtWidgets.QPushButton('Back', self) 
        layout.addWidget(self.manageProfileButton)
        layout.addWidget(self.viewsitereportButton)
        layout.addWidget(self.manageeventButton)
        layout.addWidget(self.taketransitButton)
        layout.addWidget(self.viewstaffButton)
        layout.addWidget(self.viewTransitHistButton)
        layout.addWidget(self.backButton)
        self.setLayout(layout)
        self.resize(600, 150)