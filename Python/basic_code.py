from calendar import month
from datetime import date

def CalculateAge(born):
    today = date.today()
    try:
        birthday = born.replace(year = today.year)

    except ValueError:
        birthday = born.replace(year = today.year, month = born.month + 12, day = 23)

    if birthday > today:
        return today.year - born.year - 1
    else:
        return today.year - born.year 

print(CalculateAge(date(2000, 12, 23,)), "years")
