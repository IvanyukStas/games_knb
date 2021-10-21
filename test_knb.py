import unittest

from main import Knb


class Test(unittest.TestCase):

    def setUp(self):
        self.choise = Knb()

    def test_equil(self):
        #True
        self.assertTrue(self.choise.get_choice('1', 2))
        self.assertTrue(self.choise.get_choice('2', 3))
        self.assertTrue(self.choise.get_choice('3', 2))
        self.assertTrue(self.choise.get_choice('3', 4))
        self.assertTrue(self.choise.get_choice('4', 1))
        self.assertTrue(self.choise.get_choice('4', 2))
        #False
        self.assertFalse(self.choise.get_choice('1', 1))
        self.assertFalse(self.choise.get_choice('1', 3))
        self.assertFalse(self.choise.get_choice('1', 4))
        self.assertFalse(self.choise.get_choice('2', 1))
        self.assertFalse(self.choise.get_choice('2', 2))
        self.assertFalse(self.choise.get_choice('2', 4))