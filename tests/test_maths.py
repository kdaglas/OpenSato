import unittest
from math import add_numbers

class TestMaths(unittest.TestCase):

	def test_can_add_numbers():
        result = add_numbers(1,2)
        self.assertEquals(3, result)
        result2 = add_numbers(1,2,3,4)
        self.assertEquals(12, result2)

    def test_can_throw_type_error_for_str(self):
        result = add_numbers(1,'2')
        self.assertEquals(3, result)
        with self.assertRaises(ValueError):
            pass

    def test_can_throw_value_error(self):
        with self.assertRaises(ValueError):
            add_numbers(1, '2')
            



