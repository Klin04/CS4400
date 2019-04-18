class RegisterNavigation(QtWidgets.QWidget):

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('Register Navigation')
        self.title = QtWidgets.QLabel()
        self.title.setText("Register Navigation")
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.userOnly = QtWidgets.QPushButton('User Only', self)
        self.userOnly.clicked.connect(self.userOnlyB)
        self.visitorOnly = QtWidgets.QPushButton('Visitor Only', self)
        self.employeeOnly = QtWidgets.QPushButton('Employee Only', self)
        self.employeeVisitor = QtWidgets.QPushButton('Employee-Visitor', self)
        self.back = QtWidgets.QPushButton('Back', self)
        self.back.clicked.connect(self.backB)

        layout = QtWidgets.QGridLayout()

        layout.addWidget(self.title)
        layout.addWidget(self.userOnly)
        layout.addWidget(self.visitorOnly)
        layout.addWidget(self.employeeOnly)
        layout.addWidget(self.employeeVisitor)
        layout.addWidget(self.back)

        self.setLayout(layout)

    def userOnlyB(self):
        self.cams = userOnlyRegistration()
        self.cams.show()
        self.close()

    def visitorOnlyB(self):
        self.cams = visitorOnlyRegistration()
        self.cams.show()
        self.close()

    def employeeOnlyB(self):
        self.cams = employeeOnlyRegistration()
        self.cams.show()
        self.close()

    def employeeVisitorB(self):
        self.cams = employeeVisitorRegistration()
        self.cams.show()
        self.close()
    
    def backB(self):
        self.cams = Login()
        self.cams.show()
        self.close()
