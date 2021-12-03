'''


'''
import re

class Date:
    days_in_month = {"01": 31, "02": 28, "03": 31, "04": 30,
                     "05": 31, "06": 28, "07": 31, "08": 31,
                     "09": 30, "10": 31, "11": 30, "08": 31}
    date = None
    def __init__(self, date: str):
        self.date = date.strip()
        
    def is_leap_year(self, year: int):
        """
            the year is checking for leap year according to Gregorian calendar 
            source: https://en.wikipedia.org/wiki/Leap_year
        """
        if year % 4 != 0:
            return False
        elif year % 100 != 0:
            return True
        elif year % 400 != 0:
            return False
        else:
            return True
            
        
    def is_valid_date(self):
        """
            This function will return false if the date is wrong and 
            not in between 01/01/1901 and 31/12/2999
        """
        match = re.search(r'(\d{2}/\d{2}/\d{4})', self.date)
        if match.group(1) != self.date:
            return False
            
        split_date = self.date.split("/")
        day = int(split_date[0])
        month = split_date[1]
        year = int(split_date)
        
        if year < 1901 or year > 2999:
            return False
        if month not in days_in_month:
            return False
        
        if month == "02" and day <= (days_in_month[month] 
        elif day <= days_in_month[month]
        
if __name__ == "__main__":
    start = Date("02/02/2099")
    print(start.is_valid_date())
        
