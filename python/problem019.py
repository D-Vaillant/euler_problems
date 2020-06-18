""" problem019.py:
        1 Jan 1900 was a Monday.
        Thirty days has September,
        April, June and November.
        All the rest have thirty-one,
        Saving February alone,
        Which has twenty-eight, rain or shine.
        And on leap years, twenty-nine.
        A leap year occurs on any year evenly divisible by 4,
            but not on a century unless it is divisible by 400.

        How many Sundays fell on the first of the month during the twentieth
            century (1 Jan 1901 to 31 Dec 2000)?
"""
from enum import Enum

class Month(Enum):
    JAN = 1
    FEB = 2
    MAR = 3
    APR = 4
    MAY = 5
    JUN = 6
    JUL = 7
    AUG = 8
    SEP = 9
    OCT = 10
    NOV = 11
    DEC = 12

    def step(self):
        if self.value == 12:
            return Month.JAN
        else:
            return Month(self.value + 1)


def days_per_month(month, year):
    if month == Month.FEB:
        if year % 100 == 0:
            return 28 if year % 400 else 29
        return 28 if year % 4 else 29
    elif month in [Month.SEP, Month.APR, Month.JUN, Month.NOV]:
        return 30
    else:
        return 31


class MonthFirstDay():
    def __init__(self):
        self.day = 1
        self.year = 1900
        self.month = Month.JAN

        # Move that sucka up.
        while self.year != 1901:
            self.push()

    def push(self):
        self.day += days_per_month(self.month, self.year)
        # self.day %= 7
        if self.month == Month.DEC:
            self.year += 1
        self.month = self.month.step()

    def is_sunday(self):
        return (self.day % 7) == 0

    def main(self):
        sundays = 0
        while self.year < 2001:
            self.push()
            if self.is_sunday():
                sundays += 1
        return sundays
            

if __name__ == "__main__":
    doer = MonthFirstDay()
    print(doer.main())
