from src.Database.absDatabase import absDatabase
from src.Constants.DatabaseConstants import DatabaseConstants
class itemDAO(absDatabase):
    def __init__(self):
        super().__init__(DatabaseConstants.getItemTableName())

# sql = itemDAO()
# print("Status is" , sql.insert(10))
# print("Update is: " , sql.update(10,["Price","Name"],["99","Test Item"]))