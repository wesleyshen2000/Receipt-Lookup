import os
from src.Abs.AbsFileManager import InterfaceFileManager

class FileManager(InterfaceFileManager):
    """
    Manages files and directories
    """

    def create_folder(self,path):
        try:
            os.mkdir(path)
        except FileExistsError:
            print("File Already Exists")

    def delete_folder(self,path):
        os.rmdir(path)

    def file_exist(self,path):
        if os.path.exists(path):
            return True
        return False
#f = FileManager()
#f.create_folder("../../tmp")
#f.delete_folder("../../tmp/")

