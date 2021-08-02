
class dbInterface:

    def get(self, upc: int) -> tuple:
        """
        Gets the row with the UPC
        """
        pass

    def insert(self, upc: int) -> bool:
        """
        Inserts ONLY UPC into the table
        """
        pass

    def remove(self,upc: int) -> bool:
        """
        Removes the row with the UPC
        """
        pass

    def update(self,upc:int, columns: list, values: list) -> bool:
        """
        Creates the following sample sql statement:
        UPDATE <Table> SET <COLUMN>=<Values> WHERE UPC=<UPC>;
        @param upc: Item UPC value
        @type upc: INT
        @param columns: SQL Column Values
        @type columns: list
        @param values: List of Values to put in columns
        @type values: list
        @return: True: Success & False: Failure
        @rtype: Bool
        """
        pass

    def removeAll(self) -> bool:
        """
        Removes all entries in table
        Returns: Boolean | True: Success , False: Fail
        """
        pass

    def getAll(self) -> bool:
        """
        Gets everything from the table
        @return: True: Success False: False
        @rtype: bool
        """
        pass

    def close(self) -> bool:
        """
        Close SQL connection
        @return: True: Success False: Failed
        @rtype: bool
        """
        pass

