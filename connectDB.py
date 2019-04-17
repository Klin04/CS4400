import sys
import os
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Lkj!19990424",
    auth_plugin="mysql_native_password",
    database="ProjectDB"
)

def register(information):
    
