'''


'''
import re

class Date:
    days_in_month = {1: 31,  2: 28,  3: 31,  4: 30,
                     5: 31,  6: 28,  7: 31,  8: 31,
                     9: 30, 10: 31, 11: 30, 12: 31}
    date = None
    def __init__(self, date: str):
        self.date = date.strip()
        
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
            This function will return false if the date is wrong and 
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
        if self.month not in self.days_in_month:
            return False
        
        self.adjust_days_of_february_for_leap_year()
        
        if self.day > self.days_in_month[self.month]:
            return False
            
        return True
            
        
if __name__ == "__main__":
    start = Date("02/21/2099")
    print(start.is_valid_date())
        
