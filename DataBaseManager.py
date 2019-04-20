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

def IsEmailUnique(email):
    mycursor.execute("select * from emails where email = %s", email)
    some_email = mycursor.fetchone()
    if some_email:
        return False
    else:
        return True

def IsPhoneUnique(phone):
    mycursor.execute("select * from employees where phone = %s", phone)
    any_phone = mycursor.fetchone()
    if any_phone:
        return False
    else:
        return True