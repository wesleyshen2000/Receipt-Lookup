# Create connection to database and execute queries
import sys

import mysql.connector

from src.Util.ConfigUtil import ConfigUtil
from src.Database.dbInterface import dbInterface
from src.Constants.DatabaseConstants import DatabaseConstants

class itemDAO(dbInterface):

    def __init__(self, table):
        super().__init__()
        param = self.read_config_file()
        self.table = table
        self.mydb = mysql.connector.connect(user=param['user'], password=param['password'],
                                            host=param['host'], database='Walmart')



    def read_config_file(self):
        param = {}
        try:

            with open('../../config/sqlLogin.txt', 'r') as f:
                for line in f:
                    if line[0] != '#':
                        key, val = ConfigUtil.getValue(line)
                        param[key] = val
        except OSError:
            print("Could not find sqlLogin config file")
            sys.exit()

        return param

    #TODO: Sanitize Statements
    def insert(self, upc):
        try:

            cursor = self.mydb.cursor()
            sqlStatement = f"INSERT IGNORE INTO {self.table} (UPC) VALUES ({upc})"
            cursor.execute(sqlStatement)
            self.mydb.commit()
            cursor.close()
        except mysql.connector.Error as err:
            print("Error with insert statement: ", err)

    def get(self, upc):
        try:

            cursor = self.mydb.cursor()
            sqlStatement = f"SELECT * FROM {self.table} WHERE UPC={upc}"
            cursor.execute(sqlStatement)
            results = cursor.fetchall()
            cursor.close()
            return results
        except mysql.connector.Error as err:
            print("Error Getting UPC:" + upc +" with error " , err)

    def getAll(self):
        try:

            cursor = self.mydb.cursor()
            sqlStatement = f"SELECT * FROM {self.table}"
            cursor.execute(sqlStatement)
            results = cursor.fetchall()
            self.mydb.commit()
            cursor.close()
            return results
        except mysql.connector.Error as err:
            print("Error Fetching All: ", err)

    def remove(self,upc):
        try:

            cursor = self.mydb.cursor()
            sqlStatement = f"DELETE FROM {self.table} WHERE UPC={upc}"
            cursor.execute(sqlStatement)
            self.mydb.commit()
            cursor.close()
        except mysql.connector.Error as err:
            print("Error with removing upc: ", err)


sql = itemDAO(DatabaseConstants.getItemTableName())
sql.insert(1)
sql.insert(2)
sql.insert(3)
sql.remove(3)
print(sql.getAll())