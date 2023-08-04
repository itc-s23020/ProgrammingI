import calendar


def print_calendar(year, month):
    cal = calendar.month(year, month)
    print(cal)


year = 2023
month = 8
print_calendar(year, month)
