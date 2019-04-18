import sys
from PyQt5 import QtCore, QtWidgets, QtGui

class StaffVisitorFunc(QtWidgets.QWidget):
    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.title = QtWidgets.QLabel()
        self.title.setText("Staff Functionality")
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.title)
        self.manageProfileButton = QtWidgets.QPushButton('Manage Profile', self)
        self.viewscheduleButton = QtWidgets.QPushButton('View Schedule', self)
        self.exploreeventButton = QtWidgets.QPushButton('Explore Event', self)
        self.taketransitButton = QtWidgets.QPushButton('Take Transit', self)
        self.exploresiteButton = QtWidgets.QPushButton('Explore Site', self)
        self.viewvisitHistButton = QtWidgets.QPushButton('View Visit History', self)
        self.viewTransitHistButton = QtWidgets.QPushButton('View Transit History', self)
        self.backButton = QtWidgets.QPushButton('Back', self) 
        layout.addWidget(self.manageProfileButton)
        layout.addWidget(self.viewschduleButton)
        layout.addWidget(self.taketransitButton)
        layout.addWidget(self.viewTransitHistButton)
        layout.addWidget(self.backButton)
        layout.addWidget(self.viewvisitHistButton)
        layout.addWidget(self.exploresiteButton)
        layout.addWidget(self.exploreeventButton)
        self.setLayout(layout)
        self.resize(600, 150)