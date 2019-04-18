import sys
from PyQt5 import QtCore, QtWidgets, QtGui

class Login(QtWidgets.QWidget):

    switch_window = QtCore.pyqtSignal(str)

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self)
        self.title = QtWidgets.QLabel()
        self.title.setText("Atlanta BeltLine Login")
        self.setWindowTitle('Login Page')
        self.textName = QtWidgets.QLineEdit(self)
        self.textPass = QtWidgets.QLineEdit(self)
        self.buttonLogin = QtWidgets.QPushButton('Login', self)
        self.buttonRegister = QtWidgets.QPushButton('Register', self)
        self.buttonLogin.clicked.connect(self.handleLogin)
        self.buttonRegister.clicked.connect(self.handleRegister)
        self.emailLabel = QtWidgets.QLabel()
        self.passLabel = QtWidgets.QLabel()
        self.emailLabel.setText("Email")
        self.passLabel.setText("Password")
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.title)
        layout.addWidget(self.emailLabel)
        layout.addStretch()
        layout.addWidget(self.textName)
        layout.addWidget(self.passLabel)
        layout.addStretch()
        layout.addWidget(self.textPass)
        layout.addWidget(self.buttonLogin)
        layout.addWidget(self.buttonRegister)

    def handleLogin(self):
        if (self.textName.text() == 'foo' and
            self.textPass.text() == 'bar'):
            self.accept()
        else:
            QtWidgets.QMessageBox.warning(
                self, 'Error', 'Bad user or password')

    def handleRegister(self):
        self.cams = RegisterNavigation()
        self.cams.show()
        self.close()


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


class userOnlyRegistration(QtWidgets.QWidget):

    switch_window = QtCore.pyqtSignal(str)

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('User Only Registration')
        self.title = QtWidgets.QLabel()
        self.title.setText("Register User")
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
        self.registerbutton.clicked.connect(self.registerB)
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

    def backB(self):
        self.cams = RegisterNavigation()
        self.cams.show()
        self.close()
    
    def registerB(self):
        print("Success register a user")

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

    def backB(self):
        self.cams = RegisterNavigation()
        self.cams.show()
        self.close()
    
    def registerB(self):
        print("Success register a visitor")

class RegisterEmployeeOnly(QtWidgets.QWidget):

class Controller:

    def __init__(self):
        pass

    def show_login(self):
        self.login = Login()
        # self.login.switch_window.connect(self.show_main)
        self.login.show()

    # def show_main(self):
    #     self.window = MainWindow()
    #     self.window.switch_window.connect(self.show_register)
    #     self.login.close()
    #     self.window.show()

    # def show_register(self, text):
    #     self.register = Regsiter(text)
    #     self.window.close()
    #     self.register.show()


def main():
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.show_login()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

