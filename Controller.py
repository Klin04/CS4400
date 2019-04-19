import sys
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
        found = DataBaseManager.Login(email, password)
        if found:
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

    def showRegisterVisitorOnly(self):
        self.MainWindow.close()
        self.MainWindow = MainWindow()
        self.MainWindow.startRegisterVisitorOnly()
        self.MainWindow.RegisterVisitorOnlyPage.pushButton_2.clicked.connect(self.showRegisterNavigation)

    def showRegisterEmployee(self):
        self.MainWindow.close()
        self.MainWindow = MainWindow()
        self.MainWindow.startRegisterEmployee()
        self.MainWindow.RegisterEmployeePage.pushButton_2.clicked.connect(self.showRegisterNavigation)

    def showRegisterEmployeeVisitor(self):
        self.MainWindow.close()
        self.MainWindow = MainWindow()
        self.MainWindow.startRegisterEmployeeVisitor()
        self.MainWindow.RegisterEmployeeVisitorPage.pushButton_2.clicked.connect(self.showRegisterNavigation)

    def showRegisterVisitorOnly(self):
        self.MainWindow.close()
        self.MainWindow = MainWindow()
        self.MainWindow.startRegisterVisitorOnly()
        self.MainWindow.RegisterVisitorOnlyPage.pushButton_2.clicked.connect(self.showRegisterNavigation)

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
        self.MainWindow.AdministratorFunctionality.pushButton.clicked.connect(self.showEmployeeManageProfil)
        self.MainWindow.AdministratorFunctionality.pushButton_2.clicked.connect(self.showUserTakeTransit)
        self.MainWindow.AdministratorFunctionality.pushButton_3.clicked.connect(self.showAdministratorManagerUser)
        self.MainWindow.AdministratorFunctionality.pushButton_4.clicked.connect(self.showUserTransitHistory)
        self.MainWindow.AdministratorFunctionality.pushButton_5.clicked.connect(self.showAdministratorMangerSite)
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
            self.MainWindow.UserFunctionality.pushButton_2.clicked.connect(self.showUserFunctionality)
        elif self.user == "Staff":
            self.MainWindow.UserFunctionality.pushButton_2.clicked.connect(self.showStaffFunctionality)
        elif self.user == 'Manager':
            self.MainWindow.UserFunctionality.pushButton_2.clicked.connect(self.showManagerFunctionality)
        elif self.user == 'Administrator':
            self.MainWindow.UserFunctionality.pushButton_2.clicked.connect(self.showAdministratorFunctionality)
        elif self.user == 'StaffVisitor':
            self.MainWindow.UserFunctionality.pushButton_2.clicked.connect(self.showStaffVisitorFunctionality)
        elif self.user == 'ManagerVisitor':
            self.MainWindow.UserFunctionality.pushButton_2.clicked.connect(self.showManagerVisitorFunctionality)
        elif self.user == 'AdministratorVisitor':
            self.MainWindow.UserFunctionality.pushButton_2.clicked.connect(self.showAdminVisitorFunctionality)
        elif self.user == 'Visitor':
            self.MainWindow.UserFunctionality.pushButton_2.clicked.connect(self.showVisitorFunctionality)

    def showUserTransitHistory(self):
        self.MainWindow.close()
        self.MainWindow = MainWindow()
        self.MainWindow.startUserTakeTransit()
        if self.user == 'User':
            self.MainWindow.UserFunctionality.pushButton_2.clicked.connect(self.showUserFunctionality)
        elif self.user == "Staff":
            self.MainWindow.UserFunctionality.pushButton_2.clicked.connect(self.showStaffFunctionality)
        elif self.user == 'Manager':
            self.MainWindow.UserFunctionality.pushButton_2.clicked.connect(self.showManagerFunctionality)
        elif self.user == 'Administrator':
            self.MainWindow.UserFunctionality.pushButton_2.clicked.connect(self.showAdministratorFunctionality)
        elif self.user == 'StaffVisitor':
            self.MainWindow.UserFunctionality.pushButton_2.clicked.connect(self.showStaffVisitorFunctionality)
        elif self.user == 'ManagerVisitor':
            self.MainWindow.UserFunctionality.pushButton_2.clicked.connect(self.showManagerVisitorFunctionality)
        elif self.user == 'AdministratorVisitor':
            self.MainWindow.UserFunctionality.pushButton_2.clicked.connect(self.showAdminVisitorFunctionality)
        elif self.user == 'Visitor':
            self.MainWindow.UserFunctionality.pushButton_2.clicked.connect(self.showVisitorFunctionality)

    def showEmployeeManageProfile(self):
        self.MainWindow.close()
        self.MainWindow = MainWindow()
        self.MainWindow.startEmployeeManageProfile()
        if self.user == 'User':
            self.MainWindow.UserFunctionality.pushButton_3.clicked.connect(self.showUserFunctionality)
        elif self.user == "Staff":
            self.MainWindow.UserFunctionality.pushButton_3.clicked.connect(self.showStaffFunctionality)
        elif self.user == 'Manager':
            self.MainWindow.UserFunctionality.pushButton_3.clicked.connect(self.showManagerFunctionality)
        elif self.user == 'Administrator':
            self.MainWindow.UserFunctionality.pushButton_3.clicked.connect(self.showAdministratorFunctionality)
        elif self.user == 'StaffVisitor':
            self.MainWindow.UserFunctionality.pushButton_3.clicked.connect(self.showStaffVisitorFunctionality)
        elif self.user == 'ManagerVisitor':
            self.MainWindow.UserFunctionality.pushButton_3.clicked.connect(self.showManagerVisitorFunctionality)
        elif self.user == 'AdministratorVisitor':
            self.MainWindow.UserFunctionality.pushButton_3.clicked.connect(self.showAdminVisitorFunctionality)
        elif self.user == 'Visitor':
            self.MainWindow.UserFunctionality.pushButton_3.clicked.connect(self.showVisitorFunctionality)


    def showAdministratorManagerUser(self):
        self.MainWindow.close()
        self.MainWindow = MainWindow()
        self.MainWindow.startAdministratorManagerUser()
        if self.user == 'User':
            self.MainWindow.UserFunctionality.pushButton_4.clicked.connect(self.showUserFunctionality)
        elif self.user == "Staff":
            self.MainWindow.UserFunctionality.pushButton_4.clicked.connect(self.showStaffFunctionality)
        elif self.user == 'Manager':
            self.MainWindow.UserFunctionality.pushButton_4.clicked.connect(self.showManagerFunctionality)
        elif self.user == 'Administrator':
            self.MainWindow.UserFunctionality.pushButton_4.clicked.connect(self.showAdministratorFunctionality)
        elif self.user == 'StaffVisitor':
            self.MainWindow.UserFunctionality.pushButton_4.clicked.connect(self.showStaffVisitorFunctionality)
        elif self.user == 'ManagerVisitor':
            self.MainWindow.UserFunctionality.pushButton_4.clicked.connect(self.showManagerVisitorFunctionality)
        elif self.user == 'AdministratorVisitor':
            self.MainWindow.UserFunctionality.pushButton_4.clicked.connect(self.showAdminVisitorFunctionality)
        elif self.user == 'Visitor':
            self.MainWindow.UserFunctionality.pushButton_4.clicked.connect(self.showVisitorFunctionality)

    def showAdministratorManageSite(self):
        self.MainWindow.close()
        self.MainWindow = MainWindow()
        self.MainWindow.startAdministratorManageSite()
        if self.user == 'User':
            self.MainWindow.UserFunctionality.pushButton_5.clicked.connect(self.showUserFunctionality)
        elif self.user == "Staff":
            self.MainWindow.UserFunctionality.pushButton_5.clicked.connect(self.showStaffFunctionality)
        elif self.user == 'Manager':
            self.MainWindow.UserFunctionality.pushButton_5.clicked.connect(self.showManagerFunctionality)
        elif self.user == 'Administrator':
            self.MainWindow.UserFunctionality.pushButton_5.clicked.connect(self.showAdministratorFunctionality)
        elif self.user == 'StaffVisitor':
            self.MainWindow.UserFunctionality.pushButton_5.clicked.connect(self.showStaffVisitorFunctionality)
        elif self.user == 'ManagerVisitor':
            self.MainWindow.UserFunctionality.pushButton_5.clicked.connect(self.showManagerVisitorFunctionality)
        elif self.user == 'AdministratorVisitor':
            self.MainWindow.UserFunctionality.pushButton_5.clicked.connect(self.showAdminVisitorFunctionality)
        elif self.user == 'Visitor':
            self.MainWindow.UserFunctionality.pushButton_5.clicked.connect(self.showVisitorFunctionality)

    def showAdministratorEditSite(self):
        self.MainWindow.close()
        self.MainWindow = MainWindow()
        self.MainWindow.startAdministratorEditSite()
        if self.user == 'User':
            self.MainWindow.UserFunctionality.pushButton.clicked.connect(self.showUserFunctionality)
        elif self.user == "Staff":
            self.MainWindow.UserFunctionality.pushButton.clicked.connect(self.showStaffFunctionality)
        elif self.user == 'Manager':
            self.MainWindow.UserFunctionality.pushButton.clicked.connect(self.showManagerFunctionality)
        elif self.user == 'Administrator':
            self.MainWindow.UserFunctionality.pushButton.clicked.connect(self.showAdministratorFunctionality)
        elif self.user == 'StaffVisitor':
            self.MainWindow.UserFunctionality.pushButton.clicked.connect(self.showStaffVisitorFunctionality)
        elif self.user == 'ManagerVisitor':
            self.MainWindow.UserFunctionality.pushButton.clicked.connect(self.showManagerVisitorFunctionality)
        elif self.user == 'AdministratorVisitor':
            self.MainWindow.UserFunctionality.pushButton.clicked.connect(self.showAdminVisitorFunctionality)
        elif self.user == 'Visitor':
            self.MainWindow.UserFunctionality.pushButton.clicked.connect(self.showVisitorFunctionality)

    def showAdministratorCreateSite(self):
        self.MainWindow.close()
        self.MainWindow = MainWindow()
        self.MainWindow.startAdministratorCreateSite()
        if self.user == 'User':
            self.MainWindow.UserFunctionality.pushButton.clicked.connect(self.showUserFunctionality)
        elif self.user == "Staff":
            self.MainWindow.UserFunctionality.pushButton.clicked.connect(self.showStaffFunctionality)
        elif self.user == 'Manager':
            self.MainWindow.UserFunctionality.pushButton.clicked.connect(self.showManagerFunctionality)
        elif self.user == 'Administrator':
            self.MainWindow.UserFunctionality.pushButton.clicked.connect(self.showAdministratorFunctionality)
        elif self.user == 'StaffVisitor':
            self.MainWindow.UserFunctionality.pushButton.clicked.connect(self.showStaffVisitorFunctionality)
        elif self.user == 'ManagerVisitor':
            self.MainWindow.UserFunctionality.pushButton.clicked.connect(self.showManagerVisitorFunctionality)
        elif self.user == 'AdministratorVisitor':
            self.MainWindow.UserFunctionality.pushButton.clicked.connect(self.showAdminVisitorFunctionality)
        elif self.user == 'Visitor':
            self.MainWindow.UserFunctionality.pushButton.clicked.connect(self.showVisitorFunctionality)

    def showAdministratorManageTransit(self):
        self.MainWindow.close()
        self.MainWindow = MainWindow()
        self.MainWindow.startAdministratorManageTransit()
        if self.user == 'User':
            self.MainWindow.UserFunctionality.pushButton_5.clicked.connect(self.showUserFunctionality)
        elif self.user == "Staff":
            self.MainWindow.UserFunctionality.pushButton_5.clicked.connect(self.showStaffFunctionality)
        elif self.user == 'Manager':
            self.MainWindow.UserFunctionality.pushButton_5.clicked.connect(self.showManagerFunctionality)
        elif self.user == 'Administrator':
            self.MainWindow.UserFunctionality.pushButton_5.clicked.connect(self.showAdministratorFunctionality)
        elif self.user == 'StaffVisitor':
            self.MainWindow.UserFunctionality.pushButton_5.clicked.connect(self.showStaffVisitorFunctionality)
        elif self.user == 'ManagerVisitor':
            self.MainWindow.UserFunctionality.pushButton_5.clicked.connect(self.showManagerVisitorFunctionality)
        elif self.user == 'AdministratorVisitor':
            self.MainWindow.UserFunctionality.pushButton_5.clicked.connect(self.showAdminVisitorFunctionality)
        elif self.user == 'Visitor':
            self.MainWindow.UserFunctionality.pushButton_5.clicked.connect(self.showVisitorFunctionality)

    def showAdministratorEditTransit(self):
        self.MainWindow.close()
        self.MainWindow = MainWindow()
        self.MainWindow.startAdministratorEditTransit()
        if self.user == 'User':
            self.MainWindow.UserFunctionality.pushButton.clicked.connect(self.showUserFunctionality)
        elif self.user == "Staff":
            self.MainWindow.UserFunctionality.pushButton.clicked.connect(self.showStaffFunctionality)
        elif self.user == 'Manager':
            self.MainWindow.UserFunctionality.pushButton.clicked.connect(self.showManagerFunctionality)
        elif self.user == 'Administrator':
            self.MainWindow.UserFunctionality.pushButton.clicked.connect(self.showAdministratorFunctionality)
        elif self.user == 'StaffVisitor':
            self.MainWindow.UserFunctionality.pushButton.clicked.connect(self.showStaffVisitorFunctionality)
        elif self.user == 'ManagerVisitor':
            self.MainWindow.UserFunctionality.pushButton.clicked.connect(self.showManagerVisitorFunctionality)
        elif self.user == 'AdministratorVisitor':
            self.MainWindow.UserFunctionality.pushButton.clicked.connect(self.showAdminVisitorFunctionality)
        elif self.user == 'Visitor':
            self.MainWindow.UserFunctionality.pushButton.clicked.connect(self.showVisitorFunctionality)


    def showAdministratorCreateTransit(self):
        self.MainWindow.close()
        self.MainWindow = MainWindow()
        self.MainWindow.startAdministratorCreateTransit()
        if self.user == 'User':
            self.MainWindow.UserFunctionality.pushButton_5.clicked.connect(self.showUserFunctionality)
        elif self.user == "Staff":
            self.MainWindow.UserFunctionality.pushButton_5.clicked.connect(self.showStaffFunctionality)
        elif self.user == 'Manager':
            self.MainWindow.UserFunctionality.pushButton_5.clicked.connect(self.showManagerFunctionality)
        elif self.user == 'Administrator':
            self.MainWindow.UserFunctionality.pushButton_5.clicked.connect(self.showAdministratorFunctionality)
        elif self.user == 'StaffVisitor':
            self.MainWindow.UserFunctionality.pushButton_5.clicked.connect(self.showStaffVisitorFunctionality)
        elif self.user == 'ManagerVisitor':
            self.MainWindow.UserFunctionality.pushButton_5.clicked.connect(self.showManagerVisitorFunctionality)
        elif self.user == 'AdministratorVisitor':
            self.MainWindow.UserFunctionality.pushButton_5.clicked.connect(self.showAdminVisitorFunctionality)
        elif self.user == 'Visitor':
            self.MainWindow.UserFunctionality.pushButton_5.clicked.connect(self.showVisitorFunctionality)

    def showManagerManageEvent(self):
        self.MainWindow.close()
        self.MainWindow = MainWindow()
        self.MainWindow.startManagerManageEvent()
        if self.user == 'User':
            self.MainWindow.UserFunctionality.pushButton_5.clicked.connect(self.showUserFunctionality)
        elif self.user == "Staff":
            self.MainWindow.UserFunctionality.pushButton_5.clicked.connect(self.showStaffFunctionality)
        elif self.user == 'Manager':
            self.MainWindow.UserFunctionality.pushButton_5.clicked.connect(self.showManagerFunctionality)
        elif self.user == 'Administrator':
            self.MainWindow.UserFunctionality.pushButton_5.clicked.connect(self.showAdministratorFunctionality)
        elif self.user == 'StaffVisitor':
            self.MainWindow.UserFunctionality.pushButton_5.clicked.connect(self.showStaffVisitorFunctionality)
        elif self.user == 'ManagerVisitor':
            self.MainWindow.UserFunctionality.pushButton_5.clicked.connect(self.showManagerVisitorFunctionality)
        elif self.user == 'AdministratorVisitor':
            self.MainWindow.UserFunctionality.pushButton_5.clicked.connect(self.showAdminVisitorFunctionality)
        elif self.user == 'Visitor':
            self.MainWindow.UserFunctionality.pushButton_5.clicked.connect(self.showVisitorFunctionality)

    def showManagerViewEditEvent(self):
        self.MainWindow.close()
        self.MainWindow = MainWindow()
        self.MainWindow.startManagerViewEditEvent()
        if self.user == 'User':
            self.MainWindow.UserFunctionality.pushButton_3.clicked.connect(self.showUserFunctionality)
        elif self.user == "Staff":
            self.MainWindow.UserFunctionality.pushButton_3.clicked.connect(self.showStaffFunctionality)
        elif self.user == 'Manager':
            self.MainWindow.UserFunctionality.pushButton_3.clicked.connect(self.showManagerFunctionality)
        elif self.user == 'Administrator':
            self.MainWindow.UserFunctionality.pushButton_3.clicked.connect(self.showAdministratorFunctionality)
        elif self.user == 'StaffVisitor':
            self.MainWindow.UserFunctionality.pushButton_3.clicked.connect(self.showStaffVisitorFunctionality)
        elif self.user == 'ManagerVisitor':
            self.MainWindow.UserFunctionality.pushButton_3.clicked.connect(self.showManagerVisitorFunctionality)
        elif self.user == 'AdministratorVisitor':
            self.MainWindow.UserFunctionality.pushButton_3.clicked.connect(self.showAdminVisitorFunctionality)
        elif self.user == 'Visitor':
            self.MainWindow.UserFunctionality.pushButton_3.clicked.connect(self.showVisitorFunctionality)

    def showManagerCreateEvent(self):
        self.MainWindow.close()
        self.MainWindow = MainWindow()
        self.MainWindow.startManagerCreateEvent()
        if self.user == 'User':
            self.MainWindow.UserFunctionality.pushButton.clicked.connect(self.showUserFunctionality)
        elif self.user == "Staff":
            self.MainWindow.UserFunctionality.pushButton.clicked.connect(self.showStaffFunctionality)
        elif self.user == 'Manager':
            self.MainWindow.UserFunctionality.pushButton.clicked.connect(self.showManagerFunctionality)
        elif self.user == 'Administrator':
            self.MainWindow.UserFunctionality.pushButton.clicked.connect(self.showAdministratorFunctionality)
        elif self.user == 'StaffVisitor':
            self.MainWindow.UserFunctionality.pushButton.clicked.connect(self.showStaffVisitorFunctionality)
        elif self.user == 'ManagerVisitor':
            self.MainWindow.UserFunctionality.pushButton.clicked.connect(self.showManagerVisitorFunctionality)
        elif self.user == 'AdministratorVisitor':
            self.MainWindow.UserFunctionality.pushButton.clicked.connect(self.showAdminVisitorFunctionality)
        elif self.user == 'Visitor':
            self.MainWindow.UserFunctionality.pushButton.clicked.connect(self.showVisitorFunctionality)

    def showManagerManageStaff(self):
        self.MainWindow.close()
        self.MainWindow = MainWindow()
        self.MainWindow.startManagerManageStaff()
        if self.user == 'User':
            self.MainWindow.UserFunctionality.pushButton_2.clicked.connect(self.showUserFunctionality)
        elif self.user == "Staff":
            self.MainWindow.UserFunctionality.pushButton_2.clicked.connect(self.showStaffFunctionality)
        elif self.user == 'Manager':
            self.MainWindow.UserFunctionality.pushButton_2.clicked.connect(self.showManagerFunctionality)
        elif self.user == 'Administrator':
            self.MainWindow.UserFunctionality.pushButton_2.clicked.connect(self.showAdministratorFunctionality)
        elif self.user == 'StaffVisitor':
            self.MainWindow.UserFunctionality.pushButton_2.clicked.connect(self.showStaffVisitorFunctionality)
        elif self.user == 'ManagerVisitor':
            self.MainWindow.UserFunctionality.pushButton_2.clicked.connect(self.showManagerVisitorFunctionality)
        elif self.user == 'AdministratorVisitor':
            self.MainWindow.UserFunctionality.pushButton_2.clicked.connect(self.showAdminVisitorFunctionality)
        elif self.user == 'Visitor':
            self.MainWindow.UserFunctionality.pushButton_2.clicked.connect(self.showVisitorFunctionality)

    def showManagerSiteReport(self):
        self.MainWindow.close()
        self.MainWindow = MainWindow()
        self.MainWindow.startManagerSiteReport()
        if self.user == 'User':
            self.MainWindow.UserFunctionality.pushButton_3.clicked.connect(self.showUserFunctionality)
        elif self.user == "Staff":
            self.MainWindow.UserFunctionality.pushButton_3.clicked.connect(self.showStaffFunctionality)
        elif self.user == 'Manager':
            self.MainWindow.UserFunctionality.pushButton_3.clicked.connect(self.showManagerFunctionality)
        elif self.user == 'Administrator':
            self.MainWindow.UserFunctionality.pushButton_3.clicked.connect(self.showAdministratorFunctionality)
        elif self.user == 'StaffVisitor':
            self.MainWindow.UserFunctionality.pushButton_3.clicked.connect(self.showStaffVisitorFunctionality)
        elif self.user == 'ManagerVisitor':
            self.MainWindow.UserFunctionality.pushButton_3.clicked.connect(self.showManagerVisitorFunctionality)
        elif self.user == 'AdministratorVisitor':
            self.MainWindow.UserFunctionality.pushButton_3.clicked.connect(self.showAdminVisitorFunctionality)
        elif self.user == 'Visitor':
            self.MainWindow.UserFunctionality.pushButton_3.clicked.connect(self.showVisitorFunctionality)


    def showManagerDailyDetail(self):
        self.MainWindow.close()
        self.MainWindow = MainWindow()
        self.MainWindow.startManagerDailyDetail()
        if self.user == 'User':
            self.MainWindow.UserFunctionality.pushButton.clicked.connect(self.showUserFunctionality)
        elif self.user == "Staff":
            self.MainWindow.UserFunctionality.pushButton.clicked.connect(self.showStaffFunctionality)
        elif self.user == 'Manager':
            self.MainWindow.UserFunctionality.pushButton.clicked.connect(self.showManagerFunctionality)
        elif self.user == 'Administrator':
            self.MainWindow.UserFunctionality.pushButton.clicked.connect(self.showAdministratorFunctionality)
        elif self.user == 'StaffVisitor':
            self.MainWindow.UserFunctionality.pushButton.clicked.connect(self.showStaffVisitorFunctionality)
        elif self.user == 'ManagerVisitor':
            self.MainWindow.UserFunctionality.pushButton.clicked.connect(self.showManagerVisitorFunctionality)
        elif self.user == 'AdministratorVisitor':
            self.MainWindow.UserFunctionality.pushButton.clicked.connect(self.showAdminVisitorFunctionality)
        elif self.user == 'Visitor':
            self.MainWindow.UserFunctionality.pushButton.clicked.connect(self.showVisitorFunctionality)

    def showStaffViewSchedule(self):
        self.MainWindow.close()
        self.MainWindow = MainWindow()
        self.MainWindow.startStaffViewSchedule()
        if self.user == 'User':
            self.MainWindow.UserFunctionality.pushButton_3.clicked.connect(self.showUserFunctionality)
        elif self.user == "Staff":
            self.MainWindow.UserFunctionality.pushButton_3.clicked.connect(self.showStaffFunctionality)
        elif self.user == 'Manager':
            self.MainWindow.UserFunctionality.pushButton_3.clicked.connect(self.showManagerFunctionality)
        elif self.user == 'Administrator':
            self.MainWindow.UserFunctionality.pushButton_3.clicked.connect(self.showAdministratorFunctionality)
        elif self.user == 'StaffVisitor':
            self.MainWindow.UserFunctionality.pushButton_3.clicked.connect(self.showStaffVisitorFunctionality)
        elif self.user == 'ManagerVisitor':
            self.MainWindow.UserFunctionality.pushButton_3.clicked.connect(self.showManagerVisitorFunctionality)
        elif self.user == 'AdministratorVisitor':
            self.MainWindow.UserFunctionality.pushButton_3.clicked.connect(self.showAdminVisitorFunctionality)
        elif self.user == 'Visitor':
            self.MainWindow.UserFunctionality.pushButton_3.clicked.connect(self.showVisitorFunctionality)


    def showStaffEventDetail(self):
        self.MainWindow.close()
        self.MainWindow = MainWindow()
        self.MainWindow.startStaffEventDetail()
        if self.user == 'User':
            self.MainWindow.UserFunctionality.pushButton.clicked.connect(self.showUserFunctionality)
        elif self.user == "Staff":
            self.MainWindow.UserFunctionality.pushButton.clicked.connect(self.showStaffFunctionality)
        elif self.user == 'Manager':
            self.MainWindow.UserFunctionality.pushButton.clicked.connect(self.showManagerFunctionality)
        elif self.user == 'Administrator':
            self.MainWindow.UserFunctionality.pushButton.clicked.connect(self.showAdministratorFunctionality)
        elif self.user == 'StaffVisitor':
            self.MainWindow.UserFunctionality.pushButton.clicked.connect(self.showStaffVisitorFunctionality)
        elif self.user == 'ManagerVisitor':
            self.MainWindow.UserFunctionality.pushButton.clicked.connect(self.showManagerVisitorFunctionality)
        elif self.user == 'AdministratorVisitor':
            self.MainWindow.UserFunctionality.pushButton.clicked.connect(self.showAdminVisitorFunctionality)
        elif self.user == 'Visitor':
            self.MainWindow.UserFunctionality.pushButton.clicked.connect(self.showVisitorFunctionality)

    def showVisitorExploreEvent(self):
        self.MainWindow.close()
        self.MainWindow = MainWindow()
        self.MainWindow.startVisitorExploreEvent()
        if self.user == 'User':
            self.MainWindow.UserFunctionality.pushButton_3.clicked.connect(self.showUserFunctionality)
        elif self.user == "Staff":
            self.MainWindow.UserFunctionality.pushButton_3.clicked.connect(self.showStaffFunctionality)
        elif self.user == 'Manager':
            self.MainWindow.UserFunctionality.pushButton_3.clicked.connect(self.showManagerFunctionality)
        elif self.user == 'Administrator':
            self.MainWindow.UserFunctionality.pushButton_3.clicked.connect(self.showAdministratorFunctionality)
        elif self.user == 'StaffVisitor':
            self.MainWindow.UserFunctionality.pushButton_3.clicked.connect(self.showStaffVisitorFunctionality)
        elif self.user == 'ManagerVisitor':
            self.MainWindow.UserFunctionality.pushButton_3.clicked.connect(self.showManagerVisitorFunctionality)
        elif self.user == 'AdministratorVisitor':
            self.MainWindow.UserFunctionality.pushButton_3.clicked.connect(self.showAdminVisitorFunctionality)
        elif self.user == 'Visitor':
            self.MainWindow.UserFunctionality.pushButton_3.clicked.connect(self.showVisitorFunctionality)

    def showVisitorEventDetail(self):
        self.MainWindow.close()
        self.MainWindow = MainWindow()
        self.MainWindow.startVisitorEventDetail()
        if self.user == 'User':
            self.MainWindow.UserFunctionality.pushButton.clicked.connect(self.showUserFunctionality)
        elif self.user == "Staff":
            self.MainWindow.UserFunctionality.pushButton.clicked.connect(self.showStaffFunctionality)
        elif self.user == 'Manager':
            self.MainWindow.UserFunctionality.pushButton.clicked.connect(self.showManagerFunctionality)
        elif self.user == 'Administrator':
            self.MainWindow.UserFunctionality.pushButton.clicked.connect(self.showAdministratorFunctionality)
        elif self.user == 'StaffVisitor':
            self.MainWindow.UserFunctionality.pushButton.clicked.connect(self.showStaffVisitorFunctionality)
        elif self.user == 'ManagerVisitor':
            self.MainWindow.UserFunctionality.pushButton.clicked.connect(self.showManagerVisitorFunctionality)
        elif self.user == 'AdministratorVisitor':
            self.MainWindow.UserFunctionality.pushButton.clicked.connect(self.showAdminVisitorFunctionality)
        elif self.user == 'Visitor':
            self.MainWindow.UserFunctionality.pushButton.clicked.connect(self.showVisitorFunctionality)

    def showVisitorExploreSite(self):
        self.MainWindow.close()
        self.MainWindow = MainWindow()
        self.MainWindow.startVisitorExploreSite()
        if self.user == 'User':
            self.MainWindow.UserFunctionality.pushButton_4.clicked.connect(self.showUserFunctionality)
        elif self.user == "Staff":
            self.MainWindow.UserFunctionality.pushButton_4.clicked.connect(self.showStaffFunctionality)
        elif self.user == 'Manager':
            self.MainWindow.UserFunctionality.pushButton_4.clicked.connect(self.showManagerFunctionality)
        elif self.user == 'Administrator':
            self.MainWindow.UserFunctionality.pushButton_4.clicked.connect(self.showAdministratorFunctionality)
        elif self.user == 'StaffVisitor':
            self.MainWindow.UserFunctionality.pushButton_4.clicked.connect(self.showStaffVisitorFunctionality)
        elif self.user == 'ManagerVisitor':
            self.MainWindow.UserFunctionality.pushButton_4.clicked.connect(self.showManagerVisitorFunctionality)
        elif self.user == 'AdministratorVisitor':
            self.MainWindow.UserFunctionality.pushButton_4.clicked.connect(self.showAdminVisitorFunctionality)
        elif self.user == 'Visitor':
            self.MainWindow.UserFunctionality.pushButton_4.clicked.connect(self.showVisitorFunctionality)

    def showVisitorTransitDetail(self):
        self.MainWindow.close()
        self.MainWindow = MainWindow()
        self.MainWindow.startVisitorTransitDetail()
        if self.user == 'User':
            self.MainWindow.UserFunctionality.pushButton.clicked.connect(self.showUserFunctionality)
        elif self.user == "Staff":
            self.MainWindow.UserFunctionality.pushButton.clicked.connect(self.showStaffFunctionality)
        elif self.user == 'Manager':
            self.MainWindow.UserFunctionality.pushButton.clicked.connect(self.showManagerFunctionality)
        elif self.user == 'Administrator':
            self.MainWindow.UserFunctionality.pushButton.clicked.connect(self.showAdministratorFunctionality)
        elif self.user == 'StaffVisitor':
            self.MainWindow.UserFunctionality.pushButton.clicked.connect(self.showStaffVisitorFunctionality)
        elif self.user == 'ManagerVisitor':
            self.MainWindow.UserFunctionality.pushButton.clicked.connect(self.showManagerVisitorFunctionality)
        elif self.user == 'AdministratorVisitor':
            self.MainWindow.UserFunctionality.pushButton.clicked.connect(self.showAdminVisitorFunctionality)
        elif self.user == 'Visitor':
            self.MainWindow.UserFunctionality.pushButton.clicked.connect(self.showVisitorFunctionality)

    def showVisitorSiteDetail(self):
        self.MainWindow.close()
        self.MainWindow = MainWindow()
        self.MainWindow.startVisitorSiteDetail()
        if self.user == 'User':
            self.MainWindow.UserFunctionality.pushButton.clicked.connect(self.showUserFunctionality)
        elif self.user == "Staff":
            self.MainWindow.UserFunctionality.pushButton.clicked.connect(self.showStaffFunctionality)
        elif self.user == 'Manager':
            self.MainWindow.UserFunctionality.pushButton.clicked.connect(self.showManagerFunctionality)
        elif self.user == 'Administrator':
            self.MainWindow.UserFunctionality.pushButton.clicked.connect(self.showAdministratorFunctionality)
        elif self.user == 'StaffVisitor':
            self.MainWindow.UserFunctionality.pushButton.clicked.connect(self.showStaffVisitorFunctionality)
        elif self.user == 'ManagerVisitor':
            self.MainWindow.UserFunctionality.pushButton.clicked.connect(self.showManagerVisitorFunctionality)
        elif self.user == 'AdministratorVisitor':
            self.MainWindow.UserFunctionality.pushButton.clicked.connect(self.showAdminVisitorFunctionality)
        elif self.user == 'Visitor':
            self.MainWindow.UserFunctionality.pushButton.clicked.connect(self.showVisitorFunctionality)

    def showVisitorVisitHistory(self):
        self.MainWindow.close()
        self.MainWindow = MainWindow()
        self.MainWindow.startVisitorVisitHistory()
        

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    c = Controller()
    c.showLogin()
    sys.exit(app.exec_())
