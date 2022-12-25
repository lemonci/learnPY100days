def is_leap(year: int):
    if year % 4 == 0 and year % 100 != 0:
        return True
    elif year % 400 == 0:
        return True
    else:
        return False

def which_day(year, month, date):
    if is_leap(year):
        month_days = {1:31, 2:29, 3:31, 4:30, 5: 31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    else:
        month_days = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    days = 0
    for i in range(1, month):
        days += month_days[month]

    days = days + date
    return days