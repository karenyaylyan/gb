class Date:
    def __init__(self, date):
        self.day, self.month, self.year = Date.parse_date(date)

    @classmethod
    def parse_date(cls, date):
        day, month, year = map(int, date.split('-'))
        Date.validate_date(day, month, year)
        return day, month, year

    @staticmethod
    def validate_date(day, month, year):
        days_in_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if month < 1 or month > 12:
            raise ValueError('invalid date')
        elif day < 1 or day > days_in_month[month - 1]:
            raise ValueError('invalid date')
        elif (month == 2 and day == 29 and not
                (year % 4 == 0 and year % 100 != 0 or year % 400 == 0)):
            raise ValueError('invalid date')


simple_date = Date('01-11-2020')
assert simple_date.day == 1 and simple_date.month == 11 and simple_date.year == 2020

leap_year_date = Date('29-2-2020')
assert leap_year_date.day == 29 and leap_year_date.month == 2 and leap_year_date.year == 2020

try:
    date = '29-2-1700'
    Date(date)
except ValueError:
    print(f'{date} is not correct date')

try:
    date = '2-13-2021'
    Date(date)
except ValueError:
    print(f'{date} is not correct date')

try:
    date = '34-01-2021'
    Date(date)
except ValueError:
    print(f'{date} is not correct date')
