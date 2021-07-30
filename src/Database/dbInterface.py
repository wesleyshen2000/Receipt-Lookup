
class dbInterface:

    def get(self, upc: int) -> tuple:
        pass

    def insert(self, upc: int) -> bool:
        pass

    def remove(self,upc: int) -> bool:
        pass

    def columnType(self, colNames: str) -> any:
        pass

    def update(self,upc:int, columns: str, values: tuple) -> bool:
        """

        :param upc: UPC value of item
        :type upc: INT
        :param columns: SQL Column Values
        :type columns: Str
        :param values: Tuple of values to put in columns
        :type values: Any
        :return:
        :rtype:
        """
        pass

    def getAll(self) -> bool:
        pass


