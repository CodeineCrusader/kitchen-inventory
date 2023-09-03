import atexit
import datetime
import mysql.connector
import customtkinter
from dotenv import load_dotenv
import os
import logging
import logging.handlers
from colorama import Fore, Back, Style
from pytz import timezone

load_dotenv()

ENV_dbHost = os.getenv('DB_HOST')
ENV_dbPort = os.getenv('DB_PORT')
ENV_dbUser = os.getenv('DB_USER')
ENV_dbDatabase = os.getenv('DB_DATABASE')
ENV_dbPassword = os.getenv('DB_PASSWORD')


class dbConnection:
    def __init__(self):
        self.db = mysql.connector.connect(user=ENV_dbUser,
                                          password=ENV_dbPassword,
                                          host=ENV_dbHost,
                                          database=ENV_dbDatabase,
                                          port=ENV_dbPort)
        self.cursor = self.db.cursor()
        self.closecursor = self.cursor.close()
        self.closedb = self.db.close()
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


def exit_handler():
    dbcursor.close()
    logging.info("Database Cursor Closed!")
    db.commit()
    logger.info("Unsaved Database Changes Committed!")
    db.close()
    logger.info("Database Closed!")
    logger.info("Program Exiting!")


atexit.register(exit_handler)

if __name__ == "__main__":
    logger = logging.getLogger()
    fh = logging.handlers.RotatingFileHandler('./logs/latest.log', maxBytes=10240, backupCount=5)
    fh.setLevel(logging.DEBUG)
    logformat = logging.Formatter("%(asctime)s | %(name)s | %(levelname)s | %(message)s",
                                  "%m/%d/%Y @ %H:%M:%S")
    fh.setFormatter(logformat)
    logger.addHandler(fh)

    try:
        global db
        db = mysql.connector.connect(user=ENV_dbUser,
                                     password=ENV_dbPassword,
                                     host=ENV_dbHost,
                                     database=ENV_dbDatabase,
                                     port=3306)
    except mysql.connector.errors.DatabaseError as e:
        logger.critical(
            f"An Exception Occured While Attempting a Connection with the Database. Please Ensure the Correct Information was Specified!\n{e}")
    except Exception as e:
        logger.error(e)
        print(e)
    else:
        logger.info("Database Connection Established!")
    global dbcursor
    dbcursor = db.cursor()

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