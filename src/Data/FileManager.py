import os
import shutil
from src.Abs.AbsFileManager import InterfaceFileManager

class FileManager(InterfaceFileManager):
    """
    Manages files and directories
    """

    def create_folder(self,path: str ) -> int:
        try:
            os.mkdir(path)
            print("Running")
            return 1
        except FileExistsError:
            print("Cannot create file that already exists")
            return 0

    def delete_folder(self,path):
        try:
            shutil.rmtree(path)
            return 1
        except Exception as e:
            print("Error deleteing Exception" + str(e))
            return 0
    def file_exist(self,path):
        if os.path.exists(path):
            return True
        return False
#f = FileManager()
#f.create_folder("../../tmp")
#f.delete_folder("../../tmp/")

