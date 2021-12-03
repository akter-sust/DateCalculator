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
    def test_Date_subtract2(self):
        first = "03/08/2018"
        second = "04/08/2018"
        self.assertEqual(0, Date(first) - Date(second))
    def test_Date_subtract3(self):
        first = "02/06/1983"
        second = "22/06/1983"
        self.assertEqual(19, Date(first) - Date(second))
    def test_Date_subtract4(self):
        first = "04/07/1984"
        second = "25/12/1984"
        self.assertEqual(173, Date(first) - Date(second))
    def test_Date_subtract5(self):
        first = "03/01/1989"
        second = "03/08/1983"
        self.assertEqual(1979, Date(first) - Date(second))
        
        
if __name__ == "__main__":
    unittest.main()
