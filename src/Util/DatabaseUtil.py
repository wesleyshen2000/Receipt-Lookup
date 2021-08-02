import mysql.connector


class DatabaseUtil():

    #TODO: Turn this function into dictionary?
    @staticmethod
    def convertTupleToSqlString(columns:str, columnTypes: str, values:str, conjunction:str) -> str:
        """
        Converts column and value into sql string (INCLUDE SPACES IF NEEDED)
        (Price,Name),(1.2,Test)," and " = Price=1.2 and Name="Test"
        Args:
            columns (str[]): Name of Columns
            columnTypes (str[]): Column Types
            values (str[]): Values to insert into column
            conjunction (str): Separator between each key:value

        Returns: sql string to be appended to original string

        """
        sql = ""
        for i in range(0, len(columnTypes)):
            sql += columns[i] + "="
            if columnTypes != None and 'char' in columnTypes[i]:
                sql += f"\'{values[i]}\'"
            else:
                sql += f"{values[i]}"

            if (len(columns) != 1 and i != (len(columns) - 1)):
                sql += f"{conjunction}"

        return sql

    @staticmethod
    def getColumnType(mydb: mysql.connector, table:str, colNames: str) -> any:
        """
        :param colNames: Array of Column Names
        :type colNames: String
        :return: Column Types
        :rtype: String[]
        """
        try:
            types = []
            cursor = mydb.cursor()
            for col in colNames:

                sqlStatement = f"SELECT DATA_TYPE FROM INFORMATION_SCHEMA.COLUMNS WHERE table_name = \'{table}\' AND COLUMN_NAME = \'{col}\'"
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