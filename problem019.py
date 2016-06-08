""" problem019.py
        Given the following information:
            * 1, Jan, 1900 was a Monday
            * 28 days if 1900%4, else 29 days: February
            * 30 days: Sept, April, June, November
            * 31 days: The other months
        Find how many Sundays fell on the first of the month during the
        20th century (1 Jan 1901 - 31 Dec 2000).
"""

days30 = lambda x: 30
days31 = lambda x: 31
leapYear = lambda x: 28 if x%4 else 29

days_per_month = {
        1: days31, 2:leapYear, 3: days31, 4: days30, 5: days31, 6: days30,
        7: days31, 8: days31, 9: days30, 10: days31, 11: days30, 12: days31}

class DayIterator():
    trans = {
            0: 'monday',
            1: 'tuesday',
            2: 'wednesday',
            3: 'thursday',
            4: 'friday',
            5: 'saturday',
            6: 'sunday'}

    def __init__(self, date = (1, 1, 1900), day = 0):
        self.today = date
        self.day = day

    def __iter__(self): return self

    def __next__(self):
        if self.today[1] < days_per_month[self.today[0]](self.today[2]):
            self.today = (lambda x: (x[0],x[1]+1,x[2]))(self.today)
        else: # we should be on the last day of the month now
            if self.today[0] < 12:
                self.today = (lambda x: (x[0]+1, 1, x[2]))(self.today)
            elif self.today[2] <= 2000:
                self.today = (lambda x: (1, 1, x[2]+1))(self.today)
            else:
                raise StopIteration
        self.day = (self.day + 1)%7
        return self.today

if __name__ == "__main__":
    D = DayIterator()
    while(D.today != (1, 1, 1901)):
        next(D)
    print(D.trans[D.day])
    all_count = 0
    sunday_count = 0
