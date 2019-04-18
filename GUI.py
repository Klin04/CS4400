import sys
from PyQt5 import QtCore, QtWidgets, QtGui


# class MainWindow(QtWidgets.QWidget):

#     switch_window = QtCore.pyqtSignal(str)

#     def __init__(self):
#         QtWidgets.QWidget.__init__(self)
#         self.setWindowTitle('Main Window')

#         layout = QtWidgets.QGridLayout()

#         self.line_edit = QtWidgets.QLineEdit()
#         layout.addWidget(self.line_edit)

#         self.button = QtWidgets.QPushButton('Switch Window')
#         self.button.clicked.connect(self.switch)
#         layout.addWidget(self.button)

#         self.setLayout(layout)

#     def switch(self):
#         self.switch_window.emit(self.line_edit.text())


class RegisterNavigation(QtWidgets.QWidget):

    def __init__(self):
        QtWidgets.QWidget.__init__(self)
        self.setWindowTitle('Register Navigation')
        self.title = QtWidgets.QLabel()
        self.title.setText("Register Navigation")
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.userOnly = QtWidgets.QPushButton('User Only', self)
        self.visitorOnly = QtWidgets.QPushButton('Visitor Only', self)
        self.employeeOnly = QtWidgets.QPushButton('Employee Only', self)
        self.employeeVisitor = QtWidgets.QPushButton('Employee-Visitor', self)
        self.back = QtWidgets.QPushButton('Back', self)

        layout = QtWidgets.QGridLayout()

        layout.addWidget(self.title)
        layout.addWidget(self.userOnly)
        layout.addWidget(self.visitorOnly)
        layout.addWidget(self.employeeOnly)
        layout.addWidget(self.employeeVisitor)
        layout.addWidget(self.back)

        self.setLayout(layout)


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

