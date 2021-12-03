"""
  Unittest for DateCalculator
  Author: Akter
  Date: 04/12/2021
"""

import unittest
from date import Date

class TestDateMethods(unittest.TestCase):
    def test_Date_is_leap_year_True(self):
        date = Date("01/01/2020")
        self.assertTrue(date.is_leap_year())
    def test_Date_is_leap_year_False(self):
        date = Date("01/01/2021")
        self.assertFalse(date.is_leap_year())
        
    def test_Date_is_valid_date_True(self):
        date = Date("01/01/2021")
        self.assertTrue(date.is_valid_date())
    def test_Date_is_valid_date_ValueError1(self):
        self.assertRaises(ValueError, lambda: Date("01/01/3000"))
    def test_Date_is_valid_date_ValueError2(self):
        self.assertRaises(ValueError, lambda: Date("01/01/qw12"))
        
    def test_Date_subtract1(self):
        first = "02/01/2021"
        second = "02/04/2021"
        from datetime import datetime
        date1 = datetime.strptime(first, "%d/%m/%Y")
        date2 = datetime.strptime(second, "%d/%m/%Y")
        expected_diff = abs((date1 - date2).days) - 1 
        
        self.assertEqual(expected_diff, Date(first) - Date(second))
        
        
if __name__ == "__main__":
    unittest.main()
