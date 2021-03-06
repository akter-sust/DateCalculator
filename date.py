"""
    Date Calculator
    Author: Akter
    Date: 04/12/2021
"""
import re
import argparse

class Date:
    date = None
    def __init__(self, date: str):
        """
            Constructor of Date
        """
        self.date = date.strip()
        # since python indexing from 0 and month started from 1, 
        # we set 0 for 0th index of days_in_month
        self.days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if not self.is_valid_date():
            raise ValueError("Invalid formatted Date provided")
        
    def is_leap_year(self):
        """
            the year is checking for leap year according to Gregorian calendar 
            source: https://en.wikipedia.org/wiki/Leap_year
        """
        if self.year % 4 != 0:
            return False
        elif self.year % 100 != 0:
            return True
        elif self.year % 400 != 0:
            return False
        else:
            return True
        
    def adjust_days_of_february_for_leap_year(self):
        """
            If it is leap year, then days of february is 29
            otherwise 28
        """
        if self.is_leap_year():
            self.days_in_month[2] = 29
        
    def is_valid_date(self):
        """
            This function will return false if the date is wrong format 
            (correct format is DD/MM/YYYY) and 
            not in between 01/01/1901 and 31/12/2999
        """
        match = re.search(r'(\d{2}/\d{2}/\d{4})', self.date)
        if match is None:
            return False
            
        split_date = self.date.split("/")
        self.day = int(split_date[0])
        self.month = int(split_date[1])
        self.year = int(split_date[2])
        
        if self.year < 1901 or self.year > 2999:
            return False
        if self.month < 1 or self.month > 12:
            return False
        
        self.adjust_days_of_february_for_leap_year()
        
        if self.day > self.days_in_month[self.month]:
            return False
            
        return True
            
    def __sub__(self, date_b: "Date"):
        """
            mathmatical substruct for the date class
        """
        assert isinstance(date_b, Date)
        if not self.is_valid_date():
            raise ValueError("Invalid formatted first Date provided")
        if not date_b.is_valid_date():
            raise ValueError("Invalid formatted second Date provided")
             
        number_of_leap_year = lambda x: (x//4) - (x//100) + (x//400)
        
        # considering previous year for number of leap year, 
        # since leap year for current year is coming through days of month
        days_a = self.year * 365 + number_of_leap_year(self.year - 1) + \
                 sum(self.days_in_month[:self.month]) + \
                 self.day
                 
        days_b = date_b.year * 365 + number_of_leap_year(date_b.year - 1) + \
                 sum(date_b.days_in_month[:date_b.month]) + \
                 date_b.day
                 
        diff = abs(days_a - days_b) - 1 # subtract 1 due to non inclusive of both dates 
        if diff < 0:
            # for same first and second date is not defined, so i am returning 0.
            diff = 0
        return diff 
        
if __name__ == "__main__":
    # Instantiate the parser
    parser = argparse.ArgumentParser(description='Date Calculator: usage example "python date.py 02/03/1989 03/08/2099"')
    # Two required positional argument
    parser.add_argument('first', type=str, help='The first date in DD/MM/YYYY format.')
    parser.add_argument('second', type=str, help='The second date in DD/MM/YYYY format.')
    args = parser.parse_args()
    
    date1 = Date(args.first)
    date2 = Date(args.second)
    print(date1 - date2)
    
            
