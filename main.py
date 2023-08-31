import mysql.connector
import customtkinter

DBuser = None
DBhost = None
DBdatabase = None
DBpassword = None

db = mysql.connector.connect(user=DBuser, password=DBpassword,
                              host=DBhost,
                              database=DBdatabase)
db.close()