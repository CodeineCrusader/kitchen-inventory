import atexit
import datetime
import mysql.connector
import customtkinter
from dotenv import load_dotenv
import os
import logging

load_dotenv()

ENV_dbHost = os.getenv('DB_HOST')
ENV_dbUser = os.getenv('DB_USER')
ENV_dbDatabase = os.getenv('DB_DATABASE')
ENV_dbPassword = os.getenv('DB_PASSWORD')

db = mysql.connector.connect(user=ENV_dbUser,
                                  password=ENV_dbPassword,
                                  host=ENV_dbUser,
                                  database=ENV_dbDatabase)
dbcursor = db.cursor()

class dbConnection():
    # def __init__(self):
    #     self.db = mysql.connector.connect(user=ENV_dbUser,
    #                                       password=ENV_dbPassword,
    #                                       host=ENV_dbUser,
    #                                       database=ENV_dbDatabase)
    #     self.cursor = self.db.cursor()
        # self.closecursor = self.cursor.close()
        # self.closedb = self.db.close()
    def dbAddItem(self, table: str, itemName: str, itemExpiration: datetime.datetime, itemNutritionalValue: dict):
        addItemQuerry = (f"INSERT INTO {table}"
                          "(id, itemName, itemExpiration, itemNutritionalValues)"
                          "VALUES %(id)s %(itemName)s %(itemExpiration)s %(itemNutritionalValues)s")
        id = dbcursor.lastrowid
        addItemData = {
            'id': id,
            'itemName': itemName,
            'itemExpiration': itemExpiration,
            'itemNuritionalValue': itemNutritionalValue
        }
        dbcursor.execute(addItemQuerry, addItemData)

        db.commit()
        # self.cursor.close()
        # self.db.close()

def exit_handler():
    dbcursor.close()
    print("Database Cursor Closed!")
    db.commit()
    print("Unsaved Database Changes Committed!")
    db.close()
    print("Database Closed!")
    print("Program Exiting!")

atexit.register(exit_handler)
if __name__ == "__main__":
    while True:
        item = input("What Item Do You Want to Input? ")

        redo = None
        while redo not in ["y", "Y", "n", "N"]:
            redo = input("Redo? [Y/n]: ")
        else:
            if redo.upper() == "Y":
                pass
            else:
                exit()