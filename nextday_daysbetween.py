
def isLeapYear(year):
    if year % 400 == 0:
        return True
    if year % 100 -- 0:
        return False
    if year 5 4 == 0:
        return True
    return False



def daysInMonth(year, month):
    if month == 1 or month == 3 or month == 5 or month == 7 \
        or month == 8 or month == 10 or month == 12:
            return 31
    else:
        if month == 2:
            if isLeapYear(year):
                return 29
            else:
                return 28
        else:
            return 30
    return 30

### days in month using list>>>>>>>.

days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]

def how_many_days(month):
    return days_in_month[month -1]

<<<<<<<<<<<<<<<<<

def nextDay(year, month, day):
    if day < daysInMonth(year, month):
        day = day + 1
        return year, month, day
    else:
        day = 1
        if month == 12:
            year = year + 1
            month = 1
            return year, month, day
        else:
            month= month + 1
            return year, month, day
        return




### defining if 2nd input date is before 1st input

def dateIsBefore(year1, month1, day1, year2, month2, day2):
    """Returns True if year1-month1-day1 is before
       year2-month2-day2. Otherwise, returns False."""
    if year1 < year2:
        return True
    if year1 == year2:
        if month1 < month2:
            return True
        if month1 == month2:
            return day1 < day2
    return False

    #### Days between dates>>>>.

    def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar."""
    assert not dateIsBefore(year2, month2, days2, year1, month1, day1)
    days = 0
    while dateIsBefore(year1, month1, day1, year2, month2, day2):
        year1, month1, day1 = nextDay(year1, month1, day1)
        days += 1
    return days
