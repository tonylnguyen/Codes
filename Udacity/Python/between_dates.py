# Credit goes to Websten from forums
#
# Use Dave's suggestions to finish your daysBetweenDates
# procedure. It will need to take into account leap years
# in addition to the correct number of days in each month.


def leap(year):
    if year%400 == 0:
        return True
    if year%100 != 0 and year%4 ==0:
        return True
    else:
        return False

def days_in_month(year, month):

    thirty_one_days = [1, 3, 5, 7, 8, 10, 12]
    thirty_days = [4, 6, 9, 11]

    if leap(year) == True:
        if month == 2:
            return 29

    if leap(year) == False:
        if month == 2:
            return 28
    if month in thirty_one_days:
        return 31
    if month in thirty_days:
        return 30


def nextDay(year, month, day):
    """Simple version: assume every month has 30 days"""
    if day < days_in_month(year, month):
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1

def dateIsBefore(year1, month1, day1, year2, month2, day2):
    """Returns True if year1-month1-day1 is before year2-month2-day2. Otherwise, returns False."""
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
    return False

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar."""
    # program defensively! Add an assertion if the input is not valid!
    assert not dateIsBefore(year2, month2, day2, year1, month1, day1)
    days = 0
    while dateIsBefore(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        days += 1
    return days

print (leap(1900))
print(daysBetweenDates(1900, 1, 1, 1999, 12, 31))
