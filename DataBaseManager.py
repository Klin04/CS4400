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
    # encrypted_password = str(base64.b64encode(Password.encode()))
    mycursor = mydb.cursor()
    mycursor.execute("Select * from users where username = %s and pass_word = %s", (Email, Password, ))
    myresult = mycursor.fetchone()
    if len(myresult) != 0:
        return myresult
    return None

def RegisterUser(Fname, Lname, Username, Password, Emails):
    encrypted_password = str(base64.b64encode(Password.encode()))
    mycursor = mydb.cursor()
    for email in Emails:
        mycursor.execute("Insert into User")