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
        DataBaseManager.RegisterUser(Fname, Lname, Username, Password, Emails)
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
        Username = self.MainWindow.RegisterVistorOnlyPage.lineEdit_3.text()
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
        DataBaseManager.RegisterVisitor(Fname, Lname, Username, Password, Emails)
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
                  "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]
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
        if not Zipcode.isdigit():
            return QtWidgets.QMessageBox.warning(self.MainWindow, "Zipcode not valid", "Please confirm your zipcode", QtWidgets.QMessageBox.Ok)
        if not DataBaseManager.IsPhoneUnique(int(Phone)):
            return QtWidgets.QMessageBox.warning(self.MainWindow, "Phone already used", "Please use a new phone", QtWidgets.QMessageBox.Ok)
        if not DataBaseManager.IsUsernameUnique(Username):
            return QtWidgets.QMessageBox.warning(self.MainWindow, "Username not unique", "Please use a new username", QtWidgets.QMessageBox.Ok)
        DataBaseManager.RegisterEmployeeVisitor(Fname, Lname, Username, Password, Emails, self.generate_unique_employee_id(), int(Phone), Address, City, State, int(Zipcode), Erole)
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
        DataBaseManager.RegisterEmployeeVisitor(Fname, Lname, Username, Password, Emails, self.generate_unique_employee_id(), int(Phone), Address, City, State, int(Zipcode), Erole)
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
        TransitDate = self.MainWindow.UserTakeTransit.dateEdit.date()
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

    def declineUsers(self):
        print("Declined")

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
        self.MainWindow.AdministratorManageSite.comboBox.addItems(allSites)
        allManagers = ['All']
        self.MainWindow.AdministratorManageSite.comboBox_2.addItems(allManagers)
        self.MainWindow.AdministratorManageSite.comboBox_3.addItems(["Yes", "No"])
        self.MainWindow.AdministratorManageSite.pushButton_2.clicked.connect(self.showAdministratorCreateSite)
        self.MainWindow.AdministratorManageSite.pushButton_3.clicked.connect(self.showAdministratorEditSite)
        self.MainWindow.AdministratorManageSite.pushButton_4.clicked.connect(self.deleteSite)

    def filterSites(self):
        Site = self.MainWindow.AdministratorManageSite.comboBox.currentText()
        Manager = self.MainWindow.AdministratorManageSite.comboBox_2.currentText()
        OpenEveryday = self.MainWindow.AdministratorManageSite.comboBox_3.currentText()

    def deleteSite(self):
        print("Delete a site")

    def showAdministratorEditSite(self):
        self.MainWindow.close()
        self.MainWindow = MainWindow()
        self.MainWindow.startAdministratorEditSite()
        self.MainWindow.AdministratorEditSite.pushButton.clicked.connect(self.showAdministratorManageSite)
        self.MainWindow.AdministratorEditSite.pushButton_2.clicked.connect(self.editSite)
        allManagers = DataBaseManager.GetCurrentSiteManagerAndAllUnAssignedManagers()
        managerNames = []
        for manager in allManagers:
            managerNames.append(manager['name'])
        self.MainWindow.AdministratorEditSite.comboBox.addItems(managerNames)
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

    def editSite(self):
        Name = self.MainWindow.AdministratorEditSite.lineEdit.text()
        Zipcode = self.MainWindow.AdministratorEditSite.lineEdit_2.text()
        Address = self.MainWindow.AdministratorEditSite.lineEdit_3.text()
        Manager = self.MainWindow.AdministratorEditSite.comboBox.currentText()
        OpenEveryday = self.MainWindow.AdministratorEditSite.checkBox.isChecked()

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
        TransitType = self.MainWindow.AdministratorEditTransit.label_2.setText.text()
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
                siteName = data['sitename']
                startDate = data['startdate']
                Price = data['revenue']
                EndDate = data['endate']
        self.MainWindow.close()
        self.MainWindow = MainWindow()
        self.MainWindow.startManagerViewEditEvent()
        self.MainWindow.ManagerViewEditEvent.pushButton_3.clicked.connect(self.showManagerManageEvent)
        self.MainWindow.ManagerViewEditEvent.label_2.setText(EventName)
        self.MainWindow.ManagerViewEditEvent.label_4.setText(str(Price))
        self.MainWindow.ManagerViewEditEvent.label_6.setText(str(startDate))
        self.MainWindow.ManagerViewEditEvent.label_8.setText(str(EndDate))
        allStaff = DataBaseManager.StaffAssignedAndAvailibleStaffForEvent(EventName, siteName, startDate, EndDate)
        allAssignedStaff = DataBaseManager.GetAssignedStaffsForEvent(EventName, SiteName, startDate)
        allStaffNames = []
        allAssignedStaffNames = [each['fname'] + ' ' + each['lname'] for each in allAssignedStaff]
        for staff in allStaff:
            allStaffNames.append(allStaff['fname'] + ' ' + allStaff['lname'])
        self.MainWindow.ManagerViewEditEvent.listWidget.addItems(allStaffNames)
        for i in range(self.MainWindow.ManagerViewEditEvent.listWidget.count()):
            if self.MainWindow.ManagerViewEditEvent.listWidget.item(i).text() in allAssignedStaffNames:
                self.MainWindow.AdministratorEditTransit.listWidget.item(i).setSelected(True)
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
        staffAssigned = self.MainWindow.ManagerViewEditEvent.listWidget.selectedItems()
        LowDailyVisit = self.MainWindow.ManagerViewEditEvent.lineEdit.text()
        HighDailyVisit = self.MainWindow.ManagerViewEditEvent.lineEdit_2.text()
        LowDailyRevenue = self.MainWindow.ManagerViewEditEvent.lineEdit_3.text()
        HighDailyRevenue = self.MainWindow.ManagerViewEditEvent.lineEdit_4.text()
        Price = self.MainWindow.ManagerViewEditEvent.label_4.text()
        if len(LowDailyVisit) == 0 and len(HighDailyVisit) == 0:
            LowTotalRevenueRange = None
            HighTotalRevenueRange = None
        elif len(LowDailyVisit) * len(HighDailyVisit) == 0:
            return QtWidgets.QMessageBox.warning(self.MainWindow, "Range not valid", "Please enter both ranges",
                                                 QtWidgets.QMessageBox.Ok)
        if len(LowDailyRevenue) == 0 and len(HighDailyRevenue) == 0:
            LowTotalRevenueRange = None
            HighTotalRevenueRange = None
        elif len(LowDailyRevenue) * len(HighDailyRevenue) == 0:
            return QtWidgets.QMessageBox.warning(self.MainWindow, "Range not valid", "Please enter both ranges",
                                                 QtWidgets.QMessageBox.Ok)
        tableData = DataBaseManager.GetEventViewEditEventByFilterByVisitRange_RevenueRange(EventName, Price, LowDailyVisit, HighDailyVisit, LowDailyRevenue, HighDailyRevenue)
        print (tableData)

    def updateEvent(self, EventName, SiteName, startDate):
        staffAssigned = self.MainWindow.ManagerViewEditEvent.listWidget.selectedItems()
        Description = self.MainWindow.ManagerViewEditEvent.textBrowser.toPlainText()
        LowDailyVisit = self.MainWindow.ManagerViewEditEvent.lineEdit.text()
        HighDailyVisit = self.MainWindow.ManagerViewEditEvent.lineEdit_2.text()
        LowDailyRevenue = self.MainWindow.ManagerViewEditEvent.lineEdit_3.text()
        HighDailyRevenue = self.MainWindow.ManagerViewEditEvent.lineEdit_4.text()
        selectedStaff = self.MainWindow.ManagerViewEditEvent.listWidget.selectedItems()
        DataBaseManager.DeleteAllAssignedStaffsForEvent(EventName, SiteName, startDate)
        for staff in staffAssigned:
            DataBaseManager.AddAssignedStaffForEvent(staff.text(), SiteName, EventName, startDate)
        DataBaseManager.UpdateDescriptionForEvent(Description, SiteName, EventName, startDate)

    def showManagerCreateEvent(self):
        self.MainWindow.close()
        self.MainWindow = MainWindow()
        self.MainWindow.startManagerCreateEvent()
        self.MainWindow.ManagerCreateEvent.pushButton.clicked.connect(self.showManagerManageEvent)
        self.MainWindow.ManagerCreateEvent.pushButton.clicked.connect(self.createEvent)
        availableStaffs = []
        self.MainWindow.ManagerCreateEvent.listWidget.addItems(availableStaffs)
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

    def createEvent(self):
        startDate = self.MainWindow.ManagerCreateEvent.dateEdit.date()
        endDate = self.MainWindow.ManagerCreateEvent.dateEdit_2.date()
        Name = self.MainWindow.ManagerCreateEvent.lineEdit.text()
        Price = self.MainWindow.ManagerCreateEvent.lineEdit_2.text()
        Capacity = self.MainWindow.ManagerCreateEvent.lineEdit_3.text()
        MinStaffRequired = self.MainWindow.ManagerCreateEvent.lineEdit_4.text()
        Description = self.MainWindow.ManagerCreateEvent.textEdit.toPlainText()


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
        allSites = []
        self.MainWindow.ManagerManageStaff.comboBox.addItems(allSites)
        self.MainWindow.ManagerManageStaff.pushButton.clicked.connect(self.filterStaff)

    def filterStaff(self):
        Site = self.MainWindow.ManagerManageStaff.comboBox.currentText()
        Fname = self.MainWindow.ManagerManageStaff.lineEdit.text()
        Lname = self.MainWindow.ManagerManageStaff.lineEdit.text()
        StartDate = self.MainWindow.ManagerManageStaff.dateEdit.date()
        EndDate = self.MainWindow.ManagerManageStaff.dateEdit_2.date()

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

    def filterSiteReport(self):
        StartDate = self.MainWindow.ManagerSiteReport.dateEdit.date()
        EndDate = self.MainWindow.ManagerSiteReport.dateEdit_2.date()
        LowEventCountRange = self.MainWindow.ManagerSiteReport.lineEdit.text()
        HighEventCountRange = self.MainWindow.ManagerSiteReport.lineEdit_2.text()
        LowStaffCountRange = self.MainWindow.ManagerSiteReport.lineEdit_3.text()
        HightStaffCountRange = self.MainWindow.ManagerSiteReport.lineEdit_4.text()
        LowTotalVisitsRange = self.MainWindow.ManagerSiteReport.lineEdit_5.text()
        HighTotalVisitRange = self.MainWindow.ManagerSiteReport.lineEdit_6.text()
        LowTotalRevenueRange = self.MainWindow.ManagerSiteReport.lineEdit_7.text()
        HighTotalRevenueRange = self.MainWindow.ManagerSiteReport.lineEdit_8.text()

    def showManagerDailyDetail(self):
        self.MainWindow.close()
        self.MainWindow = MainWindow()
        self.MainWindow.startManagerDailyDetail()
        self.MainWindow.ManagerDailyDetail.pushButton.clicked.connect(self.showManagerSiteReport)
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


    def showStaffEventDetail(self):
        self.MainWindow.close()
        self.MainWindow = MainWindow()
        self.MainWindow.startStaffEventDetail()
        self.MainWindow.StaffEventDetail.pushButton.clicked.connect(self.showStaffViewSchedule)
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

    def filterVisitorEvents(self):
        Name = self.MainWindow.VisitorExploreEvent.lineEdit.text()
        DescriptionKeyword = self.MainWindow.VisitorExploreEvent.lineEdit_2.text()
        SiteName = self.MainWindow.VisitorExploreEvent.comboBox.currentText()
        StartDate = self.MainWindow.VisitorExploreEvent.dateEdit.date()
        EndDate = self.MainWindow.VisitorExploreEvent.dateEdit_2.date()
        IncludeVisited = self.MainWindow.VisitorExploreEvent.checkBox.isChecked()
        IncludeSoldOut = self.MainWindow.VisitorExploreEvent.checkBox_2.isChecked()
        LowTotalVisitRange = self.MainWindow.VisitorExploreEvent.lineEdit_5.text()
        HighTotalVisitRange = self.MainWindow.VisitorExploreEvent.lineEdit_6.text()
        LowTicketPriceRange = self.MainWindow.VisitorExploreEvent.lineEdit_7.text()
        HighTicketPriceRange = self.MainWindow.VisitorExploreEvent.lineEdit_8.text()

    def showVisitorEventDetail(self):
        self.MainWindow.close()
        self.MainWindow = MainWindow()
        self.MainWindow.startVisitorEventDetail()
        self.MainWindow.VisitorEventDetail.pushButton.clicked.connect(self.showVisitorExploreEvent)
        self.MainWindow.VisitorEventDetail.pushButton_2.clicked.connect(self.LogVisit)
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
        visitDate = self.MainWindow.VisitorEventDetail.dateEdit.date()

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

    def filterVisitorSites(self):
        Name = self.MainWindow.VisitorExploreSite.comboBox.currentText()
        OpenEveryday = self.MainWindow.VisitorExploreSite.comboBox_2.currentText()
        StartDate = self.MainWindow.VisitorExploreSite.dateEdit.date()
        EndDate = self.MainWindow.VisitorExploreSite.dateEdit_2.date()
        LowTotalVisitRange = self.MainWindow.VisitorExploreSite.lineEdit.text()
        HighTotalVisitRange = self.MainWindow.VisitorExploreSite.lineEdit_2.text()
        LowEventCount = self.MainWindow.VisitorExploreSite.lineEdit_3.text()
        HighEventCount = self.MainWindow.VisitorExploreSite.lineEdit_4.text()

    def showVisitorTransitDetail(self):
        self.MainWindow.close()
        self.MainWindow = MainWindow()
        self.MainWindow.startVisitorTransitDetail()
        self.MainWindow.VisitorTransitDetail.pushButton.clicked.connect(self.showVisitorExploreSite)
        self.MainWindow.VisitorTransitDetail.pushButton_2.clicked.connect(self.LogVisitorTransit)
        self.MainWindow.VisitorTransitDetail.comboBox.addItems(['All', 'MARTA', 'Bus', 'Bike'])
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

    def LogVisitorTransit(self):
        Site = self.MainWindow.VisitorTransitDetail.label_2.text()
        TransportType = self.MainWindow.VisitorTransitDetail.comboBox.currentText()
        TransitDate = self.MainWindow.VisitorTransitDetail.dateEdit.date()

    def showVisitorSiteDetail(self):
        self.MainWindow.close()
        self.MainWindow = MainWindow()
        self.MainWindow.startVisitorSiteDetail()
        self.MainWindow.VisitorSiteDetail.pushButton.clicked.connect(self.showVisitorExploreSite)
        self.MainWindow.VisitorSiteDetail.pushButton_2.clicked.connect(self.LogVisitorVisit)
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

    def FilterVisitorVisitHistory(self):
        Event = self.MainWindow.VisitorVisitHistory.lineEdit.text()
        StartDate = self.MainWindow.VisitorVisitHistory.dateEdit.date()
        EndDate = self.MainWindow.VisitorVisitHistory.dateEdit_2.date()
        Site = self.MainWindow.VisitorVisitHistory.comboxBox.currentText()



if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    c = Controller()
    c.showLogin()
    sys.exit(app.exec_())
