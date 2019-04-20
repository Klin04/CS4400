import pymysql.cursors
import base64

mydb = pymysql.connect(
  host="localhost",
  user="root",
  passwd="Lkj!19990424",
  database="project3",
  cursorclass=pymysql.cursors.DictCursor
)

mycursor = mydb.cursor()

def Login(Email, Password):
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
    mycursor.execute("Select * from employees where username = %s", (Username, ))
    myresult = mycursor.fetchone()
    return myresult

def RegisterUser(Fname, Lname, Username, Password, Emails):
    arguments = (Username, Password, 'pending', Fname, Lname, 0, 0, )
    mycursor.execute("insert into users (username, pass_word, user_status, fname, lname, is_employee, is_visitor) values (%s, %s, %s, %s, %s, %d, %d)", arguments)
    for email in Emails:
        mycursor.execute("insert into emails(username, email) values (%s, $s)", (Username, email))

def RegisterVisitor(Fname, Lname, Username, Password, Emails):
    arguments = (Username, Password, 'pending', Fname, Lname, 0, 1, )
    mycursor.execute(
        "insert into users (username, pass_word, user_status, fname, lname, is_employee, is_visitor) values (%s, %s, %s, %s, %s, %d, %d)", arguments)
    for email in Emails:
        mycursor.execute("insert into emails(username, email) values (%s, $s)", (Username, email))

def RegisterEmployee(Fname, Lname, Username, Password, Emails, EmployeeId, Phone, Address, City, State, Zipcode, Erole):
    arguments = (Username, Password, 'pending', Fname, Lname, 1, 0,)
    mycursor.execute(
        "insert into users (username, pass_word, user_status, fname, lname, is_employee, is_visitor) values (%s, %s, %s, %s, %s, %d, %d)",
        arguments)
    for email in Emails:
        mycursor.execute("insert into emails(username, email) values (%s, $s)", (Username, email))
    arguments = (Username, EmployeeId, Phone, Address, City, State, Zipcode, Erole,)
    mycursor.execute("insert into `project`.`employee`(username, employee_id, phone, address, city, state, zipcode, erole) values (%s, %s, %d, %s, %s, %s, %d, $s)",
                     arguments)

def RegisterEmployeeVisitor(Fname, Lname, Username, Password, Emails, EmployeeId, Phone, Address, City, State, Zipcode, Erole):
    arguments = (Username, Password, 'pending', Fname, Lname, 1, 1,)
    mycursor.execute(
        "insert into users (username, pass_word, user_status, fname, lname, is_employee, is_visitor) values (%s, %s, %s, %s, %s, %d, %d)",
        arguments)
    for email in Emails:
        mycursor.execute("insert into emails(username, email) values (%s, $s)", (Username, email))
    arguments = (Username, EmployeeId, Phone, Address, City, State, Zipcode, Erole,)
    mycursor.execute("insert into `project`.`employee`(username, employee_id, phone, address, city, state, zipcode, erole) values (%s, %s, %d, %s, %s, %s, %d, $s)",
                     arguments)

def IsEmailUnique(email):
    mycursor.execute("select * from emails where email = %s", email)
    some_email = mycursor.fetchone()
    if some_email:
        return False
    else:
        return True

def IsPhoneUnique(phone):
    mycursor.execute("select * from employees where phone = %d", phone)
    any_phone = mycursor.fetchone()
    if any_phone:
        return False
    else:
        return True

def GetAllTransportTypeFromTransits():
    """
    For Screen 15/22 drop down menu for Transport Type
    :return: list of transport
    """
    mycursor.execute("select transit_type from transits")
    return mycursor.fetchall()

def GetAllSiteNameFromConnect():
    """
    For Screen 15/22 drop down menu for Contain Site
    :return: list
    """
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
    arguments = (zipcode, address, openeveryday, sitemanager_id, sitename, )
    mycursor.execute("UPDATE sites SET zipcode = %d, address = %s, openeveryday = %d, sitemanager_id = %d WHERE sitename = %s",
                     arguments)
    mycursor.execute("update sites set sitename = %s where sitename = %s", (new_sitename, sitename))