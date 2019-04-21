import pymysql.cursors
import base64

mydb = pymysql.connect(
  host="localhost",
  user="root",
  passwd="Lkj!19990424",
  database="project3",
  cursorclass=pymysql.cursors.DictCursor
)

def Login(Email, Password):
    with mydb as mycursor:
    # encrypted_password = str(base64.b64encode(Password.encode()))
        mycursor.execute("Select * from emails where email = %s",(Email, ))
        myResult = mycursor.fetchone()
        if not myResult:
            return None
        mycursor.execute("Select * from users where username = %s and pass_word = %s", (myResult['username'], Password, ))
        myFinalResult = mycursor.fetchone()
        if myFinalResult:
            return myFinalResult
        return None

def SearchEmployeeType(Username):
    with mydb as mycursor:
        mycursor.execute("Select * from employees where username = %s", (Username, ))
        myresult = mycursor.fetchone()
        return myresult

def RegisterUser(Fname, Lname, Username, Password, Emails):
    with mydb as mycursor:
        arguments = (Username, Password, 'pending', Fname, Lname, 0, 0, )
        mycursor.execute("insert into users (username, pass_word, user_status, fname, lname, is_employee, is_visitor) values (%s, %s, %s, %s, %s, %s, %s)", arguments)
        for email in Emails:
            print(mycursor.execute("insert into emails(username, email) values (%s, %s)", (Username, email)))

def RegisterVisitor(Fname, Lname, Username, Password, Emails):
    with mydb as mycursor:
        arguments = (Username, Password, 'pending', Fname, Lname, 0, 1, )
        mycursor.execute(
            "insert into users (username, pass_word, user_status, fname, lname, is_employee, is_visitor) values (%s, %s, %s, %s, %s, %s, %s)", arguments)
        for email in Emails:
            mycursor.execute("insert into emails(username, email) values (%s, %s)", (Username, email))

def RegisterEmployee(Fname, Lname, Username, Password, Emails, EmployeeId, Phone, Address, City, State, Zipcode, Erole):
    with mydb as mycursor:
        arguments = (Username, Password, 'pending', Fname, Lname, 1, 0,)
        mycursor.execute(
            "insert into users (username, pass_word, user_status, fname, lname, is_employee, is_visitor) values (%s, %s, %s, %s, %s, %s, %s)",
            arguments)
        for email in Emails:
            mycursor.execute("insert into emails(username, email) values (%s, %s)", (Username, email))
        arguments = (Username, EmployeeId, Phone, Address, City, State, Zipcode, Erole,)
        mycursor.execute("insert into employee(username, employee_id, phone, address, city, state, zipcode, erole) values (%s, %s, %s, %s, %s, %s, %s, %s)",
                         arguments)

def RegisterEmployeeVisitor(Fname, Lname, Username, Password, Emails, EmployeeId, Phone, Address, City, State, Zipcode, Erole):
    with mydb as mycursor:
        arguments = (Username, Password, 'pending', Fname, Lname, 1, 1,)
        mycursor.execute(
            "insert into users (username, pass_word, user_status, fname, lname, is_employee, is_visitor) values (%s, %s, %s, %s, %s, %s, %s)",
            arguments)
        for email in Emails:
            mycursor.execute("insert into emails(username, email) values (%s, %s)", (Username, email))
        arguments = (Username, EmployeeId, Phone, Address, City, State, Zipcode, Erole,)
        mycursor.execute("insert into employee(username, employee_id, phone, address, city, state, zipcode, erole) values (%s, %s, %s, %s, %s, %s, %s, %s)",
                         arguments)

def IsEmailUnique(email):
    with mydb as mycursor:
        mycursor.execute("select * from emails where email = %s", email)
        some_email = mycursor.fetchone()
        if some_email:
            return False
        else:
            return True

def IsPhoneUnique(phone):
    with mydb as mycursor:
        mycursor.execute("select * from employees where phone = %s", phone)
        any_phone = mycursor.fetchone()
        if any_phone:
            return False
        else:
            return True

def IsUsernameUnique(username):
    with mydb as mycursor:
        mycursor.execute("select * from users where username = %s", username)
        any_user = mycursor.fetchone()
        if any_user:
            return False
        else:
            return True

def IsEmployeeIdUnique(username):
    with mydb as mycursor:
        mycursor.execute("select * from employee where username = %s", username)
        any_user = mycursor.fetchone()
        if any_user:
            return False
        else:
            return True

def AddEmailForUsername(email, username):
    with mydb as mycursor:
        mycursor.execute("insert into emails(username, email) values (%s, %s)", (username, email))

def GetAllTransportTypeFromTransits():
    """
    For Screen 15/22 drop down menu for Transport Type
    :return: list of transport
    """
    with mydb as mycursor:
        mycursor.execute("select transit_type from transits")
        return mycursor.fetchall()

def GetAllSiteNameFromConnect():
    """
    For Screen 15/22 drop down menu for Contain Site
    :return: list
    """
    with mydb as mycursor:
        mycursor.execute("select connect_name from connect")
        return mycursor.fetchall()

def GetAllRoutesForTakeTransit(transit_type):
    """
    Filters all the routes for taking transits, for Screen 15
    :return: list of routes and their information
    """
    pass
    # mycursor.execute("select transit_route, transit_type, price from `project`.`transits` where transit_type = %s",
    #                  transit_type)
    # mycursor.fetchall()

    # finds the intersection of three lists
    # res_list = [i for n, i in enumerate(first_filter_result) if i in second_filter_result and i in third_filter_result]


def GetCurrentSiteManagerAndAllUnAssignedManagers(sitename):
    """
    For screen 20, shows a 'dropdown list containing the current site manager as well
    as the managers who have not yet been assigned to another site'
    :param sitename: the current site name
    :return:
    """
    with mydb as mycursor:
        mycursor.execute("(select username from employees where employee_id in (select sitemanager_id from sites where sitename = %s)) "
                         "union (select username from employees where employee_id not in (select sitemanager_id from sites))", sitename)
        return mycursor.fetchall()

def UpdateSiteInformation(sitename, zipcode, address, openeveryday, sitemanager_id, new_sitename):
    """
    Used for screen 20, edits the site information by administrator
    :param sitename:
    :param zipcode:
    :param address:
    :param openeveryday:
    :param sitemanager_id:
    :return:
    """
    with mydb as mycursor:
        arguments = (zipcode, address, openeveryday, sitemanager_id, sitename, )
        mycursor.execute("update sites SET zipcode = %s, address = %s, openeveryday = %s, sitemanager_id = %s WHERE sitename = %s",
                         arguments)
        mycursor.execute("update sites set sitename = %s where sitename = %s", (new_sitename, sitename))

def GetManagersNotAssignedSite():
    """
    For screen 21, where we need a drop down list of all the managers not assigned to a site
    :return: list
    """
    with mydb as mycursor:
        mycursor.execute("select username from employees where employee_id not in (select sitemanager_id from sites)")
        return mycursor.fetchall()

def UpdateUserInformation(username, fname, lname, is_visitor, phone, employee_id):
    with mydb as mycursor:
        mycursor.execute("update users set fname = %s, lname = %s, is_visitor = %s where username = %s", (fname, lname, is_visitor, username))
        mycursor.execute("update employee set phone = %s where employee_id = %s", (phone, employee_id))

def AddAllEmailsOfAUser(emails, username):
    with mydb as mycursor:
        for email in emails:
            mycursor.execute("insert into emails(username, email) values (%s, %s)", (username, email))

def RemoveAllEmailsOfAUser(username):
    with mydb as mycursor:
        mycursor.execute("delete from emails where username = %s)", username)

def AddNewSites(sitename, zipcode, address, openeveryday, sitemanager_id):
    """
    Adds a new site, note that if there is NO ADDRESS, please pass in None
    :param sitename:
    :param zipcode:
    :param address: None if no address is supplied
    :param openeveryday:
    :param sitemanager_id:
    :return:
    """
    with mydb as mycursor:
        mycursor.execute("insert into sites(sitename, zipcode, address, openeveryday, sitemanager_id) values (%s, %s, %s, %s, %s)")
