import sys
import uuid
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
        self.VisitorSiteDetail.setupUi(self)
        self.show()


class Controller():
    def __init__(self):
        self.MainWindow = MainWindow()
        self.user = None
    
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
        if len(password) == 0:
            return QtWidgets.QMessageBox.warning(self.MainWindow, "Password not entered", "Password not entered", QtWidgets.QMessageBox.Ok)
        found = DataBaseManager.Login(email, password)
        if found:
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
        DataBaseManager.RegisterUser(Fname, Lname, Username, Password, Emails)
        self.showLogin()

    def showRegisterVisitorOnly(self):
        self.MainWindow.close()
        self.MainWindow = MainWindow()
        self.MainWindow.startRegisterVisitorOnly()
        self.MainWindow.RegisterVisitorOnlyPage.pushButton_2.clicked.connect(self.showRegisterNavigation)
        self.MainWindow.RegisterVisitorOnlyPage.pushButton_3.clicked.connect(self.RegisterVisitor)

    def RegisterVisitor(self):
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
        if not Phone.isdigit():
            return QtWidgets.QMessageBox.warning(self.MainWindow, "Phone not valid", "Please confirm your phone", QtWidgets.QMessageBox.Ok)
        if not Zipcode.isdigit():
            return QtWidgets.QMessageBox.warning(self.MainWindow, "Zipcode not valid", "Please confirm your zipcode", QtWidgets.QMessageBox.Ok)
        if not DataBaseManager.IsPhoneUnique(int(Phone)):
            return QtWidgets.QMessageBox.warning(self.MainWindow, "Phone already used", "Please use a new phone", QtWidgets.QMessageBox.Ok)
        DataBaseManager.RegisterEmployeeVisitor(Fname, Lname, Username, Password, uuid.uuid4(), int(Phone), Address, City, State, int(Zipcode), Erole)
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
        State = self.MainWindow.RegisterEmployeePage.comboBox_2.currentText()
        Erole = self.MainWindow.RegisterEmployeePage.comboBox.currentText()
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
        if not Phone.isdigit():
            return QtWidgets.QMessageBox.warning(self.MainWindow, "Phone not valid", "Please confirm your phone", QtWidgets.QMessageBox.Ok)
        if not DataBaseManager.IsPhoneUnique(int(Phone)):
            return QtWidgets.QMessageBox.warning(self.MainWindow, "Phone not valid", "Please confirm your phone", QtWidgets.QMessageBox.Ok)
        if not Zipcode.isdigit():
            return QtWidgets.QMessageBox.warning(self.MainWindow, "Zipcode not valid", "Please confirm your zipcode", QtWidgets.QMessageBox.Ok)
        DataBaseManager.RegisterEmployeeVisitor(Fname, Lname, Username, Password, Emails, uuid.uuid4(), int(Phone), Address, City, State, int(Zipcode), Erole)
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
        self.MainWindow.AdministratorFunctionality.pushButton_5.clicked.connect(self.showAdministratorManageSite)
        self.MainWindow.AdministratorFunctionality.pushButton_6.clicked.connect(self.showLogin)
        self.MainWindow.AdministratorFunctionality.pushButton_7.clicked.connect(self.showAdministratorEditSite)

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
        self.MainWindow.UserTakeTransit.pushButton.clicked.connect(self.filterTransit())
        self.MainWindow.UserTakeTransit.comboBox_2.addItems(["All", "MARTA", "Bus", "Bike"])
        self.MainWindow.UserTakeTransit.comboBox.addItems(allSites)

    def filterTransit(self):
        containSite = self.MainWindow.UserTakeTransit.comboBox.currentText()
        transportType = self.MainWindow.UserTakeTransit.comboBox_2.currentText()
        LowRange = self.MainWindow.UserTakeTransit.lineEdit.text()
        HighRange = self.MainWindow.UserTakeTransit.lineEdit.text()
        TransitDate = self.MainWindow.UserTakeTransit.dateEdit.date()
        if not LowRange.isdecimal() or not HighRange.isdecimal():
            return QtWidgets.QMessageBox.warning(self.MainWindow, "Range not valid", "You could only enter digits", QtWidgets.QMessageBox.Ok)


    def showUserTransitHistory(self):
        self.MainWindow.close()
        self.MainWindow = MainWindow()
        self.MainWindow.startUserTakeTransit()
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
        self.MainWindow.UserTransitHistory.comboBox.addItems(allSites)
        self.MainWindow.UserTransitHistory.comboBox_2.addItems(["All", "MARTA", "Bus", "Bike"])
        self.MainWindow.UserTransitHistory.pushButton.clicked.connect(self.filterTransitHistory)

    def filterTransitHistory(self):
        containSite = self.MainWindow.UserTransitHistory.comboBox.currentText()
        transportType = self.MainWindow.UserTransitHistory.comboBox_2.currentText()
        startDate = self.MainWindow.UserTransitHistory.dateEdit.date()
        endDate = self.MainWindow.UserTransitHistory.dateEdit.date()
        Route = self.MainWindow.UserTransitHistory.lineEdit.text()

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

    def updateEmployeeProfile(self):
        Fname = self.MainWindow.EmployeeManageProfile.lineEdit.text()
        Lname = self.MainWindow.EmployeeManageProfile.lineEdit_2.text()
        Phone = self.MainWindow.EmployeeManageProfile.lineEdit_3.text()
        Emails = []
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
            self.MainWindow.AdministratorManagerUser.pushButton_4.clicked.connect(self.showAdministratorFunctionality)
        elif self.user == 'StaffVisitor':
            self.MainWindow.AdministratorManagerUser.pushButton_4.clicked.connect(self.showStaffVisitorFunctionality)
        elif self.user == 'ManagerVisitor':
            self.MainWindow.AdministratorManagerUser.pushButton_4.clicked.connect(self.showManagerVisitorFunctionality)
        elif self.user == 'AdministratorVisitor':
            self.MainWindow.AdministratorManagerUser.pushButton_4.clicked.connect(self.showAdminVisitorFunctionality)
        elif self.user == 'Visitor':
            self.MainWindow.AdministratorManagerUser.pushButton_4.clicked.connect(self.showVisitorFunctionality)
        self.MainWindow.AdministratorManageUser.comboBox_2.addItems(["Approved", "Pending", "Declined", "All"])
        self.MainWindow.AdministratorManageUser.comboBox.addItems("All", "Manager", "User", "Visitor", "Staff")
        self.MainWindow.AdministratorManageUser.pushButton.clicked.connect(self.filterUsers)
        self.MainWindow.AdministratorManageUser.pushButton_2.clicked.connect(self.approveUsers)
        self.MainWindow.AdministratorManageUser.pushButton_3.clicked.connect(self.declineUsers)

    def filterUsers(self):
        Username = self.MainWindow.AdministratorManageUser.lineEdit.text()
        Type = self.MainWindow.AdministratorManageUser.comboBox.currentText()
        Status = self.MainWindow.AdministratorManageUser.comboBox_2.currentText()

    # Todo in backend
    def approveUsers(self):
        print("Approved")

    def declineUsers(self):
        print("Declined")

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
        self.MainWindow.AdministratorManageSite.comboBox.addItems(allSites)
        allManagers = ['All']
        self.MainWindow.AdministratorManageSite.comboBox_2.addItems(allManagers)
        self.MainWindow.AdministratorManageSite.comboBox_3.addItems(["Yes", "No"])
        self.MainWindow.AdministratorManageSite.pushButton_2.clicked.connect(self.showAdministratorCreateSite())
        self.MainWindow.AdministratorManageSite.pushButton_3.clicked.connect(self.showAdministratorEditSite())
        self.MainWindow.AdministratorManageSite.pushButton_4.clicked.connect(self.deleteSite)

    def filterSites(self):
        Site = self.MainWindow.AdministratorManageSite.comboBox.currentText()
        Manager = self.MainWindow.AdministratorManageSite.comboBox_2.currentText()
        OpenEveryday = self.MainWindow.AdministratorManageSite.comboBox_3.currentText()

    def deleteSites(self):
        print("Delete a site")

    def showAdministratorEditSite(self):
        self.MainWindow.close()
        self.MainWindow = MainWindow()
        self.MainWindow.startAdministratorEditSite()
        self.MainWindow.AdministratorEditSite.pushButton.clicked.connect(self.showAdministratorManageSite)
        self.MainWindow.AdministratorEditSite.pushButton_2.clicked.connect(self.editSite)
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
        print("update a site")

    def showAdministratorCreateSite(self):
        self.MainWindow.close()
        self.MainWindow = MainWindow()
        self.MainWindow.startAdministratorCreateSite()
        self.MainWindow.AdministratorCreateSite.pushButton.clicked.connect(self.showAdministratorManageSite)
        self.MainWindow.AdministratorCreateSite.pushButton_2.clicked.connect(self.createSite)
        allManagers = []
        self.MainWindow.AdministratorCreateSite.comboBox.addItems(allManagers)
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
        Manager = self.MainWindow.AdministratorCreateSite.comboBox.currentText()
        openEveryday = self.MainWindow.AdministratorCreateSite.checkBox.isChecked()

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
        self.MainWindow.AdministratorManageTransit.comboBox_2.addItems(allSites)
        self.MainWindow.AdministratorManageTransit.pushButton.clicked.connect(self.filterTransit)
        self.MainWindow.AdministratorManageTransit.pushButton_2.clicked.connect(self.showAdministratorCreateTransit)
        self.MainWindow.AdministratorManageTransit.pushButton_3.clicked.connect(self.showAdministratorEditTransit)
        self.MainWindow.AdministratorManageTransit.pushButton_4.clicked.connect(self.deleteTransit)

    def deleteTransit(self):
        print("Deleted")

    def filterTransit(self):
        TransportType = self.MainWindow.AdministratorManageTransit.comboBox.currentText()
        Route = self.MainWindow.AdministratorManageTransit.lineEdit.text()
        LowRange = self.MainWindow.AdministratorManageTransit.lineEdit_2.text()
        HighRange = self.MainWindow.AdministratorManageTransit.lineEdit_3.text()


    def showAdministratorEditTransit(self):
        self.MainWindow.close()
        self.MainWindow = MainWindow()
        self.MainWindow.startAdministratorEditTransit()
        self.MainWindow.AdministratorEditTransit.pushButton.clicked.connect(self.showAdministratorManageTransit)
        self.MainWindow.AdministratorEditTransit.pushButton_2.clicked.connect(self.updateTransit)
        allSites = []
        self.MainWindow.AdministratorEditTransit.listWidget.addItems(allSites)
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

    def updateTransit(self):
        Route = self.MainWindow.AdministratorEditTransit.lineEdit.text()
        Price = self.MainWindow.AdministratorEditTransit.lineEdit_2.text()

    def showAdministratorCreateTransit(self):
        self.MainWindow.close()
        self.MainWindow = MainWindow()
        self.MainWindow.startAdministratorCreateTransit()
        self.MainWindow.AdministratorCreateTransit.pushButton_5.clicked.connect(self.showAdministratorManageTransit)
        self.MainWindow.AdministratorCreateTransit.pushButton_6.clicked.connect(self.createTransit)
        allSites = []
        self.MainWindow.AdministratorCreateTransit.listWidget.addItems(allSites)
        self.MainWindow.AdministratorCreateTransit.comboBox.addItems(["All", "MARTA", "Bus", "Bike"])
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
        self.MainWindow.ManagerManageEvent.pushButton.clicked.connect(self.filterEvents)
        self.MainWindow.ManagerManageEvent.pushButton_2.clicked.connect(self.showManagerCreateEvent)
        self.MainWindow.ManagerManageEvent.pushButton_3.clicked.connect(self.showManagerViewEditEvent)
        self.MainWindow.ManagerManageEvent.pushButton_4.clicked.connect(self.deleteEvent)

    def filterEvents(self):
        print("filter events")

    def deleteEvent(self):
        print("deleted")

    def showManagerViewEditEvent(self):
        self.MainWindow.close()
        self.MainWindow = MainWindow()
        self.MainWindow.startManagerViewEditEvent()
        if self.user == 'User':
            self.MainWindow.ManagerViewEditEvent.pushButton_3.clicked.connect(self.showUserFunctionality)
        elif self.user == "Staff":
            self.MainWindow.ManagerViewEditEvent.pushButton_3.clicked.connect(self.showStaffFunctionality)
        elif self.user == 'Manager':
            self.MainWindow.ManagerViewEditEvent.pushButton_3.clicked.connect(self.showManagerFunctionality)
        elif self.user == 'Administrator':
            self.MainWindow.ManagerViewEditEvent.pushButton_3.clicked.connect(self.showAdministratorFunctionality)
        elif self.user == 'StaffVisitor':
            self.MainWindow.ManagerViewEditEvent.pushButton_3.clicked.connect(self.showStaffVisitorFunctionality)
        elif self.user == 'ManagerVisitor':
            self.MainWindow.ManagerViewEditEvent.pushButton_3.clicked.connect(self.showManagerVisitorFunctionality)
        elif self.user == 'AdministratorVisitor':
            self.MainWindow.ManagerViewEditEvent.pushButton_3.clicked.connect(self.showAdminVisitorFunctionality)
        elif self.user == 'Visitor':
            self.MainWindow.ManagerViewEditEvent.pushButton_3.clicked.connect(self.showVisitorFunctionality)
        

    def showManagerCreateEvent(self):
        self.MainWindow.close()
        self.MainWindow = MainWindow()
        self.MainWindow.startManagerCreateEvent()
        if self.user == 'User':
            self.MainWindow.ManagerCreateEvent.pushButton.clicked.connect(self.showUserFunctionality)
        elif self.user == "Staff":
            self.MainWindow.ManagerCreateEvent.pushButton.clicked.connect(self.showStaffFunctionality)
        elif self.user == 'Manager':
            self.MainWindow.ManagerCreateEvent.pushButton.clicked.connect(self.showManagerFunctionality)
        elif self.user == 'Administrator':
            self.MainWindow.ManagerCreateEvent.pushButton.clicked.connect(self.showAdministratorFunctionality)
        elif self.user == 'StaffVisitor':
            self.MainWindow.ManagerCreateEvent.pushButton.clicked.connect(self.showStaffVisitorFunctionality)
        elif self.user == 'ManagerVisitor':
            self.MainWindow.ManagerCreateEvent.pushButton.clicked.connect(self.showManagerVisitorFunctionality)
        elif self.user == 'AdministratorVisitor':
            self.MainWindow.ManagerCreateEvent.pushButton.clicked.connect(self.showAdminVisitorFunctionality)
        elif self.user == 'Visitor':
            self.MainWindow.ManagerCreateEvent.pushButton.clicked.connect(self.showVisitorFunctionality)

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


    def showManagerDailyDetail(self):
        self.MainWindow.close()
        self.MainWindow = MainWindow()
        self.MainWindow.startManagerDailyDetail()
        if self.user == 'User':
            self.MainWindow.ManagerDailyDetail.pushButton.clicked.connect(self.showUserFunctionality)
        elif self.user == "Staff":
            self.MainWindow.ManagerDailyDetail.pushButton.clicked.connect(self.showStaffFunctionality)
        elif self.user == 'Manager':
            self.MainWindow.ManagerDailyDetail.pushButton.clicked.connect(self.showManagerFunctionality)
        elif self.user == 'Administrator':
            self.MainWindow.ManagerDailyDetail.pushButton.clicked.connect(self.showAdministratorFunctionality)
        elif self.user == 'StaffVisitor':
            self.MainWindow.ManagerDailyDetail.pushButton.clicked.connect(self.showStaffVisitorFunctionality)
        elif self.user == 'ManagerVisitor':
            self.MainWindow.ManagerDailyDetail.pushButton.clicked.connect(self.showManagerVisitorFunctionality)
        elif self.user == 'AdministratorVisitor':
            self.MainWindow.ManagerDailyDetail.pushButton.clicked.connect(self.showAdminVisitorFunctionality)
        elif self.user == 'Visitor':
            self.MainWindow.ManagerDailyDetail.pushButton.clicked.connect(self.showVisitorFunctionality)

    def showStaffViewSchedule(self):
        self.MainWindow.close()
        self.MainWindow = MainWindow()
        self.MainWindow.startStaffViewSchedule()
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
        if self.user == 'User':
            self.MainWindow.StaffEventDetail.pushButton.clicked.connect(self.showUserFunctionality)
        elif self.user == "Staff":
            self.MainWindow.StaffEventDetail.pushButton.clicked.connect(self.showStaffFunctionality)
        elif self.user == 'Manager':
            self.MainWindow.StaffEventDetail.pushButton.clicked.connect(self.showManagerFunctionality)
        elif self.user == 'Administrator':
            self.MainWindow.StaffEventDetail.pushButton.clicked.connect(self.showAdministratorFunctionality)
        elif self.user == 'StaffVisitor':
            self.MainWindow.StaffEventDetail.pushButton.clicked.connect(self.showStaffVisitorFunctionality)
        elif self.user == 'ManagerVisitor':
            self.MainWindow.StaffEventDetail.pushButton.clicked.connect(self.showManagerVisitorFunctionality)
        elif self.user == 'AdministratorVisitor':
            self.MainWindow.StaffEventDetail.pushButton.clicked.connect(self.showAdminVisitorFunctionality)
        elif self.user == 'Visitor':
            self.MainWindow.StaffEventDetail.pushButton.clicked.connect(self.showVisitorFunctionality)

    def showVisitorExploreEvent(self):
        self.MainWindow.close()
        self.MainWindow = MainWindow()
        self.MainWindow.startVisitorExploreEvent()
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

    def showVisitorEventDetail(self):
        self.MainWindow.close()
        self.MainWindow = MainWindow()
        self.MainWindow.startVisitorEventDetail()
        if self.user == 'User':
            self.MainWindow.VisitorEventDetail.pushButton.clicked.connect(self.showUserFunctionality)
        elif self.user == "Staff":
            self.MainWindow.VisitorEventDetail.pushButton.clicked.connect(self.showStaffFunctionality)
        elif self.user == 'Manager':
            self.MainWindow.VisitorEventDetail.pushButton.clicked.connect(self.showManagerFunctionality)
        elif self.user == 'Administrator':
            self.MainWindow.VisitorEventDetail.pushButton.clicked.connect(self.showAdministratorFunctionality)
        elif self.user == 'StaffVisitor':
            self.MainWindow.VisitorEventDetail.pushButton.clicked.connect(self.showStaffVisitorFunctionality)
        elif self.user == 'ManagerVisitor':
            self.MainWindow.VisitorEventDetail.pushButton.clicked.connect(self.showManagerVisitorFunctionality)
        elif self.user == 'AdministratorVisitor':
            self.MainWindow.VisitorEventDetail.pushButton.clicked.connect(self.showAdminVisitorFunctionality)
        elif self.user == 'Visitor':
            self.MainWindow.VisitorEventDetail.pushButton.clicked.connect(self.showVisitorFunctionality)

    def showVisitorExploreSite(self):
        self.MainWindow.close()
        self.MainWindow = MainWindow()
        self.MainWindow.startVisitorExploreSite()
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

    def showVisitorTransitDetail(self):
        self.MainWindow.close()
        self.MainWindow = MainWindow()
        self.MainWindow.startVisitorTransitDetail()
        if self.user == 'User':
            self.MainWindow.VisitorTransitDetail.pushButton.clicked.connect(self.showUserFunctionality)
        elif self.user == "Staff":
            self.MainWindow.VisitorTransitDetail.pushButton.clicked.connect(self.showStaffFunctionality)
        elif self.user == 'Manager':
            self.MainWindow.VisitorTransitDetail.pushButton.clicked.connect(self.showManagerFunctionality)
        elif self.user == 'Administrator':
            self.MainWindow.VisitorTransitDetail.pushButton.clicked.connect(self.showAdministratorFunctionality)
        elif self.user == 'StaffVisitor':
            self.MainWindow.VisitorTransitDetail.pushButton.clicked.connect(self.showStaffVisitorFunctionality)
        elif self.user == 'ManagerVisitor':
            self.MainWindow.VisitorTransitDetail.pushButton.clicked.connect(self.showManagerVisitorFunctionality)
        elif self.user == 'AdministratorVisitor':
            self.MainWindow.VisitorTransitDetail.pushButton.clicked.connect(self.showAdminVisitorFunctionality)
        elif self.user == 'Visitor':
            self.MainWindow.VisitorTransitDetail.pushButton.clicked.connect(self.showVisitorFunctionality)

    def showVisitorSiteDetail(self):
        self.MainWindow.close()
        self.MainWindow = MainWindow()
        self.MainWindow.startVisitorSiteDetail()
        if self.user == 'User':
            self.MainWindow.VisitorSiteDetail.pushButton.clicked.connect(self.showUserFunctionality)
        elif self.user == "Staff":
            self.MainWindow.VisitorSiteDetail.pushButton.clicked.connect(self.showStaffFunctionality)
        elif self.user == 'Manager':
            self.MainWindow.VisitorSiteDetail.pushButton.clicked.connect(self.showManagerFunctionality)
        elif self.user == 'Administrator':
            self.MainWindow.VisitorSiteDetail.pushButton.clicked.connect(self.showAdministratorFunctionality)
        elif self.user == 'StaffVisitor':
            self.MainWindow.VisitorSiteDetail.pushButton.clicked.connect(self.showStaffVisitorFunctionality)
        elif self.user == 'ManagerVisitor':
            self.MainWindow.VisitorSiteDetail.pushButton.clicked.connect(self.showManagerVisitorFunctionality)
        elif self.user == 'AdministratorVisitor':
            self.MainWindow.VisitorSiteDetail.pushButton.clicked.connect(self.showAdminVisitorFunctionality)
        elif self.user == 'Visitor':
            self.MainWindow.VisitorSiteDetail.pushButton.clicked.connect(self.showVisitorFunctionality)

    def showVisitorVisitHistory(self):
        self.MainWindow.close()
        self.MainWindow = MainWindow()
        self.MainWindow.startVisitorVisitHistory()
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


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    c = Controller()
    c.showLogin()
    sys.exit(app.exec_())
