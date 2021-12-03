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
        days_a = self.year * 365 + number_of_leap_year(self.year) + \
                 sum([self.days_in_month[m] for m in range(1, self.month)]) + \
                 self.day
                 
        days_b = date_b.year * 365 + number_of_leap_year(date_b.year) + \
                 sum([date_b.days_in_month[m] for m in range(1, date_b.month)]) + \
                 date_b.day
                 
        print(number_of_leap_year(self.year), "---", number_of_leap_year(date_b.year))
        print(sum([self.days_in_month[m] for m in range(1, self.month)]), "---", sum([date_b.days_in_month[m] for m in range(1, date_b.month)]))
        print(days_a, "---", days_b)
        diff = days_a - days_b
        if diff < 0:
            return "Second date is greater than first date"
        return diff - 1 # subtract 1 due to non inclusive of both dates 
        
if __name__ == "__main__":
    start = Date("02/01/2021")
    end = Date("02/01/2021")
    print(end - start)
        
