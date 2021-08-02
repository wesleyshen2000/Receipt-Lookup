# Create connection to database and execute queries
import sys

import mysql.connector

from src.Util.ConfigUtil import ConfigUtil
from src.Database.dbInterface import dbInterface

from src.Util.DatabaseUtil import DatabaseUtil

class absDatabase(dbInterface):

    def __init__(self, table):
        super().__init__()
        param = self.read_config_file()
        self.table = table
        self.mydb = mysql.connector.connect(user=param['user'], password=param['password'],
                                            host=param['host'], database='Walmart')
        print("Connection created")

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

    # TODO: Sanitize Statements
    def insert(self, upc: int) -> bool:
        try:

            cursor = self.mydb.cursor()
            sqlStatement = f"INSERT IGNORE INTO {self.table} (UPC) VALUES ({upc})"
            cursor.execute(sqlStatement)
            self.mydb.commit()
            cursor.close()
            return True
        except mysql.connector.Error as err:
            print("Error with insert statement: ", err)
            return False

    def get(self, upc: int) -> tuple:
        try:
            cursor = self.mydb.cursor()
            sqlStatement = f"SELECT * FROM {self.table} WHERE UPC={upc}"
            cursor.execute(sqlStatement)
            results = cursor.fetchall()
            cursor.close()
            return results
        except mysql.connector.Error as err:
            print("Error Getting UPC:" + str(upc) + " with error ", err)
            return ()

    def getAll(self) -> bool:
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
            return False

    def remove(self, upc: int) -> bool:
        try:

            cursor = self.mydb.cursor()
            sqlStatement = f"DELETE FROM {self.table} WHERE UPC={upc}"
            cursor.execute(sqlStatement)
            self.mydb.commit()
            cursor.close()
            return True
        except mysql.connector.Error as err:
            print("Error with removing upc: ", err)
            return False

    # noinspection PyTypeChecker
    def update(self,upc:int, columns: list, values: list) -> bool:
        try:
            cursor = self.mydb.cursor()
            columnTypes = DatabaseUtil.getColumnType(self.mydb,self.table,columns)
            sqlStatement = f"UPDATE {self.table} SET "
            sqlStatement += DatabaseUtil.convertTupleToSqlString(columns, columnTypes,values, ',')
            sqlStatement += f" WHERE UPC={upc}"
            cursor.execute(sqlStatement)
            self.mydb.commit()
            cursor.close()
            return True
        except mysql.connector.Error as err:
            print("Error updating UPC: ", upc, " error: ", err)
            return False

    def close(self) -> bool:
        try:
            print("Successfully closed connection")
            self.mydb.close()
            return True

        except mysql.connector.Error as err:
            print("Error closing sql connection")
            return False

