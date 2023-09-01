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

class dbConnection():
    def __init__(self):
        self.db = mysql.connector.connect(user=ENV_dbUser,
                                          password=ENV_dbPassword,
                                          host=ENV_dbUser,
                                          database=ENV_dbDatabase)
    # def dbQuerry(self):
    #     self.db.

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