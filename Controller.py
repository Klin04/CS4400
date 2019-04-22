import sys
import random
from PyQt5 import QtCore, QtGui, QtWidgets
from Login import Ui_MainWindow as LoginPage
from RegisterNavigation import Ui_Form as RegisterNavigationPage
import RegisterUser
import RegisterEmployee
import RegisterEmployeeVisitor
import RegisterVisitorOnly
import UserFunctionality
import AdministratorFunctionality
import AdminVisitorFunctionality
import ManagerFunctionality
import ManagerVisitorFunctionality
import StaffFunctionality
import StaffVisitorFunctionality
import VisitorFunctionality
import UserTakeTransit
import UserTransitHistory
import EmployeeManageProfile
import AdministratorManagerUser
import AdministratorManageSite
import AdministratorEditSite
import AdministratorCreateSite
import AdministratorManageTransit
import AdministratorEditTransit
import AdministratorCreateTransit
import ManagerManageEvent
import ManagerViewEditEvent
import ManagerCreateEvent
import ManagerManageStaff
import ManagerSiteReport
import ManagerDailyDetail
import StaffViewSchedule
import StaffEventDetail
import VisitorExploreEvent
import VisitorEventDetail
import VisitorExploreSite
import VisitorTransitDetail
import VisitorSiteDetail
import VisitorVisitHistory
import DataBaseManager
import validators
from datetime import datetime

def isValidEmail(email):
    return bool(validators.email(email))

def isFloat(num):
    try:
        val = float(num)
    except ValueError:
        return False
    return True

def setNone(element):
    return None if len(element) == 0 else element

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.LoginPage = LoginPage()
        self.RegisterNavigationPage = RegisterNavigationPage()
        self.RegisterUserPage = RegisterUser.Ui_Form()
        self.RegisterEmployeePage = RegisterEmployee.Ui_Form()
        self.RegisterEmployeeVisitorPage = RegisterEmployeeVisitor.Ui_Form()
        self.RegisterVisitorOnlyPage = RegisterVisitorOnly.Ui_Form()
        self.UserFunctionality = UserFunctionality.Ui_Form()
        self.AdministratorFunctionality = AdministratorFunctionality.Ui_Form()
        self.AdminVisitorFunctionality = AdminVisitorFunctionality.Ui_Form()
        self.ManagerFunctionality = ManagerFunctionality.Ui_Form()
        self.ManagerVisitorFunctionality = ManagerVisitorFunctionality.Ui_Form()
        self.StaffFunctionality = StaffFunctionality.Ui_Form()
        self.StaffVisitorFunctionality = StaffVisitorFunctionality.Ui_Form()
        self.VisitorFunctionality = VisitorFunctionality.Ui_Form()
        self.UserTakeTransit = UserTakeTransit.Ui_Form()
        self.UserTransitHistory = UserTransitHistory.Ui_Form()
        self.EmployeeManageProfile = EmployeeManageProfile.Ui_Form()
        self.AdministratorManageUser = AdministratorManagerUser.Ui_Form()
        self.AdministratorManageSite = AdministratorManageSite.Ui_Form()
        self.AdministratorEditSite = AdministratorEditSite.Ui_Form()
        self.AdministratorCreateSite = AdministratorCreateSite.Ui_Form()
        self.AdministratorManageTransit = AdministratorManageTransit.Ui_Form()
        self.AdministratorEditTransit = AdministratorEditTransit.Ui_Form()
        self.AdministratorCreateTransit = AdministratorCreateTransit.Ui_Form()
        self.ManagerManageEvent = ManagerManageEvent.Ui_Form()
        self.ManagerViewEditEvent = ManagerViewEditEvent.Ui_Form()
        self.ManagerCreateEvent = ManagerCreateEvent.Ui_Form()
        self.ManagerManageStaff = ManagerManageStaff.Ui_Form()
        self.ManagerSiteReport = ManagerSiteReport.Ui_Form()
        self.ManagerDailyDetail = ManagerDailyDetail.Ui_Form()
        self.StaffViewSchedule = StaffViewSchedule.Ui_Form()
        self.StaffEventDetail = StaffEventDetail.Ui_Form()
        self.VisitorExploreEvent = VisitorExploreEvent.Ui_Form()
        self.VisitorEventDetail = VisitorEventDetail.Ui_Form()
        self.VisitorExploreSite = VisitorExploreSite.Ui_Form()
        self.VisitorTransitDetail = VisitorTransitDetail.Ui_Form()
        self.VisitorSiteDetail = VisitorSiteDetail.Ui_Form()
        self.VisitorVisitHistory = VisitorVisitHistory.Ui_Form()

    def startRegisterNavigation(self, parent=None):
        self.RegisterNavigationPage.setupUi(self)
        self.show()

    def startLoginPage(self):
        self.LoginPage.setupUi(self)
        self.show()

    def startRegisterUser(self):
        self.RegisterUserPage.setupUi(self)
        self.show()

    def startRegisterVisitorOnly(self):
        self.RegisterVisitorOnlyPage.setupUi(self)
        self.show()

    def startRegisterEmployee(self):
        self.RegisterEmployeePage.setupUi(self)
        self.show()

    def startRegisterEmployeeVisitor(self):
        self.RegisterEmployeeVisitorPage.setupUi(self)
        self.show()

    def startUserFunctionality(self):
        self.UserFunctionality.setupUi(self)
        self.show()

    def startAdministratorFunctionality(self):
        self.AdministratorFunctionality.setupUi(self)
        self.show()

    def startAdminVisitorFunctionality(self):
        self.AdminVisitorFunctionality.setupUi(self)
        self.show()

    def startManagerFunctionality(self):
        self.ManagerFunctionality.setupUi(self)
        self.show()

    def startManagerVisitorFunctionality(self):
        self.ManagerVisitorFunctionality.setupUi(self)
        self.show()

    def startStaffFunctionality(self):
        self.StaffFunctionality.setupUi(self)
        self.show()

    def startStaffVisitorFunctionality(self):
        self.StaffVisitorFunctionality.setupUi(self)
        self.show()

    def startVisitorFunctionality(self):
        self.VisitorFunctionality.setupUi(self)
        self.show()

    def startUserTakeTransit(self):
        self.UserTakeTransit.setupUi(self)
        self.show()

    def startUserTransitHistory(self):
        self.UserTransitHistory.setupUi(self)
        self.show()

    def startEmployeeManageProfile(self):
        self.EmployeeManageProfile.setupUi(self)
        self.show()

    def startAdministratorManagerUser(self):
        self.AdministratorManageUser.setupUi(self)
        self.show()

    def startAdministratorManageSite(self):
        self.AdministratorManageSite.setupUi(self)
        self.show()

    def startAdministratorEditSite(self):
        self.AdministratorEditSite.setupUi(self)
        self.show()

    def startAdministratorCreateSite(self):
        self.AdministratorCreateSite.setupUi(self)
        self.show()

    def startAdministratorManageTransit(self):
        self.AdministratorManageTransit.setupUi(self)
        self.show()

    def startAdministratorEditTransit(self):
        self.AdministratorEditTransit.setupUi(self)
        self.show()

    def startAdministratorCreateTransit(self):
        self.AdministratorCreateTransit.setupUi(self)
        self.show()

    def startManagerManageEvent(self):
        self.ManagerManageEvent.setupUi(self)
        self.show()

    def startManagerViewEditEvent(self):
        self.ManagerViewEditEvent.setupUi(self)
        self.show()

    def startManagerCreateEvent(self):
        self.ManagerCreateEvent.setupUi(self)
        self.show()

    def startManagerManageStaff(self):
        self.ManagerManageStaff.setupUi(self)
        self.show()

    def startManagerSiteReport(self):
        self.ManagerSiteReport.setupUi(self)
        self.show()

    def startManagerDailyDetail(self):
        self.ManagerDailyDetail.setupUi(self)
        self.show()

    def startStaffViewSchedule(self):
        self.StaffViewSchedule.setupUi(self)
        self.show()

    def startStaffEventDetail(self):
        self.StaffEventDetail.setupUi(self)
        self.show()

    def startVisitorExploreEvent(self):
        self.VisitorExploreEvent.setupUi(self)
        self.show()

    def startVisitorEventDetail(self):
        self.VisitorEventDetail.setupUi(self)
        self.show()

    def startVisitorExploreSite(self):
        self.VisitorExploreSite.setupUi(self)
        self.show()

    def startVisitorTransitDetail(self):
        self.VisitorTransitDetail.setupUi(self)
        self.show()

    def startVisitorSiteDetail(self):
        self.VisitorSiteDetail.setupUi(self)
        self.show()

    def startVisitorVisitHistory(self):
        self.VisitorVisitHistory.setupUi(self)
        self.show()


class Controller():
    def __init__(self):
        self.MainWindow = MainWindow()
        self.user = None
        self.username = None
    
    def showLogin(self):
        self.MainWindow.close()
        self.MainWindow = MainWindow()
        self.MainWindow.startLoginPage()
        self.MainWindow.LoginPage.pushButton_2.clicked.connect(self.showRegisterNavigation)
        self.MainWindow.LoginPage.pushButton.clicked.connect(self.Login)

    def Login(self):
        email = self.MainWindow.LoginPage.lineEdit.text()
        password = self.MainWindow.LoginPage.lineEdit_2.text()
        if len(email) == 0:
            return QtWidgets.QMessageBox.warning(self.MainWindow, "Email not entered", "Email not entered.", QtWidgets.QMessageBox.Ok)
        if len(password) < 8:
            return QtWidgets.QMessageBox.warning(self.MainWindow, "Password not entered", "Password not entered", QtWidgets.QMessageBox.Ok)
        found = DataBaseManager.Login(email, password)
        if found:
            self.username = found['username']
            if found['user_status'] != 'Approved':
                return QtWidgets.QMessageBox.warning(self.MainWindow, "User not Approved", "User not Approved", QtWidgets.QMessageBox.Ok)
            if not found['is_employee'] and not found['is_visitor']:
                self.user = 'User'
                self.showUserFunctionality()
            elif found['is_employee'] and not found['is_visitor']:
                employee = DataBaseManager.SearchEmployeeType(found['username'])
                self.user = employee['erole']
                if employee['erole'] == 'Staff':
                    self.showStaffFunctionality()
                elif employee['erole'] == 'Manager':
                    self.showManagerFunctionality()
                elif employee['erole'] == 'Administrator':
                    self.showAdministratorFunctionality()
            elif found['is_employee'] and found['is_visitor']:
                employee = DataBaseManager.SearchEmployeeType(found['username'])
                self.user = employee['erole'] + 'Visitor'
                if employee['erole'] == 'Staff':
                    self.showStaffVisitorFunctionality()
                elif employee['erole'] == 'Manager':
                    self.showManagerVisitorFunctionality()
                elif employee['erole'] == 'Administrator':
                    self.showAdminVisitorFunctionality()
            elif found['is_visitor']:
                self.user = 'Visitor'
                self.showVisitorFunctionality()
        else:
            return QtWidgets.QMessageBox.warning(self.MainWindow, "User not found", "User not found. Please register before you log in.", QtWidgets.QMessageBox.Ok)


    def showRegisterNavigation(self):
        self.MainWindow.close()
        self.MainWindow = MainWindow()
        self.MainWindow.startRegisterNavigation()
        self.MainWindow.RegisterNavigationPage.pushButton.clicked.connect(self.showRegisterUser)
        self.MainWindow.RegisterNavigationPage.pushButton_2.clicked.connect(self.showRegisterVisitorOnly)
        self.MainWindow.RegisterNavigationPage.pushButton_3.clicked.connect(self.showRegisterEmployee)
        self.MainWindow.RegisterNavigationPage.pushButton_4.clicked.connect(self.showRegisterEmployeeVisitor)
        self.MainWindow.RegisterNavigationPage.pushButton_5.clicked.connect(self.showLogin)

    def showRegisterUser(self):
        self.MainWindow.close()
        self.MainWindow = MainWindow()
        self.MainWindow.startRegisterUser()
        self.MainWindow.RegisterUserPage.pushButton_2.clicked.connect(self.showRegisterNavigation)
        self.MainWindow.RegisterUserPage.pushButton_3.clicked.connect(self.RegisterUser)

    def RegisterUser(self):
        Fname = self.MainWindow.RegisterUserPage.lineEdit.text()
        Lname = self.MainWindow.RegisterUserPage.lineEdit_2.text()
        Username = self.MainWindow.RegisterUserPage.lineEdit_3.text()
        Password = self.MainWindow.RegisterUserPage.lineEdit_4.text()
        CPassword = self.MainWindow.RegisterUserPage.lineEdit_5.text()
        Emails = []
        for email in self.MainWindow.RegisterUserPage.EditLineList:
            Emails.append(email.text())
        if len(Fname) == 0 or len(Lname) == 0 or len(Username) == 0 or len(Password) == 0 or len(Emails) == 0:
            return QtWidgets.QMessageBox.warning(self.MainWindow, "Missing Field", "There are missing fields", QtWidgets.QMessageBox.Ok)
        if Password != CPassword:
            return QtWidgets.QMessageBox.warning(self.MainWindow, "Password not match", "Please confirm your password", QtWidgets.QMessageBox.Ok)
        for email in Emails:
            if not isValidEmail(email):
                return QtWidgets.QMessageBox.warning(self.MainWindow, "Email not valid", "Please confirm your email", QtWidgets.QMessageBox.Ok)
            if not DataBaseManager.IsEmailUnique(email):
                return QtWidgets.QMessageBox.warning(self.MainWindow, "Email already registered", "Please use a new email", QtWidgets.QMessageBox.Ok)
        if not DataBaseManager.IsUsernameUnique(Username):
            return QtWidgets.QMessageBox.warning(self.MainWindow, "Username not unique", "Please use a new username", QtWidgets.QMessageBox.Ok)
        DataBaseManager.RegisterUser(Fname, Lname, Username, DataBaseManager.encrypt_password(Password), Emails)
        self.showLogin()

    def showRegisterVisitorOnly(self):
        self.MainWindow.close()
        self.MainWindow = MainWindow()
        self.MainWindow.startRegisterVisitorOnly()
        self.MainWindow.RegisterVisitorOnlyPage.pushButton_2.clicked.connect(self.showRegisterNavigation)
        self.MainWindow.RegisterVisitorOnlyPage.pushButton_3.clicked.connect(self.RegisterVisitor)

    def RegisterVisitor(self):
        Fname = self.MainWindow.RegisterVisitorOnlyPage.lineEdit.text()
        Lname = self.MainWindow.RegisterVisitorOnlyPage.lineEdit_2.text()
        Username = self.MainWindow.RegisterVisitorOnlyPage.lineEdit_3.text()
        Password = self.MainWindow.RegisterVisitorOnlyPage.lineEdit_4.text()
        CPassword = self.MainWindow.RegisterVisitorOnlyPage.lineEdit_5.text()
        Emails = []
        for email in self.MainWindow.RegisterVisitorOnlyPage.EditLineList:
            Emails.append(email.text())
        if len(Fname) == 0 or len(Lname) == 0 or len(Username) == 0 or len(Password) == 0 or len(Emails) == 0:
            return QtWidgets.QMessageBox.warning(self.MainWindow, "Missing Field", "There are missing fields", QtWidgets.QMessageBox.Ok)
        if Password != CPassword or len(Password) < 8:
            return QtWidgets.QMessageBox.warning(self.MainWindow, "Password not match", "Please confirm your password", QtWidgets.QMessageBox.Ok)
        for email in Emails:
            if not isValidEmail(email):
                return QtWidgets.QMessageBox.warning(self.MainWindow, "Email not valid", "Please confirm your email", QtWidgets.QMessageBox.Ok)
            if not DataBaseManager.IsEmailUnique(email):
                return QtWidgets.QMessageBox.warning(self.MainWindow, "Email already registered", "Please use a new email", QtWidgets.QMessageBox.Ok)
        if not DataBaseManager.IsUsernameUnique(Username):
            return QtWidgets.QMessageBox.warning(self.MainWindow, "Username not unique", "Please use a new username", QtWidgets.QMessageBox.Ok)
        DataBaseManager.RegisterVisitor(Fname, Lname, Username, DataBaseManager.encrypt_password(Password), Emails)
        self.showLogin()

    def showRegisterEmployee(self):
        self.MainWindow.close()
        self.MainWindow = MainWindow()
        self.MainWindow.startRegisterEmployee()
        self.MainWindow.RegisterEmployeePage.pushButton_2.clicked.connect(self.showRegisterNavigation)
        states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA",
                  "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
                  "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
                  "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
                  "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY", "Other"]
        self.MainWindow.RegisterEmployeePage.comboBox_2.addItems(states)
        self.MainWindow.RegisterEmployeePage.comboBox.addItems(["Manager", "Staff"])
        self.MainWindow.RegisterEmployeePage.pushButton_3.clicked.connect(self.RegisterEmployee)

    def generate_unique_employee_id(self):
        current_employee_id = random.randint(0, 999999999)
        while not DataBaseManager.IsEmployeeIdUnique(current_employee_id):
            current_employee_id = random.randint(0, 999999999)
        return current_employee_id

    def RegisterEmployee(self):
        Fname = self.MainWindow.RegisterEmployeePage.lineEdit_2.text()
        Lname = self.MainWindow.RegisterEmployeePage.lineEdit_3.text()
        Username = self.MainWindow.RegisterEmployeePage.lineEdit_5.text()
        Password = self.MainWindow.RegisterEmployeePage.lineEdit_4.text()
        CPassword = self.MainWindow.RegisterEmployeePage.lineEdit_7.text()
        Phone = self.MainWindow.RegisterEmployeePage.lineEdit_8.text()
        Address = self.MainWindow.RegisterEmployeePage.lineEdit_9.text()
        Zipcode = self.MainWindow.RegisterEmployeePage.lineEdit_11.text()
        City = self.MainWindow.RegisterEmployeePage.lineEdit_10.text()
        State = self.MainWindow.RegisterEmployeePage.comboBox_2.currentText()
        Erole = self.MainWindow.RegisterEmployeePage.comboBox.currentText()
        Emails = []
        for email in self.MainWindow.RegisterEmployeePage.EditLineList:
            Emails.append(email.text())
        if len(Fname) == 0 or len(Lname) == 0 or len(Username) == 0 or len(Password) == 0 or len(Emails) == 0:
            return QtWidgets.QMessageBox.warning(self.MainWindow, "Missing Field", "There are missing fields", QtWidgets.QMessageBox.Ok)
        if len(Password) < 8 and Password != CPassword:
            return QtWidgets.QMessageBox.warning(self.MainWindow, "Password not match", "Please confirm your password", QtWidgets.QMessageBox.Ok)
        for email in Emails:
            if not isValidEmail(email):
                return QtWidgets.QMessageBox.warning(self.MainWindow, "Email not valid", "Please confirm your email", QtWidgets.QMessageBox.Ok)
            if not DataBaseManager.IsEmailUnique(email):
                return QtWidgets.QMessageBox.warning(self.MainWindow, "Email already registered", "Please use a new email", QtWidgets.QMessageBox.Ok)
        if not Phone.isdigit() or len(Phone) != 10:
            return QtWidgets.QMessageBox.warning(self.MainWindow, "Phone not valid", "Please confirm your phone", QtWidgets.QMessageBox.Ok)
        if not Zipcode.isdigit() or len(Zipcode) > 5:
            return QtWidgets.QMessageBox.warning(self.MainWindow, "Zipcode not valid", "Please confirm your zipcode", QtWidgets.QMessageBox.Ok)
        if not DataBaseManager.IsPhoneUnique(int(Phone)):
            return QtWidgets.QMessageBox.warning(self.MainWindow, "Phone already used", "Please use a new phone", QtWidgets.QMessageBox.Ok)
        if not DataBaseManager.IsUsernameUnique(Username):
            return QtWidgets.QMessageBox.warning(self.MainWindow, "Username not unique", "Please use a new username", QtWidgets.QMessageBox.Ok)
        DataBaseManager.RegisterEmployeeVisitor(Fname, Lname, Username, DataBaseManager.encrypt_password(Password), Emails, self.generate_unique_employee_id(), int(Phone), Address, City, State, int(Zipcode), Erole)
        self.showLogin()

    def showRegisterEmployeeVisitor(self):
        self.MainWindow.close()
        self.MainWindow = MainWindow()
        self.MainWindow.startRegisterEmployeeVisitor()
        self.MainWindow.RegisterEmployeeVisitorPage.pushButton_2.clicked.connect(self.showRegisterNavigation)
        states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA",
                  "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD",
                  "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
                  "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC",
                  "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]
        self.MainWindow.RegisterEmployeeVisitorPage.comboBox_2.addItems(states)
        self.MainWindow.RegisterEmployeeVisitorPage.comboBox.addItems(["Manager", "Staff"])
        self.MainWindow.RegisterEmployeeVisitorPage.pushButton_3.clicked.connect(self.RegisterEmployeeVisitor)

    def RegisterEmployeeVisitor(self):
        Fname = self.MainWindow.RegisterEmployeeVisitorPage.lineEdit_2.text()
        Lname = self.MainWindow.RegisterEmployeeVisitorPage.lineEdit_3.text()
        Username = self.MainWindow.RegisterEmployeeVisitorPage.lineEdit_5.text()
        Password = self.MainWindow.RegisterEmployeeVisitorPage.lineEdit_4.text()
        CPassword = self.MainWindow.RegisterEmployeeVisitorPage.lineEdit_7.text()
        Phone = self.MainWindow.RegisterEmployeeVisitorPage.lineEdit_8.text()
        Address = self.MainWindow.RegisterEmployeeVisitorPage.lineEdit_9.text()
        Zipcode = self.MainWindow.RegisterEmployeeVisitorPage.lineEdit_11.text()
        City = self.MainWindow.RegisterEmployeeVisitorPage.lineEdit_10.text()
        State = self.MainWindow.RegisterEmployeeVisitorPage.comboBox_2.currentText()
        Erole = self.MainWindow.RegisterEmployeeVisitorPage.comboBox.currentText()
        Emails = []
        for email in self.MainWindow.RegisterEmployeeVisitorPage.EditLineList:
            Emails.append(email.text())
        if len(Fname) == 0 or len(Lname) == 0 or len(Username) == 0 or len(Password) == 0 or len(Emails) == 0:
            return QtWidgets.QMessageBox.warning(self.MainWindow, "Missing Field", "There are missing fields", QtWidgets.QMessageBox.Ok)
        if len(Password) < 8 and Password != CPassword:
            return QtWidgets.QMessageBox.warning(self.MainWindow, "Password not match", "Please confirm your password", QtWidgets.QMessageBox.Ok)
        for email in Emails:
            if not isValidEmail(email):
                return QtWidgets.QMessageBox.warning(self.MainWindow, "Email not valid", "Please confirm your email", QtWidgets.QMessageBox.Ok)
            if not DataBaseManager.IsEmailUnique(email):
                return QtWidgets.QMessageBox.warning(self.MainWindow, "Email already registered", "Please use a new email", QtWidgets.QMessageBox.Ok)
        if not Phone.isdigit() or len(Phone) != 10:
            return QtWidgets.QMessageBox.warning(self.MainWindow, "Phone not valid", "Please confirm your phone", QtWidgets.QMessageBox.Ok)
        if not DataBaseManager.IsPhoneUnique(int(Phone)):
            return QtWidgets.QMessageBox.warning(self.MainWindow, "Phone not valid", "Please confirm your phone", QtWidgets.QMessageBox.Ok)
        if not Zipcode.isdigit():
            return QtWidgets.QMessageBox.warning(self.MainWindow, "Zipcode not valid", "Please confirm your zipcode", QtWidgets.QMessageBox.Ok)
        if not DataBaseManager.IsUsernameUnique(Username):
            return QtWidgets.QMessageBox.warning(self.MainWindow, "Username not unique", "Please use a new username", QtWidgets.QMessageBox.Ok)
        DataBaseManager.RegisterEmployeeVisitor(Fname, Lname, Username, DataBaseManager.encrypt_password(Password), Emails, self.generate_unique_employee_id(), int(Phone), Address, City, State, int(Zipcode), Erole)
        self.showLogin()

    def showUserFunctionality(self):
        self.MainWindow.close()
        self.MainWindow = MainWindow()
        self.MainWindow.startUserFunctionality()
        self.MainWindow.UserFunctionality.pushButton_3.clicked.connect(self.showLogin)
        self.MainWindow.UserFunctionality.pushButton.clicked.connect(self.showUserTakeTransit)
        self.MainWindow.UserFunctionality.pushButton_2.clicked.connect(self.showUserTransitHistory)


    def showAdministratorFunctionality(self):
        self.MainWindow.close()
        self.MainWindow = MainWindow()
        self.MainWindow.startAdministratorFunctionality()
        self.MainWindow.AdministratorFunctionality.pushButton.clicked.connect(self.showEmployeeManageProfile)
        self.MainWindow.AdministratorFunctionality.pushButton_2.clicked.connect(self.showUserTakeTransit)
        self.MainWindow.AdministratorFunctionality.pushButton_3.clicked.connect(self.showAdministratorManagerUser)
        self.MainWindow.AdministratorFunctionality.pushButton_4.clicked.connect(self.showUserTransitHistory)
        self.MainWindow.AdministratorFunctionality.pushButton_5.clicked.connect(self.showAdministratorManageTransit)
        self.MainWindow.AdministratorFunctionality.pushButton_6.clicked.connect(self.showLogin)
        self.MainWindow.AdministratorFunctionality.pushButton_7.clicked.connect(self.showAdministratorManageSite)

    def showAdminVisitorFunctionality(self):
        self.MainWindow.close()
        self.MainWindow = MainWindow()
        self.MainWindow.startAdminVisitorFunctionality()
        self.MainWindow.AdminVisitorFunctionality.pushButton.clicked.connect(self.showEmployeeManageProfile)
        self.MainWindow.AdminVisitorFunctionality.pushButton_3.clicked.connect(self.showAdministratorManagerUser)
        self.MainWindow.AdminVisitorFunctionality.pushButton_7.clicked.connect(self.showAdministratorManageSite)
        self.MainWindow.AdminVisitorFunctionality.pushButton_2.clicked.connect(self.showUserTakeTransit)
        self.MainWindow.AdminVisitorFunctionality.pushButton_4.clicked.connect(self.showUserTransitHistory)
        self.MainWindow.AdminVisitorFunctionality.pushButton_6.clicked.connect(self.showLogin)
        self.MainWindow.AdminVisitorFunctionality.pushButton_5.clicked.connect(self.showAdministratorManageTransit)
        self.MainWindow.AdminVisitorFunctionality.pushButton_8.clicked.connect(self.showVisitorExploreSite)
        self.MainWindow.AdminVisitorFunctionality.pushButton_9.clicked.connect(self.showManagerManageEvent)
        self.MainWindow.AdminVisitorFunctionality.pushButton_10.clicked.connect(self.showVisitorVisitHistory)

    def showManagerFunctionality(self):
        self.MainWindow.close()
        self.MainWindow = MainWindow()
        self.MainWindow.startManagerFunctionality()
        self.MainWindow.ManagerFunctionality.pushButton_3.clicked.connect(self.showManagerManageEvent)
        self.MainWindow.ManagerFunctionality.pushButton_7.clicked.connect(self.showUserTakeTransit)
        self.MainWindow.ManagerFunctionality.pushButton_2.clicked.connect(self.showManagerSiteReport)
        self.MainWindow.ManagerFunctionality.pushButton.clicked.connect(self.showEmployeeManageProfile)
        self.MainWindow.ManagerFunctionality.pushButton_4.clicked.connect(self.showUserTransitHistory)
        self.MainWindow.ManagerFunctionality.pushButton_6.clicked.connect(self.showLogin)
        self.MainWindow.ManagerFunctionality.pushButton_5.clicked.connect(self.showManagerManageStaff)


    def showManagerVisitorFunctionality(self):
        self.MainWindow.close()
        self.MainWindow = MainWindow()
        self.MainWindow.startManagerVisitorFunctionality()
        self.MainWindow.ManagerVisitorFunctionality.pushButton_3.clicked.connect(self.showManagerManageEvent)
        self.MainWindow.ManagerVisitorFunctionality.pushButton_8.clicked.connect(self.showUserTakeTransit)
        self.MainWindow.ManagerVisitorFunctionality.pushButton_2.clicked.connect(self.showManagerManageStaff)
        self.MainWindow.ManagerVisitorFunctionality.pushButton.clicked.connect(self.showEmployeeManageProfile)
        self.MainWindow.ManagerVisitorFunctionality.pushButton_9.clicked.connect(self.showUserTransitHistory)
        self.MainWindow.ManagerVisitorFunctionality.pushButton_6.clicked.connect(self.showLogin)
        self.MainWindow.ManagerVisitorFunctionality.pushButton_4.clicked.connect(self.showVisitorExploreEvent)
        self.MainWindow.ManagerVisitorFunctionality.pushButton_10.clicked.connect(self.showVisitorVisitHistory)
        self.MainWindow.ManagerVisitorFunctionality.pushButton_5.clicked.connect(self.showVisitorExploreSite)
        self.MainWindow.ManagerVisitorFunctionality.pushButton_7.clicked.connect(self.showManagerSiteReport)


    def showStaffFunctionality(self):
        self.MainWindow.close()
        self.MainWindow = MainWindow()
        self.MainWindow.startStaffFunctionality()
        self.MainWindow.StaffFunctionality.pushButton_8.clicked.connect(self.showEmployeeManageProfile)
        self.MainWindow.StaffFunctionality.pushButton.clicked.connect(self.showStaffViewSchedule)
        self.MainWindow.StaffFunctionality.pushButton_2.clicked.connect(self.showUserTakeTransit)
        self.MainWindow.StaffFunctionality.pushButton_3.clicked.connect(self.showUserTransitHistory)
        self.MainWindow.StaffFunctionality.pushButton_9.clicked.connect(self.showLogin)


    def showStaffVisitorFunctionality(self):
        self.MainWindow.close()
        self.MainWindow = MainWindow()
        self.MainWindow.startStaffVisitorFunctionality()
        self.MainWindow.StaffVisitorFunctionality.pushButton_8.clicked.connect(self.showEmployeeManageProfile)
        self.MainWindow.StaffVisitorFunctionality.pushButton.clicked.connect(self.showStaffViewSchedule)
        self.MainWindow.StaffVisitorFunctionality.pushButton_2.clicked.connect(self.showUserTakeTransit)
        self.MainWindow.StaffVisitorFunctionality.pushButton_3.clicked.connect(self.showUserTransitHistory)
        self.MainWindow.StaffVisitorFunctionality.pushButton_9.clicked.connect(self.showLogin)
        self.MainWindow.StaffVisitorFunctionality.pushButton_10.clicked.connect(self.showVisitorExploreEvent)
        self.MainWindow.StaffVisitorFunctionality.pushButton_11.clicked.connect(self.showVisitorExploreSite)
        self.MainWindow.StaffVisitorFunctionality.pushButton_4.clicked.connect(self.showVisitorVisitHistory)


    def showVisitorFunctionality(self):
        self.MainWindow.close()
        self.MainWindow = MainWindow()
        self.MainWindow.startVisitorFunctionality()
        self.MainWindow.VisitorFunctionality.pushButton_9.clicked.connect(self.showLogin)
        self.MainWindow.VisitorFunctionality.pushButton_2.clicked.connect(self.showUserTakeTransit)
        self.MainWindow.VisitorFunctionality.pushButton_3.clicked.connect(self.showVisitorVisitHistory)
        self.MainWindow.VisitorFunctionality.pushButton_8.clicked.connect(self.showVisitorExploreEvent)
        self.MainWindow.VisitorFunctionality.pushButton.clicked.connect(self.showVisitorExploreSite)
        self.MainWindow.VisitorFunctionality.pushButton_4.clicked.connect(self.showUserTransitHistory)


    def showUserTakeTransit(self):
        self.MainWindow.close()
        self.MainWindow = MainWindow()
        self.MainWindow.startUserTakeTransit()
        if self.user == 'User':
            self.MainWindow.UserTakeTransit.pushButton_2.clicked.connect(self.showUserFunctionality)
        elif self.user == "Staff":
            self.MainWindow.UserTakeTransit.pushButton_2.clicked.connect(self.showStaffFunctionality)
        elif self.user == 'Manager':
            self.MainWindow.UserTakeTransit.pushButton_2.clicked.connect(self.showManagerFunctionality)
        elif self.user == 'Administrator':
            self.MainWindow.UserTakeTransit.pushButton_2.clicked.connect(self.showAdministratorFunctionality)
        elif self.user == 'StaffVisitor':
            self.MainWindow.UserTakeTransit.pushButton_2.clicked.connect(self.showStaffVisitorFunctionality)
        elif self.user == 'ManagerVisitor':
            self.MainWindow.UserTakeTransit.pushButton_2.clicked.connect(self.showManagerVisitorFunctionality)
        elif self.user == 'AdministratorVisitor':
            self.MainWindow.UserTakeTransit.pushButton_2.clicked.connect(self.showAdminVisitorFunctionality)
        elif self.user == 'Visitor':
            self.MainWindow.UserTakeTransit.pushButton_2.clicked.connect(self.showVisitorFunctionality)
        allSites = ['All']
        self.MainWindow.UserTakeTransit.pushButton.clicked.connect(self.filterUserTransit)
        self.MainWindow.UserTakeTransit.comboBox_2.addItems(["All", "MARTA", "Bus", "Bike"])
        allSitesFromDB = DataBaseManager.GetAllSiteNameFromConnect()
        for site in allSitesFromDB:
            allSites.append(site['connect_name'])
        self.MainWindow.UserTakeTransit.comboBox.addItems(allSites)
        self.MainWindow.UserTakeTransit.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.MainWindow.UserTakeTransit.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.MainWindow.UserTakeTransit.pushButton_3.clicked.connect(self.LogUserTransit)
        self.MainWindow.UserTakeTransit.dateEdit.setDate(QtCore.QDate.currentDate())

    def filterUserTransit(self):
        self.MainWindow.UserTakeTransit.tableWidget.setRowCount(0)
        containSite = self.MainWindow.UserTakeTransit.comboBox.currentText()
        transportType = self.MainWindow.UserTakeTransit.comboBox_2.currentText()
        LowRange = self.MainWindow.UserTakeTransit.lineEdit.text()
        HighRange = self.MainWindow.UserTakeTransit.lineEdit.text()
        if containSite == 'All':
            containSite = None
        if transportType == 'All':
            transportType = None
        if (len(LowRange) != 0 and len(HighRange) == 0) or (len(LowRange) != 0 and len(HighRange) == 0):
            return QtWidgets.QMessageBox.warning(self.MainWindow, "Range not valid", "Please enter both ranges", QtWidgets.QMessageBox.Ok)
        if ((len(LowRange) != 0) and not isFloat(LowRange)) or ((len(HighRange) != 0) and not isFloat(HighRange)):
            return QtWidgets.QMessageBox.warning(self.MainWindow, "Range not valid", "You could only enter digits", QtWidgets.QMessageBox.Ok)
        tableData = None
        if len(LowRange) == 0 and len(HighRange) == 0:
            LowRange = None
            HighRange = None
            tableData = DataBaseManager.GetAllRoutesForTakeTransit(transportType, containSite, LowRange, HighRange)
        else:
            tableData = DataBaseManager.GetAllRoutesForTakeTransit(transportType, containSite, float(LowRange), float(HighRange))
        self.MainWindow.UserTakeTransit.tableWidget.setSortingEnabled(False)
        for i in range(len(tableData)):
            self.MainWindow.UserTakeTransit.tableWidget.insertRow(i)
            for column, key in enumerate(tableData[i].keys()):
                newItem = QtWidgets.QTableWidgetItem()
                newItem.setText(str(tableData[i][key]))
                self.MainWindow.UserTakeTransit.tableWidget.setItem(i, column, newItem)
        self.MainWindow.UserTakeTransit.tableWidget.setSortingEnabled(True)

    def LogUserTransit(self):
        Route = self.MainWindow.UserTakeTransit.tableWidget.selectionModel().selectedRows()[0]
        TransitDate = self.MainWindow.UserTakeTransit.dateEdit.date().toPyDate()
        TakeType = self.MainWindow.UserTakeTransit.tableWidget.item(Route.row(), 1).text()
        TakeRoute = self.MainWindow.UserTakeTransit.tableWidget.item(Route.row(), 0).text()
        DataBaseManager.UserTakeTransitLogNewTransit(self.username, TakeType, TakeRoute, TransitDate)

    def showUserTransitHistory(self):
        self.MainWindow.close()
        self.MainWindow = MainWindow()
        self.MainWindow.startUserTransitHistory()
        if self.user == 'User':
            self.MainWindow.UserTransitHistory.pushButton_2.clicked.connect(self.showUserFunctionality)
        elif self.user == "Staff":
            self.MainWindow.UserTransitHistory.pushButton_2.clicked.connect(self.showStaffFunctionality)
        elif self.user == 'Manager':
            self.MainWindow.UserTransitHistory.pushButton_2.clicked.connect(self.showManagerFunctionality)
        elif self.user == 'Administrator':
            self.MainWindow.UserTransitHistory.pushButton_2.clicked.connect(self.showAdministratorFunctionality)
        elif self.user == 'StaffVisitor':
            self.MainWindow.UserTransitHistory.pushButton_2.clicked.connect(self.showStaffVisitorFunctionality)
        elif self.user == 'ManagerVisitor':
            self.MainWindow.UserTransitHistory.pushButton_2.clicked.connect(self.showManagerVisitorFunctionality)
        elif self.user == 'AdministratorVisitor':
            self.MainWindow.UserTransitHistory.pushButton_2.clicked.connect(self.showAdminVisitorFunctionality)
        elif self.user == 'Visitor':
            self.MainWindow.UserTransitHistory.pushButton_2.clicked.connect(self.showVisitorFunctionality)
        allSites = ['All']
        allSitesFromDB = DataBaseManager.GetAllSiteNameFromConnect()
        for site in allSitesFromDB:
            allSites.append(site['connect_name'])
        self.MainWindow.UserTransitHistory.comboBox.addItems(allSites)
        self.MainWindow.UserTransitHistory.comboBox_2.addItems(["All", "MARTA", "Bus", "Bike"])
        self.MainWindow.UserTransitHistory.pushButton.clicked.connect(self.filterTransitHistory)
        self.MainWindow.UserTransitHistory.dateEdit.setDate(QtCore.QDate.currentDate())
        self.MainWindow.UserTransitHistory.dateEdit_2.setDate(QtCore.QDate.currentDate())

    def filterTransitHistory(self):
        self.MainWindow.UserTransitHistory.tableWidget.setRowCount(0)
        containSite = self.MainWindow.UserTransitHistory.comboBox.currentText()
        transportType = self.MainWindow.UserTransitHistory.comboBox_2.currentText()
        startDate = self.MainWindow.UserTransitHistory.dateEdit.date().toPyDate()
        endDate = self.MainWindow.UserTransitHistory.dateEdit_2.date().toPyDate()
        Route = self.MainWindow.UserTransitHistory.lineEdit.text()
        if transportType == 'All':
            transportType = None
        if containSite == 'All':
            containSite = None
        if len(Route) == 0:
            Route = None
        tableData = DataBaseManager.GetUserTransitHistoryFilteredByTransportType_Route_StartDate_EndDate_ContainSite(self.username, transportType, Route, startDate, endDate, containSite)
        self.MainWindow.UserTransitHistory.tableWidget.setSortingEnabled(False)
        for i in range(len(tableData)):
            self.MainWindow.UserTransitHistory.tableWidget.insertRow(i)
            for column, key in enumerate(tableData[i].keys()):
                newItem = QtWidgets.QTableWidgetItem()
                newItem.setText(str(tableData[i][key]))
                self.MainWindow.UserTransitHistory.tableWidget.setItem(i, column, newItem)
        self.MainWindow.UserTransitHistory.tableWidget.setSortingEnabled(True)

    def showEmployeeManageProfile(self):
        self.MainWindow.close()
        self.MainWindow = MainWindow()
        self.MainWindow.startEmployeeManageProfile()
        if self.user == 'User':
            self.MainWindow.EmployeeManageProfile.pushButton_3.clicked.connect(self.showUserFunctionality)
        elif self.user == "Staff":
            self.MainWindow.EmployeeManageProfile.pushButton_3.clicked.connect(self.showStaffFunctionality)
        elif self.user == 'Manager':
            self.MainWindow.EmployeeManageProfile.pushButton_3.clicked.connect(self.showManagerFunctionality)
        elif self.user == 'Administrator':
            self.MainWindow.EmployeeManageProfile.pushButton_3.clicked.connect(self.showAdministratorFunctionality)
        elif self.user == 'StaffVisitor':
            self.MainWindow.EmployeeManageProfile.pushButton_3.clicked.connect(self.showStaffVisitorFunctionality)
        elif self.user == 'ManagerVisitor':
            self.MainWindow.EmployeeManageProfile.pushButton_3.clicked.connect(self.showManagerVisitorFunctionality)
        elif self.user == 'AdministratorVisitor':
            self.MainWindow.EmployeeManageProfile.pushButton_3.clicked.connect(self.showAdminVisitorFunctionality)
        elif self.user == 'Visitor':
            self.MainWindow.EmployeeManageProfile.pushButton_3.clicked.connect(self.showVisitorFunctionality)
        self.MainWindow.EmployeeManageProfile.pushButton_2.clicked.connect(self.updateEmployeeProfile)
        tableData = DataBaseManager.GetEmployeeInformationForManageProfile(self.username)
        self.MainWindow.EmployeeManageProfile.lineEdit.setText(tableData[0]['fname'])
        self.MainWindow.EmployeeManageProfile.lineEdit_2.setText(tableData[0]['lname'])
        self.MainWindow.EmployeeManageProfile.lineEdit_3.setText(str(tableData[1]['phone']))
        self.MainWindow.EmployeeManageProfile.label_6.setText(self.username)
        self.MainWindow.EmployeeManageProfile.label_10.setText(str(tableData[1]['employee_id']))
        if tableData[2]:
            self.MainWindow.EmployeeManageProfile.label_7.setText(tableData[2]['sitename'])
        else:
            self.MainWindow.EmployeeManageProfile.label_7.setText("")
        self.MainWindow.EmployeeManageProfile.label_13.setText(tableData[1]['address'])
        Emails = DataBaseManager.GetAllEmailsOfUser(self.username)
        for email in Emails:
            line_text = QtWidgets.QLineEdit(self.MainWindow.EmployeeManageProfile.widget)
            line_text.setText(email['email'])
            self.MainWindow.EmployeeManageProfile.EditLineList.append(line_text)
            line_text.setGeometry(QtCore.QRect(20, 10, 301, 25))
            self.MainWindow.EmployeeManageProfile.inner.layout().addWidget(line_text)
            new_button = QtWidgets.QPushButton(self.MainWindow.EmployeeManageProfile.widget)
            self.MainWindow.EmployeeManageProfile.EmailRemoveButtons.append(new_button)
            new_button.setText("Remove")
            self.MainWindow.EmployeeManageProfile.inner.layout().addWidget(new_button)
            # since we can't pass arguments into .connect, we pass in the lambda as a func
            new_button.clicked.connect(lambda: self.MainWindow.EmployeeManageProfile.removeEmail(new_button))
        if tableData[0]['is_visitor']:
            self.MainWindow.EmployeeManageProfile.checkBox.setChecked(True)
        else:
            self.MainWindow.EmployeeManageProfile.checkBox.setChecked(False)

    def updateEmployeeProfile(self):
        Fname = self.MainWindow.EmployeeManageProfile.lineEdit.text()
        Lname = self.MainWindow.EmployeeManageProfile.lineEdit_2.text()
        Phone = self.MainWindow.EmployeeManageProfile.lineEdit_3.text()
        Emails = []
        Employee_id = self.MainWindow.EmployeeManageProfile.label_10.text()
        for email in self.MainWindow.RegisterUserPage.EditLineList:
            Emails.append(email.text())
        if self.MainWindow.EmployeeManageProfile.lineEdit_3.isModified() and not Phone.isdigit():
            return QtWidgets.QMessageBox.warning(self.MainWindow, "Phone not valid", "Please confirm your phone",
                                                 QtWidgets.QMessageBox.Ok)
        if self.MainWindow.EmployeeManageProfile.lineEdit_3.isModified() and not DataBaseManager.IsPhoneUnique(int(Phone)):
            return QtWidgets.QMessageBox.warning(self.MainWindow, "Phone already used", "Please use a new phone",
                                                 QtWidgets.QMessageBox.Ok)
        for email in Emails:
            if not isValidEmail(email):
                return QtWidgets.QMessageBox.warning(self.MainWindow, "Email not valid", "Please confirm your email",
                                                     QtWidgets.QMessageBox.Ok)
            if not DataBaseManager.IsEmailUnique(email):
                return QtWidgets.QMessageBox.warning(self.MainWindow, "Email already registered",
                                                     "Please use a new email", QtWidgets.QMessageBox.Ok)
        DataBaseManager.UpdateUserInformation(self.username, Fname, Lname, self.MainWindow.EmployeeManageProfile.checkBox.isChecked(), int(Phone), Employee_id)

    def showAdministratorManagerUser(self):
        self.MainWindow.close()
        self.MainWindow = MainWindow()
        self.MainWindow.startAdministratorManagerUser()
        if self.user == 'User':
            self.MainWindow.AdministratorManagerUser.pushButton_4.clicked.connect(self.showUserFunctionality)
        elif self.user == "Staff":
            self.MainWindow.AdministratorManagerUser.pushButton_4.clicked.connect(self.showStaffFunctionality)
        elif self.user == 'Manager':
            self.MainWindow.AdministratorManageUser.pushButton_4.clicked.connect(self.showManagerFunctionality)
        elif self.user == 'Administrator':
            self.MainWindow.AdministratorManageUser.pushButton_4.clicked.connect(self.showAdministratorFunctionality)
        elif self.user == 'StaffVisitor':
            self.MainWindow.AdministratorManageUser.pushButton_4.clicked.connect(self.showStaffVisitorFunctionality)
        elif self.user == 'ManagerVisitor':
            self.MainWindow.AdministratorManageUser.pushButton_4.clicked.connect(self.showManagerVisitorFunctionality)
        elif self.user == 'AdministratorVisitor':
            self.MainWindow.AdministratorManageUser.pushButton_4.clicked.connect(self.showAdminVisitorFunctionality)
        elif self.user == 'Visitor':
            self.MainWindow.AdministratorManagerUser.pushButton_4.clicked.connect(self.showVisitorFunctionality)
        self.MainWindow.AdministratorManageUser.comboBox_2.addItems(["Approved", "Pending", "Declined", "All"])
        self.MainWindow.AdministratorManageUser.comboBox.addItems(["All", "Manager", "User", "Visitor", "Staff"])
        self.MainWindow.AdministratorManageUser.pushButton.clicked.connect(self.filterUsers)
        self.MainWindow.AdministratorManageUser.pushButton_2.clicked.connect(self.approveUsers)
        self.MainWindow.AdministratorManageUser.pushButton_3.clicked.connect(self.declineUsers)
        self.MainWindow.AdministratorManageUser.tableWidget.setSelectionMode(
            QtWidgets.QAbstractItemView.SingleSelection)
        self.MainWindow.AdministratorManageUser.tableWidget.setSelectionBehavior(
            QtWidgets.QAbstractItemView.SelectRows)

    def approveUsers(self):
        User = self.MainWindow.AdministratorManageUser.tableWidget.selectionModel().selectedRows()[0]
        Username = self.MainWindow.AdministratorManageUser.tableWidget.item(User.row(), 0).text()
        DataBaseManager.ApproveUserStatus(Username)
        self.filterUser()

    def declineUsers(self):
        User = self.MainWindow.AdministratorManageUser.tableWidget.selectionModel().selectedRows()[0]
        Username = self.MainWindow.AdministratorManageUser.tableWidget.item(User.row(), 0).text()
        Status = self.MainWindow.AdministratorManageUser.tableWidget.item(User.row(), 2).text()
        if Status == 'Approved':
            return QtWidgets.QMessageBox.warning(self.MainWindow, "User already approved",
                                                 "You cannot decline an approved user", QtWidgets.QMessageBox.Ok)
        DataBaseManager.DeclineUserStatus(Username)
        self.filterUser()

    def filterUsers(self):
        self.MainWindow.AdministratorManageUser.tableWidget.setRowCount(0)
        Username = self.MainWindow.AdministratorManageUser.lineEdit.text()
        Type = self.MainWindow.AdministratorManageUser.comboBox.currentText()
        Status = self.MainWindow.AdministratorManageUser.comboBox_2.currentText()
        if Type == 'All':
            Type = None
        if Status == 'All':
            Status = None
        if len(Username) == 0:
            Username = None
        tableData = DataBaseManager.GetAllAdministratorManageUserInformationFilterByStatus_EmpType_Username(
            Username, Type, Status)
        print(tableData)
        self.MainWindow.AdministratorManageUser.tableWidget.setSortingEnabled(False)
        for i in range(len(tableData)):
            self.MainWindow.AdministratorManageUser.tableWidget.insertRow(i)
            for column, key in enumerate(tableData[i].keys()):
                newItem = QtWidgets.QTableWidgetItem()
                newItem.setText(str(tableData[i][key]))
                self.MainWindow.AdministratorManageUser.tableWidget.setItem(i, column, newItem)
        self.MainWindow.AdministratorManageUser.tableWidget.setSortingEnabled(True)

    def showAdministratorManageSite(self):
        self.MainWindow.close()
        self.MainWindow = MainWindow()
        self.MainWindow.startAdministratorManageSite()
        if self.user == 'User':
            self.MainWindow.AdministratorManageSite.pushButton_5.clicked.connect(self.showUserFunctionality)
        elif self.user == "Staff":
            self.MainWindow.AdministratorManageSite.pushButton_5.clicked.connect(self.showStaffFunctionality)
        elif self.user == 'Manager':
            self.MainWindow.AdministratorManageSite.pushButton_5.clicked.connect(self.showManagerFunctionality)
        elif self.user == 'Administrator':
            self.MainWindow.AdministratorManageSite.pushButton_5.clicked.connect(self.showAdministratorFunctionality)
        elif self.user == 'StaffVisitor':
            self.MainWindow.AdministratorManageSite.pushButton_5.clicked.connect(self.showStaffVisitorFunctionality)
        elif self.user == 'ManagerVisitor':
            self.MainWindow.AdministratorManageSite.pushButton_5.clicked.connect(self.showManagerVisitorFunctionality)
        elif self.user == 'AdministratorVisitor':
            self.MainWindow.AdministratorManageSite.pushButton_5.clicked.connect(self.showAdminVisitorFunctionality)
        elif self.user == 'Visitor':
            self.MainWindow.AdministratorManageSite.pushButton_5.clicked.connect(self.showVisitorFunctionality)
        self.MainWindow.AdministratorManageSite.pushButton.clicked.connect(self.filterSites)
        allSites = ['All']
        allSitesDB = DataBaseManager.GetAllSites()
        for site in allSitesDB:
            allSites.append(site['sitename'])
        self.MainWindow.AdministratorManageSite.comboBox.addItems(allSites)
        allManagers = ['All']
        allManagersDB = DataBaseManager.GetManagerDropdownMenuForAdminManageSite()
        for manager in allManagersDB:
            allManagers.append(manager[list(manager.keys())[0]])
        self.MainWindow.AdministratorManageSite.comboBox_2.addItems(allManagers)
        self.MainWindow.AdministratorManageSite.comboBox_3.addItems(["Yes", "No"])
        self.MainWindow.AdministratorManageSite.pushButton_2.clicked.connect(self.showAdministratorCreateSite)
        self.MainWindow.AdministratorManageSite.pushButton_3.clicked.connect(self.showAdministratorEditSite)
        self.MainWindow.AdministratorManageSite.pushButton_4.clicked.connect(self.deleteSite)
        self.MainWindow.AdministratorManageSite.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.MainWindow.AdministratorManageSite.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)

    def filterSites(self):
        Site = self.MainWindow.AdministratorManageSite.comboBox.currentText()
        Manager = self.MainWindow.AdministratorManageSite.comboBox_2.currentText()
        OpenEveryday = self.MainWindow.AdministratorManageSite.comboBox_3.currentText()
        if Site == 'All':
            Site = None
        if Manager == 'All':
            Manager = None
        if OpenEveryday == 'Yes':
            OpenEveryday = True
        else:
            OpenEveryday = False
        self.MainWindow.AdministratorManageSite.tableWidget.setRowCount(0)
        tableData = DataBaseManager.GetAllSiteInformationForManageSiteFilterBySite_Manager_OpenEveryday(Site, Manager, OpenEveryday)
        self.MainWindow.AdministratorManageSite.tableWidget.setSortingEnabled(False)
        for i in range(len(tableData)):
            self.MainWindow.AdministratorManageSite.tableWidget.insertRow(i)
            for column, key in enumerate(tableData[i].keys()):
                newItem = QtWidgets.QTableWidgetItem()
                if key == 'openeverydays':
                    tableData[i][key] = 'Yes' if tableData[i][key] == 1 else 'No'
                newItem.setText(str(tableData[i][key]))
                self.MainWindow.AdministratorManageSite.tableWidget.setItem(i, column, newItem)
        self.MainWindow.AdministratorManageSite.tableWidget.setSortingEnabled(True)


    def deleteSite(self):
        Site = self.MainWindow.AdministratorManageSite.tableWidget.selectionModel().selectedRows()
        if len(Site) == 0:
            return QtWidgets.QMessageBox.warning(self.MainWindow, "Haven't selected a site",
                                                 "Please select a site first", QtWidgets.QMessageBox.Ok)
        Site = self.MainWindow.AdministratorManageSite.tableWidget.selectionModel().selectedRows()[0]
        Sitename = self.MainWindow.AdministratorManageSite.tableWidget.item(Site.row(), 0).text()
        DataBaseManager.AdminDeletesSite(Sitename)
        self.filterSites()

    def showAdministratorEditSite(self):
        Site = self.MainWindow.AdministratorManageSite.tableWidget.selectionModel().selectedRows()
        if len(Site) == 0:
            return QtWidgets.QMessageBox.warning(self.MainWindow, "Haven't selected a site",
                                                 "Please select a site first", QtWidgets.QMessageBox.Ok)
        Site = self.MainWindow.AdministratorManageSite.tableWidget.selectionModel().selectedRows()[0]
        Sitename = self.MainWindow.AdministratorManageSite.tableWidget.item(Site.row(), 0).text()
        self.MainWindow.close()
        self.MainWindow = MainWindow()
        self.MainWindow.startAdministratorEditSite()
        self.MainWindow.AdministratorEditSite.pushButton.clicked.connect(self.showAdministratorManageSite)
        allManagers = DataBaseManager.GetCurrentSiteManagerAndAllUnAssignedManagers(Sitename)
        managerNames = []
        for manager in allManagers:
            managerNames.append(manager['fname'] + ' ' + manager['lname'])
        self.MainWindow.AdministratorEditSite.comboBox.addItems(managerNames)
        self.MainWindow.AdministratorEditSite.pushButton_2.clicked.connect(lambda: self.editSite(Sitename, manager['fname'], manager['lname']))
        tableData = DataBaseManager.GetSiteInformationForEditSite(Sitename)
        self.MainWindow.AdministratorEditSite.lineEdit.setText(Sitename)
        self.MainWindow.AdministratorEditSite.lineEdit_2.setText(str(tableData['zipcode']))
        self.MainWindow.AdministratorEditSite.lineEdit_3.setText(tableData['address'])
        self.MainWindow.AdministratorEditSite.checkBox.setChecked(bool(tableData['openeveryday']))
        # if self.user == 'User':
        #     self.MainWindow.AdministratorEditSite.pushButton.clicked.connect(self.showUserFunctionality)
        # elif self.user == "Staff":
        #     self.MainWindow.AdministratorEditSite.pushButton.clicked.connect(self.showStaffFunctionality)
        # elif self.user == 'Manager':
        #     self.MainWindow.AdministratorEditSite.pushButton.clicked.connect(self.showManagerFunctionality)
        # elif self.user == 'Administrator':
        #     self.MainWindow.AdministratorEditSite.pushButton.clicked.connect(self.showAdministratorFunctionality)
        # elif self.user == 'StaffVisitor':
        #     self.MainWindow.AdministratorEditSite.pushButton.clicked.connect(self.showStaffVisitorFunctionality)
        # elif self.user == 'ManagerVisitor':
        #     self.MainWindow.AdministratorEditSite.pushButton.clicked.connect(self.showManagerVisitorFunctionality)
        # elif self.user == 'AdministratorVisitor':
        #     self.MainWindow.AdministratorEditSite.pushButton.clicked.connect(self.showAdminVisitorFunctionality)
        # elif self.user == 'Visitor':
        #     self.MainWindow.AdministratorEditSite.pushButton.clicked.connect(self.showVisitorFunctionality)

    def editSite(self, oldName, fname, lname):
        Name = self.MainWindow.AdministratorEditSite.lineEdit.text()
        Zipcode = self.MainWindow.AdministratorEditSite.lineEdit_2.text()
        Address = self.MainWindow.AdministratorEditSite.lineEdit_3.text()
        Manager = self.MainWindow.AdministratorEditSite.comboBox.currentText()
        OpenEveryday = self.MainWindow.AdministratorEditSite.checkBox.isChecked()
        Manager_id = DataBaseManager.GetSiteManagerIdFromFname_Lname(fname, lname)
        DataBaseManager.UpdateSiteInformation(oldName, int(Zipcode), Address, OpenEveryday, Manager_id, Name)

    def showAdministratorCreateSite(self):
        self.MainWindow.close()
        self.MainWindow = MainWindow()
        self.MainWindow.startAdministratorCreateSite()
        self.MainWindow.AdministratorCreateSite.pushButton.clicked.connect(self.showAdministratorManageSite)
        self.MainWindow.AdministratorCreateSite.pushButton_2.clicked.connect(self.createSite)
        allManagers = DataBaseManager.GetManagersNotAssignedSite()
        allFnameLname = []
        for manager in allManagers:
            allFnameLname.append(manager['fname'] + ' ' + manager['lname'])
        self.MainWindow.AdministratorCreateSite.comboBox.addItems(allFnameLname)
        # if self.user == 'User':
        #     self.MainWindow.AdministratorCreateSite.pushButton.clicked.connect(self.showUserFunctionality)
        # elif self.user == "Staff":
        #     self.MainWindow.AdministratorCreateSite.pushButton.clicked.connect(self.showStaffFunctionality)
        # elif self.user == 'Manager':
        #     self.MainWindow.AdministratorCreateSite.pushButton.clicked.connect(self.showManagerFunctionality)
        # elif self.user == 'Administrator':
        #     self.MainWindow.AdministratorCreateSite.pushButton.clicked.connect(self.showAdministratorFunctionality)
        # elif self.user == 'StaffVisitor':
        #     self.MainWindow.AdministratorCreateSite.pushButton.clicked.connect(self.showStaffVisitorFunctionality)
        # elif self.user == 'ManagerVisitor':
        #     self.MainWindow.AdministratorCreateSite.pushButton.clicked.connect(self.showManagerVisitorFunctionality)
        # elif self.user == 'AdministratorVisitor':
        #     self.MainWindow.AdministratorCreateSite.pushButton.clicked.connect(self.showAdminVisitorFunctionality)
        # elif self.user == 'Visitor':
        #     self.MainWindow.AdministratorCreateSite.pushButton.clicked.connect(self.showVisitorFunctionality)

    def createSite(self):
        Name = self.MainWindow.AdministratorCreateSite.lineEdit.text()
        Zipcode = self.MainWindow.AdministratorCreateSite.lineEdit_2.text()
        Address = self.MainWindow.AdministratorCreateSite.lineEdit_3.text()
        if len(Address) == 0:
            Address = None
        if not Zipcode.isdigit():
            return QtWidgets.QMessageBox.warning(self.MainWindow, "Zipcode not valid", "Please confirm your zipcode",
                                                 QtWidgets.QMessageBox.Ok)
        Manager = self.MainWindow.AdministratorCreateSite.comboBox.currentText()
        openEveryday = self.MainWindow.AdministratorCreateSite.checkBox.isChecked()
        if not DataBaseManager.IsSitenameUnique(Name):
            return QtWidgets.QMessageBox.warning(self.MainWindow, "Sitename not valid", "Sitename is not unique",
                                                 QtWidgets.QMessageBox.Ok)
        Manager = DataBaseManager.GetEmployeeIdByFullName(Manager)['employee_id']
        DataBaseManager.AddNewSites(Name, int(Zipcode), Address, openEveryday, Manager)

    def showAdministratorManageTransit(self):
        self.MainWindow.close()
        self.MainWindow = MainWindow()
        self.MainWindow.startAdministratorManageTransit()
        if self.user == 'User':
            self.MainWindow.AdministratorManageTransit.pushButton_5.clicked.connect(self.showUserFunctionality)
        elif self.user == "Staff":
            self.MainWindow.AdministratorManageTransit.pushButton_5.clicked.connect(self.showStaffFunctionality)
        elif self.user == 'Manager':
            self.MainWindow.AdministratorManageTransit.pushButton_5.clicked.connect(self.showManagerFunctionality)
        elif self.user == 'Administrator':
            self.MainWindow.AdministratorManageTransit.pushButton_5.clicked.connect(self.showAdministratorFunctionality)
        elif self.user == 'StaffVisitor':
            self.MainWindow.AdministratorManageTransit.pushButton_5.clicked.connect(self.showStaffVisitorFunctionality)
        elif self.user == 'ManagerVisitor':
            self.MainWindow.AdministratorManageTransit.pushButton_5.clicked.connect(self.showManagerVisitorFunctionality)
        elif self.user == 'AdministratorVisitor':
            self.MainWindow.AdministratorManageTransit.pushButton_5.clicked.connect(self.showAdminVisitorFunctionality)
        elif self.user == 'Visitor':
            self.MainWindow.AdministratorManageTransit.pushButton_5.clicked.connect(self.showVisitorFunctionality)
        self.MainWindow.AdministratorManageTransit.comboBox.addItems(["All", "MARTA", "Bus", "Bike"])
        allSites = ['All']
        allSitesDB = DataBaseManager.GetAllSites()
        for site in allSitesDB:
            allSites.append(site['sitename'])
        self.MainWindow.AdministratorManageTransit.comboBox_2.addItems(allSites)
        self.MainWindow.AdministratorManageTransit.pushButton.clicked.connect(self.filterAdminTransit)
        self.MainWindow.AdministratorManageTransit.pushButton_2.clicked.connect(self.showAdministratorCreateTransit)
        self.MainWindow.AdministratorManageTransit.pushButton_3.clicked.connect(self.showAdministratorEditTransit)
        self.MainWindow.AdministratorManageTransit.pushButton_4.clicked.connect(self.deleteTransit)
        self.MainWindow.AdministratorManageTransit.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.MainWindow.AdministratorManageTransit.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)

    def deleteTransit(self):
        Route = self.MainWindow.AdministratorManageTransit.tableWidget.selectionModel().selectedRows()[0]
        TakeType = self.MainWindow.AdministratorManageTransit.tableWidget.item(Route.row(), 1).text()
        TakeRoute = self.MainWindow.AdministratorManageTransit.tableWidget.item(Route.row(), 0).text()
        Price = self.MainWindow.AdministratorManageTransit.tableWidget.item(Route.row(), 2).text()
        DataBaseManager.DeleteTransit(TakeType, TakeRoute)
        self.filterAdminTransit()

    def filterAdminTransit(self):
        self.MainWindow.AdministratorManageTransit.tableWidget.setRowCount(0)
        TransportType = self.MainWindow.AdministratorManageTransit.comboBox.currentText()
        if TransportType == 'All':
            TransportType = None
        Route = self.MainWindow.AdministratorManageTransit.lineEdit.text()
        if len(Route) == 0:
            Route = None
        LowRange = self.MainWindow.AdministratorManageTransit.lineEdit_2.text()
        HighRange = self.MainWindow.AdministratorManageTransit.lineEdit_3.text()
        if (len(LowRange) != 0 and len(HighRange) == 0) or (len(LowRange) != 0 and len(HighRange) == 0):
            return QtWidgets.QMessageBox.warning(self.MainWindow, "Range not valid", "Please enter both ranges",
                                                 QtWidgets.QMessageBox.Ok)
        if ((len(LowRange) != 0) and not isFloat(LowRange)) or ((len(HighRange) != 0) and not isFloat(HighRange)):
            return QtWidgets.QMessageBox.warning(self.MainWindow, "Range not valid", "You could only enter digits",
                                                 QtWidgets.QMessageBox.Ok)
        tableData = None
        if len(LowRange) == 0 and len(HighRange) == 0:
            LowRange = None
            HighRange = None
            tableData = DataBaseManager.GetTransitByFilterByTransportType_Route_ContainSite_PriceRange(TransportType, Route, LowRange, HighRange)
        else:
            tableData = DataBaseManager.GetTransitByFilterByTransportType_Route_ContainSite_PriceRange(TransportType, Route, float(LowRange),
                                                                   float(HighRange))
        self.MainWindow.AdministratorManageTransit.tableWidget.setSortingEnabled(False)
        for i in range(len(tableData)):
            self.MainWindow.AdministratorManageTransit.tableWidget.insertRow(i)
            for column, key in enumerate(tableData[i].keys()):
                newItem = QtWidgets.QTableWidgetItem()
                newItem.setText(str(tableData[i][key]))
                self.MainWindow.AdministratorManageTransit.tableWidget.setItem(i, column, newItem)
        self.MainWindow.AdministratorManageTransit.tableWidget.setSortingEnabled(True)

    def showAdministratorEditTransit(self):
        Route = self.MainWindow.AdministratorManageTransit.tableWidget.selectionModel().selectedRows()[0]
        TakeType = self.MainWindow.AdministratorManageTransit.tableWidget.item(Route.row(), 1).text()
        TakeRoute = self.MainWindow.AdministratorManageTransit.tableWidget.item(Route.row(), 0).text()
        Price = self.MainWindow.AdministratorManageTransit.tableWidget.item(Route.row(), 2).text()
        self.MainWindow.close()
        self.MainWindow = MainWindow()
        self.MainWindow.startAdministratorEditTransit()
        self.MainWindow.AdministratorEditTransit.pushButton.clicked.connect(self.showAdministratorManageTransit)
        self.MainWindow.AdministratorEditTransit.pushButton_2.clicked.connect(lambda: self.updateTransit(TakeRoute))
        self.MainWindow.AdministratorEditTransit.label_2.setText(TakeType)
        self.MainWindow.AdministratorEditTransit.lineEdit.setText(TakeRoute)
        self.MainWindow.AdministratorEditTransit.lineEdit_2.setText(Price)
        ConnectedSites = DataBaseManager.GetTransitConnectedSites(TakeType, TakeRoute)
        ConnectedSitenames = [each['connect_name'] for each in ConnectedSites]
        allSites = DataBaseManager.GetAllSites()
        allSitenames = []
        for site in allSites:
            allSitenames.append(site['sitename'])
        self.MainWindow.AdministratorEditTransit.listWidget.addItems(allSitenames)
        self.MainWindow.AdministratorEditTransit.listWidget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.MainWindow.AdministratorEditTransit.listWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        for i in range(self.MainWindow.AdministratorEditTransit.listWidget.count()):
            if self.MainWindow.AdministratorEditTransit.listWidget.item(i).text() in ConnectedSitenames:
                self.MainWindow.AdministratorEditTransit.listWidget.item(i).setSelected(True)
        # if self.user == 'User':
        #     self.MainWindow.AdministratorEditTransit.pushButton.clicked.connect(self.showUserFunctionality)
        # elif self.user == "Staff":
        #     self.MainWindow.AdministratorEditTransit.pushButton.clicked.connect(self.showStaffFunctionality)
        # elif self.user == 'Manager':
        #     self.MainWindow.AdministratorEditTransit.pushButton.clicked.connect(self.showManagerFunctionality)
        # elif self.user == 'Administrator':
        #     self.MainWindow.AdministratorEditTransit.pushButton.clicked.connect(self.showAdministratorFunctionality)
        # elif self.user == 'StaffVisitor':
        #     self.MainWindow.AdministratorEditTransit.pushButton.clicked.connect(self.showStaffVisitorFunctionality)
        # elif self.user == 'ManagerVisitor':
        #     self.MainWindow.AdministratorEditTransit.pushButton.clicked.connect(self.showManagerVisitorFunctionality)
        # elif self.user == 'AdministratorVisitor':
        #     self.MainWindow.AdministratorEditTransit.pushButton.clicked.connect(self.showAdminVisitorFunctionality)
        # elif self.user == 'Visitor':
        #     self.MainWindow.AdministratorEditTransit.pushButton.clicked.connect(self.showVisitorFunctionality)

    def updateTransit(self, oldRoute):
        Route = self.MainWindow.AdministratorEditTransit.lineEdit.text()
        Price = self.MainWindow.AdministratorEditTransit.lineEdit_2.text()
        TransitType = self.MainWindow.AdministratorEditTransit.label_2.text()
        if not isFloat(Price):
            return QtWidgets.QMessageBox.warning(self.MainWindow, "Price not valid", "Price must be a float",
                                                 QtWidgets.QMessageBox.Ok)
        DataBaseManager.UpdateTransitPriceAndRoute(float(Price), TransitType, oldRoute, Route)


    def showAdministratorCreateTransit(self):

        self.MainWindow.close()
        self.MainWindow = MainWindow()
        self.MainWindow.startAdministratorCreateTransit()
        self.MainWindow.AdministratorCreateTransit.pushButton_5.clicked.connect(self.showAdministratorManageTransit)
        self.MainWindow.AdministratorCreateTransit.pushButton_6.clicked.connect(self.createTransit)
        allSites = DataBaseManager.GetAllSites()
        allSitenames = []
        for site in allSites:
            allSitenames.append(site['sitename'])
        self.MainWindow.AdministratorCreateTransit.listWidget.addItems(allSitenames)
        self.MainWindow.AdministratorCreateTransit.listWidget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.MainWindow.AdministratorCreateTransit.comboBox.addItems(["MARTA", "Bus", "Bike"])
        # if self.user == 'User':
        #     self.MainWindow.AdministratorCreateTransit.pushButton_5.clicked.connect(self.showUserFunctionality)
        # elif self.user == "Staff":
        #     self.MainWindow.AdministratorCreateTransit.pushButton_5.clicked.connect(self.showStaffFunctionality)
        # elif self.user == 'Manager':
        #     self.MainWindow.AdministratorCreateTransit.pushButton_5.clicked.connect(self.showManagerFunctionality)
        # elif self.user == 'Administrator':
        #     self.MainWindow.AdministratorCreateTransit.pushButton_5.clicked.connect(self.showAdministratorFunctionality)
        # elif self.user == 'StaffVisitor':
        #     self.MainWindow.AdministratorCreateTransit.pushButton_5.clicked.connect(self.showStaffVisitorFunctionality)
        # elif self.user == 'ManagerVisitor':
        #     self.MainWindow.AdministratorCreateTransit.pushButton_5.clicked.connect(self.showManagerVisitorFunctionality)
        # elif self.user == 'AdministratorVisitor':
        #     self.MainWindow.AdministratorCreateTransit.pushButton_5.clicked.connect(self.showAdminVisitorFunctionality)
        # elif self.user == 'Visitor':
        #     self.MainWindow.AdministratorCreateTransit.pushButton_5.clicked.connect(self.showVisitorFunctionality)

    def createTransit(self):
        TransportType = self.MainWindow.AdministratorCreateTransit.comboBox.currentText()
        Route = self.MainWindow.AdministratorCreateTransit.lineEdit.text()
        Price = self.MainWindow.AdministratorCreateTransit.lineEdit_2.text()
        Sites = self.MainWindow.AdministratorCreateTransit.listWidget.selectedItems()
        if not isFloat(Price):
            return QtWidgets.QMessageBox.warning(self.MainWindow, "price not valid", "Please enter a valid price",
                                                 QtWidgets.QMessageBox.Ok)
            if float(Price) < 0:
                return QtWidgets.QMessageBox.warning(self.MainWindow, "price not valid", "Please enter a valid price",
                                                     QtWidgets.QMessageBox.Ok)
        if len(Route) == 0:
            return QtWidgets.QMessageBox.warning(self.MainWindow, "Route not valid", "Please enter a valid route",
                                                 QtWidgets.QMessageBox.Ok)
        if len(Sites) == 0:
            return QtWidgets.QMessageBox.warning(self.MainWindow, "Sites not valid", "Please select at least one site",
                                                 QtWidgets.QMessageBox.Ok)
        DataBaseManager.AddTransit(TransportType, Route, float(Price))

    def showManagerManageEvent(self):
        self.MainWindow.close()
        self.MainWindow = MainWindow()
        self.MainWindow.startManagerManageEvent()
        if self.user == 'User':
            self.MainWindow.ManagerManageEvent.pushButton_5.clicked.connect(self.showUserFunctionality)
        elif self.user == "Staff":
            self.MainWindow.ManagerManageEvent.pushButton_5.clicked.connect(self.showStaffFunctionality)
        elif self.user == 'Manager':
            self.MainWindow.ManagerManageEvent.pushButton_5.clicked.connect(self.showManagerFunctionality)
        elif self.user == 'Administrator':
            self.MainWindow.ManagerManageEvent.pushButton_5.clicked.connect(self.showAdministratorFunctionality)
        elif self.user == 'StaffVisitor':
            self.MainWindow.ManagerManageEvent.pushButton_5.clicked.connect(self.showStaffVisitorFunctionality)
        elif self.user == 'ManagerVisitor':
            self.MainWindow.ManagerManageEvent.pushButton_5.clicked.connect(self.showManagerVisitorFunctionality)
        elif self.user == 'AdministratorVisitor':
            self.MainWindow.ManagerManageEvent.pushButton_5.clicked.connect(self.showAdminVisitorFunctionality)
        elif self.user == 'Visitor':
            self.MainWindow.ManagerManageEvent.pushButton_5.clicked.connect(self.showVisitorFunctionality)
        self.MainWindow.ManagerManageEvent.pushButton.clicked.connect(self.filterManageEvents)
        self.MainWindow.ManagerManageEvent.pushButton_2.clicked.connect(self.showManagerCreateEvent)
        self.MainWindow.ManagerManageEvent.pushButton_3.clicked.connect(self.showManagerViewEditEvent)
        self.MainWindow.ManagerManageEvent.pushButton_4.clicked.connect(self.deleteEvent)
        self.MainWindow.ManagerManageEvent.dateEdit.setDate(QtCore.QDate.currentDate())
        self.MainWindow.ManagerManageEvent.dateEdit_2.setDate(QtCore.QDate.currentDate())
        self.MainWindow.ManagerManageEvent.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.MainWindow.ManagerManageEvent.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)

    def filterManageEvents(self):
        self.MainWindow.ManagerManageEvent.tableWidget.setRowCount(0)
        Name = self.MainWindow.ManagerManageEvent.lineEdit.text()
        DescriptionKeyword = self.MainWindow.ManagerManageEvent.lineEdit_2.text()
        LowDurationRange = self.MainWindow.ManagerManageEvent.lineEdit_3.text()
        HighDurationRange = self.MainWindow.ManagerManageEvent.lineEdit_4.text()
        LowTotalVisitRange = self.MainWindow.ManagerManageEvent.lineEdit_5.text()
        HighTotalVisitRange = self.MainWindow.ManagerManageEvent.lineEdit_6.text()
        LowTotalRevenueRange = self.MainWindow.ManagerManageEvent.lineEdit_7.text()
        HighTotalRevenueRange = self.MainWindow.ManagerManageEvent.lineEdit_8.text()
        StartDate = self.MainWindow.ManagerManageEvent.dateEdit.date().toPyDate()
        EndDate = self.MainWindow.ManagerManageEvent.dateEdit_2.date().toPyDate()
        Name = setNone(Name)
        DescriptionKeyword = setNone(DescriptionKeyword)
        tableData = None
        if len(LowDurationRange) == 0 and len(HighDurationRange) == 0:
            LowDurationRange = None
            HighDurationRange = None
        elif len(LowDurationRange) * len(HighDurationRange) == 0:
            return QtWidgets.QMessageBox.warning(self.MainWindow, "Range not valid", "Please enter both ranges",
                                                 QtWidgets.QMessageBox.Ok)
        if len(LowTotalVisitRange) == 0 and len(HighTotalVisitRange) == 0:
            LowTotalVisitRange = None
            HighTotalVisitRange = None
        elif len(LowTotalVisitRange) * len(HighTotalRevenueRange) == 0:
            return QtWidgets.QMessageBox.warning(self.MainWindow, "Range not valid", "Please enter both ranges",
                                                 QtWidgets.QMessageBox.Ok)
        if len(LowTotalRevenueRange) == 0 and len(HighTotalRevenueRange) == 0:
            LowTotalRevenueRange = None
            HighTotalRevenueRange = None
        elif len(LowTotalRevenueRange) * len(HighTotalRevenueRange) == 0:
            return QtWidgets.QMessageBox.warning(self.MainWindow, "Range not valid", "Please enter both ranges",
                                                 QtWidgets.QMessageBox.Ok)
        tableData = DataBaseManager.GetAllEventFilteredByEventName_DescripKeyword_StartDate_EndDate_DurationRange_VisitRange_RevenueRange(Name, DescriptionKeyword, StartDate, EndDate, LowDurationRange, HighDurationRange, LowTotalVisitRange, HighTotalVisitRange, LowTotalRevenueRange, HighTotalRevenueRange)
        self.MainWindow.ManagerManageEvent.tableWidget.setSortingEnabled(False)
        for i in range(len(tableData)):
            self.MainWindow.ManagerManageEvent.tableWidget.insertRow(i)
            for column, key in enumerate(["event_name", 'staff_count','duration', 'total_visit']):
                newItem = QtWidgets.QTableWidgetItem()
                newItem.setText(str(tableData[i][key]))
                self.MainWindow.ManagerManageEvent.tableWidget.setItem(i, column, newItem)
            newItem = QtWidgets.QTableWidgetItem()
            newItem.setText(str(tableData[i]['revenue'] * tableData[i]['total_visit']))
            self.MainWindow.ManagerManageEvent.tableWidget.setItem(i, 4, newItem)
        self.MainWindow.ManagerManageEvent.tableWidget.setSortingEnabled(True)
        self.MainWindow.ManagerManageEvent.tableData = tableData

    def deleteEvent(self):
        Event =  self.MainWindow.ManagerManageEvent.tableWidget.selectionModel().selectedRows()[0]
        EventName = self.MainWindow.ManagerManageEvent.tableWidget.item(Event.row(), 0).text()
        SiteName = None
        startDate = None
        for data in self.MainWindow.ManagerManageEvent.tableData:
            if data['event_name'] == EventName:
                siteName = data['sitename']
                startDate = data['startdate']
        DataBaseManager.DeleteEvent(EventName, SiteName, startDate)
        self.filterManageEvents()

    def showManagerViewEditEvent(self):
        Event = self.MainWindow.ManagerManageEvent.tableWidget.selectionModel().selectedRows()[0]
        EventName = self.MainWindow.ManagerManageEvent.tableWidget.item(Event.row(), 0).text()
        SiteName = None
        startDate = None
        Price = None
        EndDate = None
        for data in self.MainWindow.ManagerManageEvent.tableData:
            if data['event_name'] == EventName:
                SiteName = data['sitename']
                startDate = data['startdate']
                Price = data['revenue']
                EndDate = data['endate']
        self.MainWindow.close()
        self.MainWindow = MainWindow()
        self.MainWindow.startManagerViewEditEvent()
        self.MainWindow.ManagerViewEditEvent.pushButton_3.clicked.connect(self.showManagerManageEvent)
        self.MainWindow.ManagerViewEditEvent.label_3.setText(EventName)
        self.MainWindow.ManagerViewEditEvent.label_4.setText(str(Price))
        self.MainWindow.ManagerViewEditEvent.label_7.setText(str(startDate))
        self.MainWindow.ManagerViewEditEvent.label_9.setText(str(EndDate))
        allStaff = DataBaseManager.StaffAssignedAndAvailibleStaffForEvent(EventName, SiteName, startDate, EndDate)
        allAssignedStaff = DataBaseManager.GetAssignedStaffsForEvent(EventName, SiteName, startDate)
        allStaffNames = []
        allAssignedStaffNames = [each['fname'] + ' ' + each['lname'] for each in allAssignedStaff]
        for staff in allStaff:
            allStaffNames.append(staff['fname'] + ' ' + staff['lname'])
        self.MainWindow.ManagerViewEditEvent.listWidget.addItems(allStaffNames)
        for i in range(self.MainWindow.ManagerViewEditEvent.listWidget.count()):
            if self.MainWindow.ManagerViewEditEvent.listWidget.item(i).text() in allAssignedStaffNames:
                self.MainWindow.ManagerViewEditEvent.listWidget.item(i).setSelected(True)
        tableData = DataBaseManager.GetEventViewEditEventByFilterByVisitRange_RevenueRange(EventName, Price, None, None, None, None)
        self.MainWindow.ManagerViewEditEvent.label_13.setText(str(tableData[0]['capacity']))
        self.MainWindow.ManagerViewEditEvent.label_11.setText(str(tableData[0]['minstaffReq']))
        # if self.user == 'User':
        #     self.MainWindow.ManagerViewEditEvent.pushButton_3.clicked.connect(self.showUserFunctionality)
        # elif self.user == "Staff":
        #     self.MainWindow.ManagerViewEditEvent.pushButton_3.clicked.connect(self.showStaffFunctionality)
        # elif self.user == 'Manager':
        #     self.MainWindow.ManagerViewEditEvent.pushButton_3.clicked.connect(self.showManagerFunctionality)
        # elif self.user == 'Administrator':
        #     self.MainWindow.ManagerViewEditEvent.pushButton_3.clicked.connect(self.showAdministratorFunctionality)
        # elif self.user == 'StaffVisitor':
        #     self.MainWindow.ManagerViewEditEvent.pushButton_3.clicked.connect(self.showStaffVisitorFunctionality)
        # elif self.user == 'ManagerVisitor':
        #     self.MainWindow.ManagerViewEditEvent.pushButton_3.clicked.connect(self.showManagerVisitorFunctionality)
        # elif self.user == 'AdministratorVisitor':
        #     self.MainWindow.ManagerViewEditEvent.pushButton_3.clicked.connect(self.showAdminVisitorFunctionality)
        # elif self.user == 'Visitor':
        #     self.MainWindow.ManagerViewEditEvent.pushButton_3.clicked.connect(self.showVisitorFunctionality)
        self.MainWindow.ManagerViewEditEvent.pushButton.clicked.connect(lambda: self.filterViewEditEvents(EventName))
        self.MainWindow.ManagerViewEditEvent.pushButton_2.clicked.connect(lambda: self.updateEvent(EventName, SiteName, startDate))
        Description = DataBaseManager.GetDescriptionForEvent(SiteName, EventName, startDate)
        self.MainWindow.ManagerViewEditEvent.textBrowser.setText(Description['event_description'])
        self.MainWindow.ManagerViewEditEvent.listWidget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)


    def filterViewEditEvents(self, EventName):
        self.MainWindow.ManagerViewEditEvent.tableWidget.setRowCount(0)
        staffAssigned = self.MainWindow.ManagerViewEditEvent.listWidget.selectedItems()
        LowDailyVisit = self.MainWindow.ManagerViewEditEvent.lineEdit.text()
        HighDailyVisit = self.MainWindow.ManagerViewEditEvent.lineEdit_2.text()
        LowDailyRevenue = self.MainWindow.ManagerViewEditEvent.lineEdit_3.text()
        HighDailyRevenue = self.MainWindow.ManagerViewEditEvent.lineEdit_4.text()
        Price = self.MainWindow.ManagerViewEditEvent.label_4.text()
        if len(LowDailyVisit) == 0 and len(HighDailyVisit) == 0:
            LowDailyVisit = None
            HighDailyVisit = None
        elif len(LowDailyVisit) * len(HighDailyVisit) == 0:
            return QtWidgets.QMessageBox.warning(self.MainWindow, "Range not valid", "Please enter both ranges",
                                                 QtWidgets.QMessageBox.Ok)
        if len(LowDailyRevenue) == 0 and len(HighDailyRevenue) == 0:
            LowDailyRevenue = None
            HighDailyRevenue = None
        elif len(LowDailyRevenue) * len(HighDailyRevenue) == 0:
            return QtWidgets.QMessageBox.warning(self.MainWindow, "Range not valid", "Please enter both ranges",
                                                 QtWidgets.QMessageBox.Ok)
        tableData = DataBaseManager.GetEventViewEditEventByFilterByVisitRange_RevenueRange(EventName, Price, LowDailyVisit, HighDailyVisit, LowDailyRevenue, HighDailyRevenue)
        self.MainWindow.ManagerViewEditEvent.tableWidget.setSortingEnabled(False)
        for i in range(len(tableData)):
            self.MainWindow.ManagerViewEditEvent.tableWidget.insertRow(i)
            for column, key in enumerate(tableData[i].keys()):
                newItem = QtWidgets.QTableWidgetItem()
                newItem.setText(str(tableData[i][key]))
                self.MainWindow.ManagerViewEditEvent.tableWidget.setItem(i, column, newItem)
                if column == 2:
                    break
        self.MainWindow.ManagerViewEditEvent.tableWidget.setSortingEnabled(True)

    def updateEvent(self, EventName, SiteName, startDate):
        minstaffReq = int(self.MainWindow.ManagerViewEditEvent.label_11.text())
        staffAssigned = self.MainWindow.ManagerViewEditEvent.listWidget.selectedItems()
        Description = self.MainWindow.ManagerViewEditEvent.textBrowser.toPlainText()
        LowDailyVisit = self.MainWindow.ManagerViewEditEvent.lineEdit.text()
        HighDailyVisit = self.MainWindow.ManagerViewEditEvent.lineEdit_2.text()
        LowDailyRevenue = self.MainWindow.ManagerViewEditEvent.lineEdit_3.text()
        HighDailyRevenue = self.MainWindow.ManagerViewEditEvent.lineEdit_4.text()
        selectedStaff = self.MainWindow.ManagerViewEditEvent.listWidget.selectedItems()
        if len(staffAssigned) < minstaffReq:
            return QtWidgets.QMessageBox.warning(self.MainWindow, "Staff not valid",
                                                 "Chosen staffs fewer than minimum requirement",
                                                 QtWidgets.QMessageBox.Ok)
        DataBaseManager.DeleteAllAssignedStaffsForEvent(EventName, SiteName, startDate)
        for staff in staffAssigned:
            DataBaseManager.AddAssignedStaffForEvent(DataBaseManager.GetEmployeeIdByFullName(staff.text())['employee_id'], SiteName, EventName, startDate)
        DataBaseManager.UpdateDescriptionForEvent(Description, SiteName, EventName, startDate)

    def showManagerCreateEvent(self):
        self.MainWindow.close()
        self.MainWindow = MainWindow()
        self.MainWindow.startManagerCreateEvent()
        self.MainWindow.ManagerCreateEvent.pushButton.clicked.connect(self.showManagerManageEvent)
        self.MainWindow.ManagerCreateEvent.pushButton.clicked.connect(self.createEvent)
        self.MainWindow.ManagerCreateEvent.dateEdit.setDate(QtCore.QDate.currentDate())
        self.MainWindow.ManagerCreateEvent.dateEdit_2.setDate(QtCore.QDate.currentDate())
        self.MainWindow.ManagerCreateEvent.availableStaffs = []
        self.MainWindow.ManagerCreateEvent.listWidget.addItems(self.MainWindow.ManagerCreateEvent.availableStaffs)
        self.MainWindow.ManagerCreateEvent.dateEdit.dateChanged.connect(self.getAvailableStaffs)
        self.MainWindow.ManagerCreateEvent.dateEdit_2.dateChanged.connect(self.getAvailableStaffs)
        # if self.user == 'User':
        #     self.MainWindow.ManagerCreateEvent.pushButton.clicked.connect(self.showUserFunctionality)
        # elif self.user == "Staff":
        #     self.MainWindow.ManagerCreateEvent.pushButton.clicked.connect(self.showStaffFunctionality)
        # elif self.user == 'Manager':
        #     self.MainWindow.ManagerCreateEvent.pushButton.clicked.connect(self.showManagerFunctionality)
        # elif self.user == 'Administrator':
        #     self.MainWindow.ManagerCreateEvent.pushButton.clicked.connect(self.showAdministratorFunctionality)
        # elif self.user == 'StaffVisitor':
        #     self.MainWindow.ManagerCreateEvent.pushButton.clicked.connect(self.showStaffVisitorFunctionality)
        # elif self.user == 'ManagerVisitor':
        #     self.MainWindow.ManagerCreateEvent.pushButton.clicked.connect(self.showManagerVisitorFunctionality)
        # elif self.user == 'AdministratorVisitor':
        #     self.MainWindow.ManagerCreateEvent.pushButton.clicked.connect(self.showAdminVisitorFunctionality)
        # elif self.user == 'Visitor':
        #     self.MainWindow.ManagerCreateEvent.pushButton.clicked.connect(self.showVisitorFunctionality)

    def getAvailableStaffs(self):
        startDate = self.MainWindow.ManagerCreateEvent.dateEdit.date().toPyDate()
        endDate = self.MainWindow.ManagerCreateEvent.dateEdit_2.date().toPyDate()
        allAvailableStaffs = DataBaseManager.GetAllAvailibleStaffForNewEvent(startDate, endDate)
        self.MainWindow.ManagerCreateEvent.availableStaffs = []
        self.MainWindow.ManagerCreateEvent.listWidget.clear()
        for staff in allAvailableStaffs:
            self.MainWindow.ManagerCreateEvent.availableStaffs.append(staff['fname'] + ' ' + staff['lname'])
        self.MainWindow.ManagerCreateEvent.listWidget.addItems(self.MainWindow.ManagerCreateEvent.availableStaffs)

    def createEvent(self):
        startDate = self.MainWindow.ManagerCreateEvent.dateEdit.date().toPyDate()
        endDate = self.MainWindow.ManagerCreateEvent.dateEdit_2.date().toPyDate()
        Name = self.MainWindow.ManagerCreateEvent.lineEdit.text()
        Price = self.MainWindow.ManagerCreateEvent.lineEdit_2.text()
        Capacity = self.MainWindow.ManagerCreateEvent.lineEdit_3.text()
        MinStaffRequired = self.MainWindow.ManagerCreateEvent.lineEdit_4.text()
        Description = self.MainWindow.ManagerCreateEvent.textEdit.toPlainText()
        SelectedStaff = self.MainWindow.ManagerCreateEvent.listWidget.selectedItems()[0]
        if not isFloat(Price) or float(Price) <  0:
            return QtWidgets.QMessageBox.warning(self.MainWindow, "Price not valid", "Please enter a non-negative float",
                                                 QtWidgets.QMessageBox.Ok)
        if not Capacity.isdigit() or int(Capacity) <= 0:
            return QtWidgets.QMessageBox.warning(self.MainWindow, "Capacity not valid",
                                                 "Please enter a positive Integer",
                                                 QtWidgets.QMessageBox.Ok)
        if not MinStaffRequired.isdigit() or int(MinStaffRequired) <= 0:
            return QtWidgets.QMessageBox.warning(self.MainWindow, "Min staff required not valid",
                                                 "Please enter a positive Integer",
                                                 QtWidgets.QMessageBox.Ok)
        if startDate > endDate:
            return QtWidgets.QMessageBox.warning(self.MainWindow, "Date not valid",
                                                 "Start Date must be before End Date",
                                                 QtWidgets.QMessageBox.Ok)
        sitename = DataBaseManager.GetSitenameWithManagerUsername(self.username)['sitename']
        checkForOverlap = DataBaseManager.GetEventWithSameNameAndDateAtSameSiteToCheckIfIsOverlapEvent(Name, sitename)
        employeeID = DataBaseManager.GetEmployeeIdWithUsername(SelectedStaff.split()[0])['employee_id']
        if not checkForOverlap:
            DataBaseManager.ManagerCreateEvent(sitename, Name, startDate, int(MinStaffRequired), Description, float(Price), endDate, employeeID)
        else:
            return QtWidgets.QMessageBox.warning(self.MainWindow, "Overlap happens",
                                                 "Please change date",
                                                 QtWidgets.QMessageBox.Ok)

    def showManagerManageStaff(self):
        self.MainWindow.close()
        self.MainWindow = MainWindow()
        self.MainWindow.startManagerManageStaff()
        if self.user == 'User':
            self.MainWindow.ManagerManageStaff.pushButton_2.clicked.connect(self.showUserFunctionality)
        elif self.user == "Staff":
            self.MainWindow.ManagerManageStaff.pushButton_2.clicked.connect(self.showStaffFunctionality)
        elif self.user == 'Manager':
            self.MainWindow.ManagerManageStaff.pushButton_2.clicked.connect(self.showManagerFunctionality)
        elif self.user == 'Administrator':
            self.MainWindow.ManagerManageStaff.pushButton_2.clicked.connect(self.showAdministratorFunctionality)
        elif self.user == 'StaffVisitor':
            self.MainWindow.ManagerManageStaff.pushButton_2.clicked.connect(self.showStaffVisitorFunctionality)
        elif self.user == 'ManagerVisitor':
            self.MainWindow.ManagerManageStaff.pushButton_2.clicked.connect(self.showManagerVisitorFunctionality)
        elif self.user == 'AdministratorVisitor':
            self.MainWindow.ManagerManageStaff.pushButton_2.clicked.connect(self.showAdminVisitorFunctionality)
        elif self.user == 'Visitor':
            self.MainWindow.ManagerManageStaff.pushButton_2.clicked.connect(self.showVisitorFunctionality)
        allSites = ['All']
        allSitesDB = DataBaseManager.GetAllSites()
        for site in allSitesDB:
            allSites.append(site['sitename'])
        self.MainWindow.ManagerManageStaff.comboBox.addItems(allSites)
        self.MainWindow.ManagerManageStaff.pushButton.clicked.connect(self.filterStaff)
        self.MainWindow.ManagerManageStaff.dateEdit.setDate(QtCore.QDate.currentDate())
        self.MainWindow.ManagerManageStaff.dateEdit_2.setDate(QtCore.QDate.currentDate())

    def filterStaff(self):
        Site = self.MainWindow.ManagerManageStaff.comboBox.currentText()
        Fname = self.MainWindow.ManagerManageStaff.lineEdit.text()
        Lname = self.MainWindow.ManagerManageStaff.lineEdit.text()
        StartDate = self.MainWindow.ManagerManageStaff.dateEdit.date().toPyDate()
        EndDate = self.MainWindow.ManagerManageStaff.dateEdit_2.date().toPyDate()
        Fname = setNone(Fname)
        Lname = setNone(Lname)
        if Site == 'All':
            Site = None
        tableData = DataBaseManager.GetAllStaffByFilterBySite_Fname_Lname_StartDate_EndDate(Site, Fname, Lname, StartDate, EndDate)
        self.MainWindow.ManagerManageStaff.tableWidget.setSortingEnabled(False)
        for i in range(len(tableData)):
            self.MainWindow.ManagerManageStaff.tableWidget.insertRow(i)
            newItem = QtWidgets.QTableWidgetItem()
            newItem.setText(str(tableData[i]['fname'] + ' ' + tableData[i]['lname']))
            self.MainWindow.ManagerManageStaff.tableWidget.setItem(i, 0, newItem)
            newItem = QtWidgets.QTableWidgetItem()
            newItem.setText(str(tableData[i]['event_shifts']))
            self.MainWindow.ManagerManageStaff.tableWidget.setItem(i, 1, newItem)
        self.MainWindow.ManagerManageStaff.tableWidget.setSortingEnabled(True)

    def showManagerSiteReport(self):
        self.MainWindow.close()
        self.MainWindow = MainWindow()
        self.MainWindow.startManagerSiteReport()
        if self.user == 'User':
            self.MainWindow.ManagerSiteReport.pushButton_3.clicked.connect(self.showUserFunctionality)
        elif self.user == "Staff":
            self.MainWindow.ManagerSiteReport.pushButton_3.clicked.connect(self.showStaffFunctionality)
        elif self.user == 'Manager':
            self.MainWindow.ManagerSiteReport.pushButton_3.clicked.connect(self.showManagerFunctionality)
        elif self.user == 'Administrator':
            self.MainWindow.ManagerSiteReport.pushButton_3.clicked.connect(self.showAdministratorFunctionality)
        elif self.user == 'StaffVisitor':
            self.MainWindow.ManagerSiteReport.pushButton_3.clicked.connect(self.showStaffVisitorFunctionality)
        elif self.user == 'ManagerVisitor':
            self.MainWindow.ManagerSiteReport.pushButton_3.clicked.connect(self.showManagerVisitorFunctionality)
        elif self.user == 'AdministratorVisitor':
            self.MainWindow.ManagerSiteReport.pushButton_3.clicked.connect(self.showAdminVisitorFunctionality)
        elif self.user == 'Visitor':
            self.MainWindow.ManagerSiteReport.pushButton_3.clicked.connect(self.showVisitorFunctionality)
        self.MainWindow.ManagerSiteReport.pushButton_2.clicked.connect(self.showManagerDailyDetail)
        self.MainWindow.ManagerSiteReport.pushButton.clicked.connect(self.filterSiteReport)
        self.MainWindow.ManagerSiteReport.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.MainWindow.ManagerSiteReport.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.MainWindow.ManagerSiteReport.dateEdit.setDate(QtCore.QDate.currentDate())
        self.MainWindow.ManagerSiteReport.dateEdit_2.setDate(QtCore.QDate.currentDate())

    def filterSiteReport(self):
        StartDate = self.MainWindow.ManagerSiteReport.dateEdit.date().toPyDate()
        EndDate = self.MainWindow.ManagerSiteReport.dateEdit_2.date().toPyDate()
        LowEventCountRange = self.MainWindow.ManagerSiteReport.lineEdit.text()
        HighEventCountRange = self.MainWindow.ManagerSiteReport.lineEdit_2.text()
        LowStaffCountRange = self.MainWindow.ManagerSiteReport.lineEdit_3.text()
        HightStaffCountRange = self.MainWindow.ManagerSiteReport.lineEdit_4.text()
        LowTotalVisitsRange = self.MainWindow.ManagerSiteReport.lineEdit_5.text()
        HighTotalVisitRange = self.MainWindow.ManagerSiteReport.lineEdit_6.text()
        LowTotalRevenueRange = self.MainWindow.ManagerSiteReport.lineEdit_7.text()
        HighTotalRevenueRange = self.MainWindow.ManagerSiteReport.lineEdit_8.text()
        if len(LowEventCountRange) == 0 and len(HighEventCountRange) == 0:
            LowEventCountRange = None
            HighEventCountRange = None
        elif len(LowEventCountRange) * len(HighEventCountRange) == 0:
            return QtWidgets.QMessageBox.warning(self.MainWindow, "Range not valid", "Please enter both ranges",
                                                 QtWidgets.QMessageBox.Ok)
        if len(LowStaffCountRange) == 0 and len(HightStaffCountRange) == 0:
            LowStaffCountRange = None
            HightStaffCountRange = None
        elif len(LowStaffCountRange) * len(HightStaffCountRange) == 0:
            return QtWidgets.QMessageBox.warning(self.MainWindow, "Range not valid", "Please enter both ranges",
                                                 QtWidgets.QMessageBox.Ok)
        if len(LowTotalVisitsRange) == 0 and len(HighTotalVisitRange) == 0:
            LowTotalVisitsRange = None
            HighTotalVisitRange = None
        elif len(LowTotalVisitsRange) * len(HighTotalVisitRange) == 0:
            return QtWidgets.QMessageBox.warning(self.MainWindow, "Range not valid", "Please enter both ranges",
                                                 QtWidgets.QMessageBox.Ok)
        if len(LowTotalRevenueRange) == 0 and len(HighTotalRevenueRange) == 0:
            LowTotalRevenueRange = None
            HighTotalRevenueRange = None
        elif len(LowTotalRevenueRange) * len(HighTotalRevenueRange) == 0:
            return QtWidgets.QMessageBox.warning(self.MainWindow, "Range not valid", "Please enter both ranges",
                                                 QtWidgets.QMessageBox.Ok)
        tableData = DataBaseManager.GetAllSiteReportByFilter(self.username, StartDate, EndDate, LowEventCountRange, HighEventCountRange, LowStaffCountRange, HightStaffCountRange, LowTotalVisitsRange, HighTotalVisitRange, LowTotalRevenueRange, HighTotalRevenueRange)
        self.MainWindow.ManagerSiteReport.tableWidget.setSortingEnabled(False)
        for i in range(len(tableData)):
            self.MainWindow.ManagerSiteReport.tableWidget.insertRow(i)
            for column, key in enumerate(tableData[i].keys()):
                newItem = QtWidgets.QTableWidgetItem()
                newItem.setText(str(tableData[i][key]))
                self.MainWindow.ManagerSiteReport.tableWidget.setItem(i, column, newItem)
        self.MainWindow.ManagerSiteReport.tableWidget.setSortingEnabled(True)

    def showManagerDailyDetail(self):
        if not len(self.MainWindow.ManagerSiteReport.tableWidget.selectionModel().selectedRows()):
            return QtWidgets.QMessageBox.warning(self.MainWindow, "Haven't selected a row",
                                                 "Please select a row before seeing detail",
                                                 QtWidgets.QMessageBox.Ok)
        Date = self.MainWindow.ManagerSiteReport.tableWidget.selectionModel().selectedRows()[0]
        selectedDate = self.MainWindow.ManagerSiteReport.tableWidget.item(Date.row(), 0).text()
        selectedDate = datetime.strptime(selectedDate, '%Y-%m-%d').date()
        self.MainWindow.close()
        self.MainWindow = MainWindow()
        self.MainWindow.startManagerDailyDetail()
        self.MainWindow.ManagerDailyDetail.pushButton.clicked.connect(self.showManagerSiteReport)
        tableData = DataBaseManager.GetDailyDetail(selectedDate)
        self.MainWindow.ManagerDailyDetail.tableWidget.setSortingEnabled(False)
        for i in range(len(tableData)):
            self.MainWindow.ManagerDailyDetail.tableWidget.insertRow(i)
            for column, key in enumerate(tableData[i].keys()):
                newItem = QtWidgets.QTableWidgetItem()
                newItem.setText(str(tableData[i][key]))
                self.MainWindow.ManagerDailyDetail.tableWidget.setItem(i, column, newItem)
            self.MainWindow.ManagerDailyDetail.tableWidget.setItem(i, 4, newItem)
        self.MainWindow.ManagerDailyDetail.tableWidget.setSortingEnabled(True)

        # if self.user == 'User':
        #     self.MainWindow.ManagerDailyDetail.pushButton.clicked.connect(self.showUserFunctionality)
        # elif self.user == "Staff":
        #     self.MainWindow.ManagerDailyDetail.pushButton.clicked.connect(self.showStaffFunctionality)
        # elif self.user == 'Manager':
        #     self.MainWindow.ManagerDailyDetail.pushButton.clicked.connect(self.showManagerFunctionality)
        # elif self.user == 'Administrator':
        #     self.MainWindow.ManagerDailyDetail.pushButton.clicked.connect(self.showAdministratorFunctionality)
        # elif self.user == 'StaffVisitor':
        #     self.MainWindow.ManagerDailyDetail.pushButton.clicked.connect(self.showStaffVisitorFunctionality)
        # elif self.user == 'ManagerVisitor':
        #     self.MainWindow.ManagerDailyDetail.pushButton.clicked.connect(self.showManagerVisitorFunctionality)
        # elif self.user == 'AdministratorVisitor':
        #     self.MainWindow.ManagerDailyDetail.pushButton.clicked.connect(self.showAdminVisitorFunctionality)
        # elif self.user == 'Visitor':
        #     self.MainWindow.ManagerDailyDetail.pushButton.clicked.connect(self.showVisitorFunctionality)

    def showStaffViewSchedule(self):
        self.MainWindow.close()
        self.MainWindow = MainWindow()
        self.MainWindow.startStaffViewSchedule()
        self.MainWindow.StaffViewSchedule.pushButton.clicked.connect(self.filterStaffViewSchedule)
        self.MainWindow.StaffViewSchedule.pushButton_2.clicked.connect(self.showStaffEventDetail)
        if self.user == 'User':
            self.MainWindow.StaffViewSchedule.pushButton_3.clicked.connect(self.showUserFunctionality)
        elif self.user == "Staff":
            self.MainWindow.StaffViewSchedule.pushButton_3.clicked.connect(self.showStaffFunctionality)
        elif self.user == 'Manager':
            self.MainWindow.StaffViewSchedule.pushButton_3.clicked.connect(self.showManagerFunctionality)
        elif self.user == 'Administrator':
            self.MainWindow.StaffViewSchedule.pushButton_3.clicked.connect(self.showAdministratorFunctionality)
        elif self.user == 'StaffVisitor':
            self.MainWindow.StaffViewSchedule.pushButton_3.clicked.connect(self.showStaffVisitorFunctionality)
        elif self.user == 'ManagerVisitor':
            self.MainWindow.StaffViewSchedule.pushButton_3.clicked.connect(self.showManagerVisitorFunctionality)
        elif self.user == 'AdministratorVisitor':
            self.MainWindow.StaffViewSchedule.pushButton_3.clicked.connect(self.showAdminVisitorFunctionality)
        elif self.user == 'Visitor':
            self.MainWindow.StaffViewSchedule.pushButton_3.clicked.connect(self.showVisitorFunctionality)
        self.MainWindow.StaffViewSchedule.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.MainWindow.StaffViewSchedule.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.MainWindow.StaffViewSchedule.dateEdit.setDate(QtCore.QDate.currentDate())
        self.MainWindow.StaffViewSchedule.dateEdit_2.setDate(QtCore.QDate.currentDate())

    def filterStaffViewSchedule(self):
        EventName = self.MainWindow.StaffViewSchedule.lineEdit.text()
        DescriptionKeyword = self.MainWindow.StaffViewSchedule.lineEdit_2.text()
        StartDate = self.MainWindow.StaffViewSchedule.dateEdit.date().toPyDate()
        EndDate = self.MainWindow.StaffViewSchedule.dateEdit.date().toPyDate()
        EventName = setNone(EventName)
        DescriptionKeyword = setNone(DescriptionKeyword)
        tableData = DataBaseManager.StaffViewScheduleTableFilter(EventName, DescriptionKeyword, StartDate, EndDate)
        self.MainWindow.StaffViewSchedule.tableWidget.setSortingEnabled(False)
        for i in range(len(tableData)):
            self.MainWindow.StaffViewSchedule.tableWidget.insertRow(i)
            for column, key in enumerate(tableData[i].keys()):
                newItem = QtWidgets.QTableWidgetItem()
                newItem.setText(str(tableData[i][key]))
                self.MainWindow.StaffViewSchedule.tableWidget.setItem(i, column, newItem)
        self.MainWindow.StaffViewSchedule.tableWidget.setSortingEnabled(True)


    def showStaffEventDetail(self):
        if not len(self.MainWindow.StaffViewSchedule.tableWidget.selectionModel().selectedRows()):
            return QtWidgets.QMessageBox.warning(self.MainWindow, "No row selected", "Please select a row",
                                                 QtWidgets.QMessageBox.Ok)
        Event = self.MainWindow.StaffViewSchedule.tableWidget.selectionModel().selectedRows()[0]
        EventName = self.MainWindow.StaffViewSchedule.tableWidget.item(Event.row(), 0).text()
        Site = self.MainWindow.StaffViewSchedule.tableWidget.item(Event.row(), 1).text()
        self.MainWindow.close()
        self.MainWindow = MainWindow()
        self.MainWindow.startStaffEventDetail()
        self.MainWindow.StaffEventDetail.pushButton.clicked.connect(self.showStaffViewSchedule)
        allData = DataBaseManager.StaffEventDetail(Site)
        print(allData)
        self.MainWindow.StaffEventDetail.textBrowser.setText(allData['event_name'])
        self.MainWindow.StaffEventDetail.textBrowser_2.setText(allData['sitename'])
        self.MainWindow.StaffEventDetail.textBrowser_3.setText(str(allData['startdate']))
        self.MainWindow.StaffEventDetail.textBrowser_4.setText((allData['duration']))
        self.MainWindow.StaffEventDetail.textBrowser_5.setText(str(allData['endate']))
        self.MainWindow.StaffEventDetail.textBrowser_6.setText(str(allData['fname'] + ' ' + allData['lname']))
        self.MainWindow.StaffEventDetail.textBrowser_7.setText(str(allData['capacity']))
        self.MainWindow.StaffEventDetail.textBrowser_8.setText(str(allData['price']))
        self.MainWindow.StaffEventDetail.textBrowser_9.setText(allData['Description'])
        # if self.user == 'User':
        #     self.MainWindow.StaffEventDetail.pushButton.clicked.connect(self.showUserFunctionality)
        # elif self.user == "Staff":
        #     self.MainWindow.StaffEventDetail.pushButton.clicked.connect(self.showStaffFunctionality)
        # elif self.user == 'Manager':
        #     self.MainWindow.StaffEventDetail.pushButton.clicked.connect(self.showManagerFunctionality)
        # elif self.user == 'Administrator':
        #     self.MainWindow.StaffEventDetail.pushButton.clicked.connect(self.showAdministratorFunctionality)
        # elif self.user == 'StaffVisitor':
        #     self.MainWindow.StaffEventDetail.pushButton.clicked.connect(self.showStaffVisitorFunctionality)
        # elif self.user == 'ManagerVisitor':
        #     self.MainWindow.StaffEventDetail.pushButton.clicked.connect(self.showManagerVisitorFunctionality)
        # elif self.user == 'AdministratorVisitor':
        #     self.MainWindow.StaffEventDetail.pushButton.clicked.connect(self.showAdminVisitorFunctionality)
        # elif self.user == 'Visitor':
        #     self.MainWindow.StaffEventDetail.pushButton.clicked.connect(self.showVisitorFunctionality)

    def showVisitorExploreEvent(self):
        self.MainWindow.close()
        self.MainWindow = MainWindow()
        self.MainWindow.startVisitorExploreEvent()
        self.MainWindow.VisitorExploreEvent.pushButton.clicked.connect(self.filterVisitorEvents)
        self.MainWindow.VisitorExploreEvent.pushButton_2.clicked.connect(self.showVisitorEventDetail)
        allSites = ['All']
        self.MainWindow.VisitorExploreEvent.comboBox.addItems(allSites)
        if self.user == 'User':
            self.MainWindow.VisitorExploreEvent.pushButton_3.clicked.connect(self.showUserFunctionality)
        elif self.user == "Staff":
            self.MainWindow.VisitorExploreEvent.pushButton_3.clicked.connect(self.showStaffFunctionality)
        elif self.user == 'Manager':
            self.MainWindow.VisitorExploreEvent.pushButton_3.clicked.connect(self.showManagerFunctionality)
        elif self.user == 'Administrator':
            self.MainWindow.VisitorExploreEvent.pushButton_3.clicked.connect(self.showAdministratorFunctionality)
        elif self.user == 'StaffVisitor':
            self.MainWindow.VisitorExploreEvent.pushButton_3.clicked.connect(self.showStaffVisitorFunctionality)
        elif self.user == 'ManagerVisitor':
            self.MainWindow.VisitorExploreEvent.pushButton_3.clicked.connect(self.showManagerVisitorFunctionality)
        elif self.user == 'AdministratorVisitor':
            self.MainWindow.VisitorExploreEvent.pushButton_3.clicked.connect(self.showAdminVisitorFunctionality)
        elif self.user == 'Visitor':
            self.MainWindow.VisitorExploreEvent.pushButton_3.clicked.connect(self.showVisitorFunctionality)
        self.MainWindow.VisitorExploreEvent.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.MainWindow.VisitorExploreEvent.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)

    def filterVisitorEvents(self):
        Name = self.MainWindow.VisitorExploreEvent.lineEdit.text()
        DescriptionKeyword = self.MainWindow.VisitorExploreEvent.lineEdit_2.text()
        SiteName = self.MainWindow.VisitorExploreEvent.comboBox.currentText()
        StartDate = self.MainWindow.VisitorExploreEvent.dateEdit.date().toPyDate()
        EndDate = self.MainWindow.VisitorExploreEvent.dateEdit_2.date().toPyDate()
        IncludeVisited = self.MainWindow.VisitorExploreEvent.checkBox.isChecked()
        IncludeSoldOut = self.MainWindow.VisitorExploreEvent.checkBox_2.isChecked()
        LowTotalVisitRange = self.MainWindow.VisitorExploreEvent.lineEdit_5.text()
        HighTotalVisitRange = self.MainWindow.VisitorExploreEvent.lineEdit_6.text()
        LowTicketPriceRange = self.MainWindow.VisitorExploreEvent.lineEdit_7.text()
        HighTicketPriceRange = self.MainWindow.VisitorExploreEvent.lineEdit_8.text()
        if SiteName == 'All':
            SiteName = None
        if len(LowTotalVisitRange) == 0 and len(HighTotalVisitRange) == 0:
            LowTotalVisitRange = None
            HighTotalVisitRange = None
        elif len(LowTotalVisitRange) * len(HighTotalVisitRange) == 0:
            return QtWidgets.QMessageBox.warning(self.MainWindow, "Range not valid", "Please enter both ranges",
                                                 QtWidgets.QMessageBox.Ok)
        if len(LowTicketPriceRange) == 0 and len(HighTicketPriceRange) == 0:
            LowTicketPriceRange = None
            HighTicketPriceRange = None
        elif len(LowTicketPriceRange) * len(HighTicketPriceRange) == 0:
            return QtWidgets.QMessageBox.warning(self.MainWindow, "Range not valid", "Please enter both ranges",
                                                 QtWidgets.QMessageBox.Ok)
        Name = setNone(Name)
        DescriptionKeyword = setNone(DescriptionKeyword)
        tableData = DataBaseManager.VistorExploreEvent(self.username, Name, DescriptionKeyword, SiteName, StartDate, EndDate, LowTotalVisitRange, HighTotalVisitRange, LowTicketPriceRange, HighTicketPriceRange)
        self.MainWindow.VisitorExploreEvent.tableWidget.setSortingEnabled(False)
        for i in range(len(tableData)):
            self.MainWindow.VisitorExploreEvent.tableWidget.insertRow(i)
            for column, key in enumerate(tableData[i].keys()):
                newItem = QtWidgets.QTableWidgetItem()
                newItem.setText(str(tableData[i][key]))
                self.MainWindow.VisitorExploreEvent.tableWidget.setItem(i, column, newItem)
                if column == 5:
                    break
            newItem = QtWidgets.QTableWidgetItem()
            newItem.setText(str(tableData[i]['my_visit']))
            self.MainWindow.VisitorExploreEvent.tableWidget.setItem(i, 5, newItem)
        self.MainWindow.VisitorExploreEvent.tableWidget.setSortingEnabled(True)
        self.MainWindow.VisitorExploreEvent.tableData = tableData

    def showVisitorEventDetail(self):
        Event = self.MainWindow.VisitorExploreEvent.tableWidget.selectionModel().selectedRows()[0]
        EventDate = self.MainWindow.VisitorExploreEvent.dateEdit.date().toPyDate()
        SiteName = self.MainWindow.VisitorExploreEvent.tableWidget.item(Event.row(), 1).text()
        EventName = self.MainWindow.VisitorExploreEvent.tableWidget.item(Event.row(), 0).text()
        for data in self.MainWindow.VisitorExploreEvent.tableData:
            if data['event_name'] == EventName and data['sitename'] == SiteName:
                EventDate = data['startdate']
        self.MainWindow.close()
        self.MainWindow = MainWindow()
        self.MainWindow.startVisitorEventDetail()
        self.MainWindow.VisitorEventDetail.pushButton.clicked.connect(self.showVisitorExploreEvent)
        self.MainWindow.VisitorEventDetail.pushButton_2.clicked.connect(self.LogVisit)
        self.MainWindow.VisitorEventDetail.startDate = EventDate
        VisitorEventDetailDB = DataBaseManager.VisitorEventDetail(SiteName, EventName, EventDate)
        self.MainWindow.VisitorEventDetail.textBrowser.setText(VisitorEventDetailDB['event_name'])
        self.MainWindow.VisitorEventDetail.textBrowser_2.setText(VisitorEventDetailDB['sitename'])
        self.MainWindow.VisitorEventDetail.textBrowser_3.setText(str(EventDate))
        self.MainWindow.VisitorEventDetail.textBrowser_4.setText(str(VisitorEventDetailDB['endate']))
        self.MainWindow.VisitorEventDetail.textBrowser_5.setText(str(VisitorEventDetailDB['ticket_price']))
        self.MainWindow.VisitorEventDetail.textBrowser_6.setText(str(VisitorEventDetailDB['tickets_remainig']))
        self.MainWindow.VisitorEventDetail.textBrowser_7.setText(VisitorEventDetailDB['event_description'])
        # if self.user == 'User':
        #     self.MainWindow.VisitorEventDetail.pushButton.clicked.connect(self.showUserFunctionality)
        # elif self.user == "Staff":
        #     self.MainWindow.VisitorEventDetail.pushButton.clicked.connect(self.showStaffFunctionality)
        # elif self.user == 'Manager':
        #     self.MainWindow.VisitorEventDetail.pushButton.clicked.connect(self.showManagerFunctionality)
        # elif self.user == 'Administrator':
        #     self.MainWindow.VisitorEventDetail.pushButton.clicked.connect(self.showAdministratorFunctionality)
        # elif self.user == 'StaffVisitor':
        #     self.MainWindow.VisitorEventDetail.pushButton.clicked.connect(self.showStaffVisitorFunctionality)
        # elif self.user == 'ManagerVisitor':
        #     self.MainWindow.VisitorEventDetail.pushButton.clicked.connect(self.showManagerVisitorFunctionality)
        # elif self.user == 'AdministratorVisitor':
        #     self.MainWindow.VisitorEventDetail.pushButton.clicked.connect(self.showAdminVisitorFunctionality)
        # elif self.user == 'Visitor':
        #     self.MainWindow.VisitorEventDetail.pushButton.clicked.connect(self.showVisitorFunctionality)

    def LogVisit(self):
        visitDate = self.MainWindow.VisitorEventDetail.dateEdit.date().toPyDate()
        EventName = self.MainWindow.VisitorEventDetail.textBrowser.toPlainText()
        Sitename = self.MainWindow.VisitorEventDetail.textBrowser_2.toPlainText()
        StartDate = self.MainWindow.VisitorEventDetail.textBrowser_3.toPlainText()
        EndDate = self.MainWindow.VisitorEventDetail.textBrowser_4.toPlainText()
        DataBaseManager.VisitorEventLogVisit(visitDate, EventName, Sitename, StartDate, EndDate, self.username)


    def showVisitorExploreSite(self):
        self.MainWindow.close()
        self.MainWindow = MainWindow()
        self.MainWindow.startVisitorExploreSite()
        self.MainWindow.VisitorExploreSite.pushButton.clicked.connect(self.filterVisitorSites)
        allSites = ['All']
        self.MainWindow.VisitorExploreSite.comboBox.addItems(allSites)
        self.MainWindow.VisitorExploreSite.comboBox_2.addItems(['All', 'Yes', 'No'])
        self.MainWindow.VisitorExploreSite.pushButton_2.clicked.connect(self.showVisitorSiteDetail)
        self.MainWindow.VisitorExploreSite.pushButton_3.clicked.connect(self.showVisitorTransitDetail)
        if self.user == 'User':
            self.MainWindow.VisitorExploreSite.pushButton_4.clicked.connect(self.showUserFunctionality)
        elif self.user == "Staff":
            self.MainWindow.VisitorExploreSite.pushButton_4.clicked.connect(self.showStaffFunctionality)
        elif self.user == 'Manager':
            self.MainWindow.VisitorExploreSite.pushButton_4.clicked.connect(self.showManagerFunctionality)
        elif self.user == 'Administrator':
            self.MainWindow.VisitorExploreSite.pushButton_4.clicked.connect(self.showAdministratorFunctionality)
        elif self.user == 'StaffVisitor':
            self.MainWindow.VisitorExploreSite.pushButton_4.clicked.connect(self.showStaffVisitorFunctionality)
        elif self.user == 'ManagerVisitor':
            self.MainWindow.VisitorExploreSite.pushButton_4.clicked.connect(self.showManagerVisitorFunctionality)
        elif self.user == 'AdministratorVisitor':
            self.MainWindow.VisitorExploreSite.pushButton_4.clicked.connect(self.showAdminVisitorFunctionality)
        elif self.user == 'Visitor':
            self.MainWindow.VisitorExploreSite.pushButton_4.clicked.connect(self.showVisitorFunctionality)
        self.MainWindow.VisitorExploreSite.dateEdit.setDate(QtCore.QDate.currentDate())
        self.MainWindow.VisitorExploreSite.dateEdit_2.setDate(QtCore.QDate.currentDate())
        self.MainWindow.VisitorExploreSite.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.MainWindow.VisitorExploreSite.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)

    def filterVisitorSites(self):
        Name = self.MainWindow.VisitorExploreSite.comboBox.currentText()
        OpenEveryday = self.MainWindow.VisitorExploreSite.comboBox_2.currentText()
        StartDate = self.MainWindow.VisitorExploreSite.dateEdit.date().toPyDate()
        EndDate = self.MainWindow.VisitorExploreSite.dateEdit_2.date().toPyDate()
        LowTotalVisitRange = self.MainWindow.VisitorExploreSite.lineEdit.text()
        HighTotalVisitRange = self.MainWindow.VisitorExploreSite.lineEdit_2.text()
        LowEventCount = self.MainWindow.VisitorExploreSite.lineEdit_3.text()
        HighEventCount = self.MainWindow.VisitorExploreSite.lineEdit_4.text()
        IncludeVisited = self.MainWindow.VisitorExploreSite.checkBox_2.isChecked()
        Name = setNone(Name)
        if len(OpenEveryday) == 0:
            OpenEveryday = None
        else:
            OpenEveryday = False if OpenEveryday == 'No' else 'Yes'
        if len(LowTotalVisitRange) == 0 and len(HighTotalVisitRange) == 0:
            LowTotalVisitRange = None
            HighTotalVisitRange = None
        elif len(LowTotalVisitRange) * len(HighTotalVisitRange) == 0:
            return QtWidgets.QMessageBox.warning(self.MainWindow, "Range not valid", "Please enter both ranges",
                                                 QtWidgets.QMessageBox.Ok)
        if len(LowEventCount) == 0 and len(HighEventCount) == 0:
            LowEventCount = None
            HighEventCount = None
        elif len(LowEventCount) * len(HighEventCount) == 0:
            return QtWidgets.QMessageBox.warning(self.MainWindow, "Range not valid", "Please enter both ranges",
                                                 QtWidgets.QMessageBox.Ok)
        tableData = DataBaseManager.VisitorExploreSite(self.username, Name, OpenEveryday, StartDate, EndDate, LowTotalVisitRange, HighTotalVisitRange, LowEventCount, HighEventCount)
        self.MainWindow.VisitorExploreSite.tableWidget.setRowCount(0)
        self.MainWindow.VisitorExploreSite.tableWidget.setSortingEnabled(False)
        for i in range(len(tableData)):
            self.MainWindow.VisitorExploreSite.tableWidget.insertRow(i)
            for column, key in enumerate(tableData[i].keys()):
                newItem = QtWidgets.QTableWidgetItem()
                newItem.setText(str(tableData[i][key]))
                self.MainWindow.VisitorExploreSite.tableWidget.setItem(i, column, newItem)
        self.MainWindow.VisitorExploreSite.tableWidget.setSortingEnabled(True)


    def showVisitorTransitDetail(self):
        self.MainWindow.close()
        self.MainWindow = MainWindow()
        self.MainWindow.startVisitorTransitDetail()
        self.MainWindow.VisitorTransitDetail.pushButton.clicked.connect(self.showVisitorExploreSite)
        self.MainWindow.VisitorTransitDetail.pushButton_2.clicked.connect(self.LogVisitorTransit)
        self.MainWindow.VisitorTransitDetail.comboBox.addItems(['All', 'MARTA', 'Bus', 'Bike'])
        self.MainWindow.VisitorTransitDetail.dateEdit.setDate(QtCore.QDate.currentDate())
        self.MainWindow.VisitorTransitDetail.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.MainWindow.VisitorTransitDetail.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.MainWindow.VisitorTransitDetail.comboBox.currentTextChanged.connect(self.GetVisitorTransitDetail)
        self.GetVisitorTransitDetail()
        # if self.user == 'User':
        #     self.MainWindow.VisitorTransitDetail.pushButton.clicked.connect(self.showUserFunctionality)
        # elif self.user == "Staff":
        #     self.MainWindow.VisitorTransitDetail.pushButton.clicked.connect(self.showStaffFunctionality)
        # elif self.user == 'Manager':
        #     self.MainWindow.VisitorTransitDetail.pushButton.clicked.connect(self.showManagerFunctionality)
        # elif self.user == 'Administrator':
        #     self.MainWindow.VisitorTransitDetail.pushButton.clicked.connect(self.showAdministratorFunctionality)
        # elif self.user == 'StaffVisitor':
        #     self.MainWindow.VisitorTransitDetail.pushButton.clicked.connect(self.showStaffVisitorFunctionality)
        # elif self.user == 'ManagerVisitor':
        #     self.MainWindow.VisitorTransitDetail.pushButton.clicked.connect(self.showManagerVisitorFunctionality)
        # elif self.user == 'AdministratorVisitor':
        #     self.MainWindow.VisitorTransitDetail.pushButton.clicked.connect(self.showAdminVisitorFunctionality)
        # elif self.user == 'Visitor':
        #     self.MainWindow.VisitorTransitDetail.pushButton.clicked.connect(self.showVisitorFunctionality)

    def GetVisitorTransitDetail(self):
        Site = self.MainWindow.VisitorTransitDetail.label_2.text()
        Site = setNone(Site)
        TransportType = self.MainWindow.VisitorTransitDetail.comboBox.currentText()
        if len(TransportType) == 0:
            TransportType = None
        tableData = DataBaseManager.fetchVisitorTransitDetail(Site, TransportType)
        self.MainWindow.VisitorTransitDetail.tableWidget.setRowCount(0)
        self.MainWindow.VisitorTransitDetail.tableWidget.setSortingEnabled(False)
        for i in range(len(tableData)):
            self.MainWindow.VisitorTransitDetail.tableWidget.insertRow(i)
            for column, key in enumerate(tableData[i].keys()):
                newItem = QtWidgets.QTableWidgetItem()
                newItem.setText(str(tableData[i][key]))
                self.MainWindow.VisitorTransitDetail.tableWidget.setItem(i, column, newItem)
        self.MainWindow.VisitorTransitDetail.tableWidget.setSortingEnabled(True)

    def LogVisitorTransit(self):
        Site = self.MainWindow.VisitorTransitDetail.label_2.text()
        TransportType = self.MainWindow.VisitorTransitDetail.comboBox.currentText()
        TransitDate = self.MainWindow.VisitorTransitDetail.dateEdit.date().toPyDate()
        Route = self.MainWindow.AdministratorManageUser.tableWidget.selectionModel().selectedRows()[0]
        RouteName = self.MainWindow.AdministratorManageUser.tableWidget.item(Route.row(), 0).text()
        TType = self.MainWindow.AdministratorManageUser.tableWidget.item(Route.row(), 1).text()

    def showVisitorSiteDetail(self):
        Site = self.MainWindow.VisitorExploreSite.tableWidget.selectionModel().selectedRows()
        if (len(Site)) == 0:
            return QtWidgets.QMessageBox.warning(self.MainWindow, "Please select a row", "Please select a row",
                                                 QtWidgets.QMessageBox.Ok)
        Site = Site[0]
        Sitename = self.MainWindow.VisitorExploreSite.tableWidget.item(Site.row(), 0).text()
        self.MainWindow.close()
        self.MainWindow = MainWindow()
        self.MainWindow.startVisitorSiteDetail()
        self.MainWindow.VisitorSiteDetail.pushButton.clicked.connect(self.showVisitorExploreSite)
        self.MainWindow.VisitorSiteDetail.pushButton_2.clicked.connect(self.LogVisitorVisit)
        self.MainWindow.VisitorSiteDetail.dateEdit.setDate(QtCore.QDate.currentDate())
        tableData = DataBaseManager.fetchVisitorSiteDetail(Sitename)
        if len(tableData):
            self.MainWindow.VisitorSiteDetail.textBrowser.setText(tableData[0]['sitename'])
            self.MainWindow.VisitorSiteDetail.textBrowser_2.setText(str(tableData[0]['openeveryday']))
            self.MainWindow.VisitorSiteDetail.textBrowser_3.setTExt(str(tableData[0]['address']))
        # if self.user == 'User':
        #     self.MainWindow.VisitorSiteDetail.pushButton.clicked.connect(self.showUserFunctionality)
        # elif self.user == "Staff":
        #     self.MainWindow.VisitorSiteDetail.pushButton.clicked.connect(self.showStaffFunctionality)
        # elif self.user == 'Manager':
        #     self.MainWindow.VisitorSiteDetail.pushButton.clicked.connect(self.showManagerFunctionality)
        # elif self.user == 'Administrator':
        #     self.MainWindow.VisitorSiteDetail.pushButton.clicked.connect(self.showAdministratorFunctionality)
        # elif self.user == 'StaffVisitor':
        #     self.MainWindow.VisitorSiteDetail.pushButton.clicked.connect(self.showStaffVisitorFunctionality)
        # elif self.user == 'ManagerVisitor':
        #     self.MainWindow.VisitorSiteDetail.pushButton.clicked.connect(self.showManagerVisitorFunctionality)
        # elif self.user == 'AdministratorVisitor':
        #     self.MainWindow.VisitorSiteDetail.pushButton.clicked.connect(self.showAdminVisitorFunctionality)
        # elif self.user == 'Visitor':
        #     self.MainWindow.VisitorSiteDetail.pushButton.clicked.connect(self.showVisitorFunctionality)

    def LogVisitorVisit(self):
        Site = self.MainWindow.VisitorSiteDetail.textBrowser.toPlainText()
        OpenEveryday = self.MainWindow.VisitorSiteDetail.textBrowser_2.toPlainText()
        Address = self.MainWindow.VisitorSiteDetail.textBrowser_3.toPlainText()
        VisitDate = self.MainWindow.VisitorSiteDetail.dateEdit.date().toPyDate()
        DataBaseManager.log_visit_to_site(self.username, Site)

    def showVisitorVisitHistory(self):
        self.MainWindow.close()
        self.MainWindow = MainWindow()
        self.MainWindow.startVisitorVisitHistory()
        self.MainWindow.VisitorVisitHistory.pushButton.clicked.connect(self.FilterVisitorVisitHistory)
        allSites = ['All']
        self.MainWindow.VisitorVisitHistory.comboxBox.addItems(allSites)
        if self.user == 'User':
            self.MainWindow.VisitorVisitHistory.pushButton_2.clicked.connect(self.showUserFunctionality)
        elif self.user == "Staff":
            self.MainWindow.VisitorVisitHistory.pushButton_2.clicked.connect(self.showStaffFunctionality)
        elif self.user == 'Manager':
            self.MainWindow.VisitorVisitHistory.pushButton_2.clicked.connect(self.showManagerFunctionality)
        elif self.user == 'Administrator':
            self.MainWindow.VisitorVisitHistory.pushButton_2.clicked.connect(self.showAdministratorFunctionality)
        elif self.user == 'StaffVisitor':
            self.MainWindow.VisitorVisitHistory.pushButton_2.clicked.connect(self.showStaffVisitorFunctionality)
        elif self.user == 'ManagerVisitor':
            self.MainWindow.VisitorVisitHistory.pushButton_2.clicked.connect(self.showManagerVisitorFunctionality)
        elif self.user == 'AdministratorVisitor':
            self.MainWindow.VisitorVisitHistory.pushButton_2.clicked.connect(self.showAdminVisitorFunctionality)
        elif self.user == 'Visitor':
            self.MainWindow.VisitorVisitHistory.pushButton_2.clicked.connect(self.showVisitorFunctionality)
        self.MainWindow.VisitorVisitHistory.dateEdit_2.setDate(QtCore.QDate.currentDate())

    def FilterVisitorVisitHistory(self):
        self.MainWindow.VisitorVisitHistory.tableWidget.setRowCount(0)
        Event = self.MainWindow.VisitorVisitHistory.lineEdit.text()
        StartDate = self.MainWindow.VisitorVisitHistory.dateEdit.date().toPyDate()
        EndDate = self.MainWindow.VisitorVisitHistory.dateEdit_2.date().toPyDate()
        Site = self.MainWindow.VisitorVisitHistory.comboxBox.currentText()
        Event = setNone(Event)
        if Site == 'All':
            Site = None
        tableData = DataBaseManager.GetVisitorVisitHistory(self.username, Event, Site, StartDate, EndDate)
        self.MainWindow.VisitorVisitHistory.tableWidget.setSortingEnabled(False)
        for i in range(len(tableData)):
            self.MainWindow.VisitorVisitHistory.tableWidget.insertRow(i)
            for column, key in enumerate(tableData[i].keys()):
                newItem = QtWidgets.QTableWidgetItem()
                newItem.setText(str(tableData[i][key]))
                self.MainWindow.VisitorVisitHistory.tableWidget.setItem(i, column, newItem)
        self.MainWindow.VisitorVisitHistory.tableWidget.setSortingEnabled(True)



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    c = Controller()
    c.showLogin()
    sys.exit(app.exec_())
