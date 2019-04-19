import pymysql.cursors
import base64

mydb = pymysql.connect(
  host="localhost",
  user="root",
  passwd="",
  database="company",
  cursorclass=pymysql.cursors.DictCursor
)


def Login(Email, Password):
    encrypted_password = str(base64.b64encode(Password.encode()))
    mycursor = mydb.cursor()
    mycursor.execute("Select * from department;")
    myresult = mycursor.fetchall()
    for result in myresult:
        return True
    return False

def RegisterUser(Fname, Lname, Username, Password, Emails):
    encrypted_password = str(base64.b64encode(Password.encode()))
    mycursor = mydb.cursor()
    for email in Emails:
        mycursor.execute("Insert into User")