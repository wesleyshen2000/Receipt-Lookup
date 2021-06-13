import unittest
from src.Data.FileManager import FileManager
class TestFileManager(unittest.TestCase):

    def test_create_folder(self):
        FileManager tmp

        self.assertEqual("FOO","FOO")

if __name__ == '__main__':
    unittest.main()
