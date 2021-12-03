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
        if self.month not in self.days_in_month:
            return False
        
        self.adjust_days_of_february_for_leap_year()
        
        if self.day > self.days_in_month[self.month]:
            return False
            
        return True
            
    def __sub__(self, date_b):
        if not self.is_valid_date():
            return "Invalid first date"
        if not date_b.is_valid_date():
            return "Invalid second date"
            
        number_of_leap_year = lambda x: (x//4) - (x//100) + (x//400)
        # considering previous year for number of leap year, 
        # since leap year for current year is coming through days of month
        days_a = self.year * 365 + number_of_leap_year(self.year - 1) + \
                 sum([self.days_in_month[m] for m in range(1, self.month)]) + \
                 self.day
                 
        days_b = date_b.year * 365 + number_of_leap_year(date_b.year - 1) + \
                 sum([date_b.days_in_month[m] for m in range(1, date_b.month)]) + \
                 date_b.day
                 
        diff = abs(days_a - days_b) - 1 # subtract 1 due to non inclusive of both dates 
        return diff 
        
if __name__ == "__main__":
    date1 = "03/01/1989"
    date2 = "03/08/1983"
    start = Date(date1)
    end = Date(date2)
    print(end - start)
    
    from datetime import datetime
    date1 = datetime.strptime(date1, "%d/%m/%Y")
    date2 = datetime.strptime(date2, "%d/%m/%Y")
    diff = date1 - date2
    print(diff.days-1)
            
