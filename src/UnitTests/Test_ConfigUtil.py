import unittest

from src.Util.ConfigUtil import ConfigUtil


class TestFileManager(unittest.TestCase):


    def test_getValue(self):
        self.assertEqual(ConfigUtil.getValue("login:admin"),("login","admin"))
        self.assertEqual(ConfigUtil.getValue("login: withSpace"),("login","withSpace"))
        self.assertEqual(ConfigUtil.getValue("login: withNewLine\n"),("login","withNewLine"))







