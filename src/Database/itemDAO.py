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

    def convertTupleToSqlString(self, columns, values, conjunction) -> str:
        """
        Convert Tuples of Columns and Values into valid sql statement
        """
        sql = ""
        # TODO: Add quotes to ints
        columnTypes = self.columnType(columns)
        for i in range(0, len(columnTypes)):
            sql += columns[i] + "="
            if columnTypes != None and 'char' in columnTypes[i]:
                sql += f"\'{values[i]}\'"
            else:
                sql += f"{values[i]}"

            if (len(columns) != 1 and i != (len(columns) - 1)):
                sql += f"{conjunction}"

        return sql

    def update(self, upc: int, columns: str, values: tuple) -> bool:
        try:
            cursor = self.mydb.cursor()
            sqlStatement = f"UPDATE {self.table} SET "
            sqlStatement += self.convertTupleToSqlString(columns, values, ',')
            sqlStatement += f" WHERE UPC={upc}"
            cursor.execute(sqlStatement)
            self.mydb.commit()
            cursor.close()
        except mysql.connector.Error as err:
            print("Error updating UPC: ", upc, " error: ", err)
            return False

    def columnType(self, colNames: str) -> any:
        """
        :param colNames: Array of Column Names
        :type colNames: String
        :return: Column Types
        :rtype: String[]
        """
        try:
            types = []
            cursor = self.mydb.cursor()
            for col in colNames:

                sqlStatement = f"SELECT DATA_TYPE FROM INFORMATION_SCHEMA.COLUMNS WHERE table_name = \'{self.table}\' AND COLUMN_NAME = \'{col}\'"
                cursor.execute(sqlStatement)
                result = cursor.fetchone()

                if result is not None:
                    types.append(result[0])
                else:
                    print(f"Error in identifying column in function columnType {col}. Please check your columns are accurate")
            return types
        except mysql.connector.Error as err:
            print("Error in identifying columnType: ", err)
            return None


sql = itemDAO(DatabaseConstants.getItemTableName())
sql.insert(1)
sql.insert(2)
sql.insert(3)
sql.remove(3)
sql.update(1,["Price"], ["3", "Test Name1", "Test Desc"])
