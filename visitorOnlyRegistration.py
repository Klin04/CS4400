import sys
from PyQt5 import QtCore, QtWidgets, QtGui

class visitorOnlyRegistration(QtWidgets.QWidget):
    switch_window = QtCore.pyqtSignal(str)

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('Visitor Only Registration')
        self.title = QtWidgets.QLabel()
        self.title.setText("Register Visitor")
        self.fnameLabel = QtWidgets.QLabel()
        self.fnameLabel.setText('First Name')
        self.lnameLabel = QtWidgets.QLabel()
        self.lnameLabel.setText('Last Name')
        self.usernameLabel = QtWidgets.QLabel()
        self.usernameLabel.setText('Username')
        self.passwordLabel = QtWidgets.QLabel()
        self.passwordLabel.setText('Password')
        self.confpasswordLabel = QtWidgets.QLabel()
        self.confpasswordLabel.setText('Confirm Password')
        self.textFname = QtWidgets.QLineEdit()
        self.textLname = QtWidgets.QLineEdit()
        self.textusername = QtWidgets.QLineEdit()
        self.textpassword = QtWidgets.QLineEdit()
        self.textConfirmPass = QtWidgets.QLineEdit()
        self.emailLabel = QtWidgets.QLabel()
        self.emailLabel.setText('Email')
        self.emailEnter = QtWidgets.QLineEdit()
        self.registerbutton = QtWidgets.QPushButton('Register', self)
        self.registerbutton.clicked.connect(self.register)
        self.backButton = QtWidgets.QPushButton('Back', self)
        self.backButton.clicked.connect(self.backB)
        layout = QtWidgets.QGridLayout()

        layout.addWidget(self.title)
        layout.addWidget(self.fnameLabel)
        layout.addWidget(self.textFname)
        layout.addWidget(self.lnameLabel)
        layout.addWidget(self.textLname)
        layout.addWidget(self.usernameLabel)
        layout.addWidget(self.textusername)
        layout.addWidget(self.passwordLabel)
        layout.addWidget(self.textpassword)
        layout.addWidget(self.confpasswordLabel)
        layout.addWidget(self.textConfirmPass)
        layout.addWidget(self.emailLabel)
        layout.addWidget(self.emailEnter)
        layout.addWidget(self.backButton)
        layout.addWidget(self.registerbutton)
        self.setLayout(layout)
        self.resize(600, 150)

    def backB(self):
        from RegisterNavigation import RegisterNavigation
        self.cams = RegisterNavigation()
        self.cams.show()
        self.close()
    
    def registerB(self):
        print("Success register a visitor")