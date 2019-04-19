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
    mycursor.execute("Select * from emails where Email = %s",(Email, ))
    myResult = mycursor.fetchone()
    if not myResult:
        return None
    mycursor.execute("Select * from users where username = %s and pass_word = %s", (myResult['username'], Password, ))
    myFinalResult = mycursor.fetchone()
    if not myFinalResult:
        return myFinalResult
    return None

def SearchEmployeeType(Username):
    mycursor.execute("Select * from employees where username = %s", (Username, ))
    myresult = mycursor.fetchone()
    return myresult

def Register(Fname):
    print()