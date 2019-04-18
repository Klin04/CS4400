import sys
from PyQt5 import QtCore, QtWidgets, QtGui
from RegisterNavigation import RegisterNavigation
from UserFunc import UserFunc
from AdminFunc import AdminFunc

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
        self.setLayout(layout)
        self.resize(600, 150)

    def handleLogin(self):
        if (self.textName.text() != '' and
            self.textPass.text() != ''):
            self.cams = AdminFunc()
            self.cams.show()
            self.close()
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
        self.login.resize(600, 150)
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

