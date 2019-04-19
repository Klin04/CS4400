import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from Login import Ui_MainWindow as LoginPage
from RegisterNavigation import Ui_Form as RegisterNavigationPage

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.LoginPage = LoginPage()
        self.RegisterNavigationPage = RegisterNavigationPage()

    def startRegisterNavigation(self, parent=None):
        self.RegisterNavigationPage.setupUi(self)
        self.show()

    def startLoginPage(self):
        self.LoginPage.setupUi(self)
        self.show()


class Controller():
    def __init__(self):
        self.MainWindow = MainWindow()
    
    def showLogin(self):
        self.MainWindow.close()
        self.MainWindow.startLoginPage()
        self.MainWindow.LoginPage.pushButton_2.clicked.connect(self.showRegNav)
    
    def showRegNav(self):
        self.MainWindow.close()
        self.MainWindow = MainWindow()
        self.MainWindow.startRegisterNavigation()
    
    def showRegisterUser(self):
        self.MainWindow.close()
        self.MainWindow = MainWindow()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    c = Controller()
    c.showLogin()
    sys.exit(app.exec_())
