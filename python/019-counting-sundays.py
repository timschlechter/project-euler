
def days_in_month(month, year):
    if (month in [1,3,5,7,8,10,12]):
        return 31
    if (month in [4,6,9,11]):
        return 30
    return 29 if is_leapyear(year) else 28

def is_leapyear(year):
    if (year % 100 == 0 and year % 400 != 0):
        return False
    return year % 4 == 0

# 1/1/1901 is a tuesday, day 6 is a sunday
def is_sunday(day):
    return day % 7 == 6

sundays_found = 0
day = 1
year = 1901
while year < 2001:
    for month in range(1, 13):
        day += days_in_month(month, year)
        if (is_sunday(day)):
            sundays_found += 1
    year = year + 1

print(sundays_found)