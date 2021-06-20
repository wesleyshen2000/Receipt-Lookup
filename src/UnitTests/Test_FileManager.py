import unittest

from src.Constants.FileLocationConstants import FolderLocationConstants
from src.Data.FileManager import FileManager


class TestFileManager(unittest.TestCase):


    def test_createNewFolder(self):
        folderLocation = FolderLocationConstants()
        fileManager = FileManager()
        retVal = fileManager.create_folder(folderLocation.get_temp_folder())
        self.assertEqual(retVal, 1)

    def test_removeNewFolder(self):
        folderLocation = FolderLocationConstants()
        fileManager = FileManager()
        retVal = fileManager.delete_folder(folderLocation.get_temp_folder())
        self.assertEqual(retVal, 1)

    # def test_deleteFolder(self):






existFolder = unittest.TestSuite()
existFolder.addTest(TestFileManager('test_createNewFolder'))
existFolder.addTest(TestFileManager('test_removeNewFolder'))


runner = unittest.TextTestRunner()
runner.run(existFolder)

