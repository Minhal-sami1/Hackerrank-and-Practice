class Date_returned():
    def __init__(self, data):
        self.day = None
        self.month = None
        self.year = None
        if int(data[0]) <= 31:
            self.day = int(data[0])
        if int(data[1]) <= 12:
            self.month = int(data[1])
        if int(data[2]) <= 3000:
            self.year = int(data[2])

    def test(self):
        if self.day and self.month and self.year:
            print(self.day, self.month, self.year)


class Date_due():
    def __init__(self, data):
        self.day = None
        self.month = None
        self.year = None
        if int(data[0]) <= 31:
            self.day = int(data[0])
        if int(data[1]) <= 12:
            self.month = int(data[1])
        if int(data[2]) <= 3000:
            self.year = int(data[2])

    def test(self):
        if self.day and self.month and self.year:
            print(self.day, self.month, self.year)


class Solution():
    def __init__(self, date_r, date_d):
        self.date_r = Date_returned(date_r)
        self.date_d = Date_due(date_d)

    def check(self):
        if self.date_r.year > self.date_d.year:
            print(10000)
        # If the book is returned on or before the expected return date, no fine will be charged (i.e.: fine = 0)
        elif self.date_r.month < self.date_d.month or self.date_r.year < self.date_d.year:
            print(0)
        # If the book is returned after the expected return day but still within the same calendar month and year as
        # the expected return date, fine = 15 x (the number of days late)
        elif self.date_r.day != self.date_d.day and self.date_r.month == self.date_d.month and self.date_r.year == self.date_d.year:
            print(15*(self.date_r.day - self.date_d.day))
        # If the book is returned after the expected return month but still within the same calendar year as the expected return date
        # the fine = 500 * (The number of months late)
        elif self.date_r.year == self.date_d.year:
            print(500*(self.date_r.month - self.date_d.month))
        else:
            print(10000)
        pass

    def test(self):
        print(self.date_r.day, self.date_d.day)


# Take Input
#date_returned = input().split()
#date_due = input().split()
test = Solution([9, 6, 2015], [8, 6, 2015])
test.check()
