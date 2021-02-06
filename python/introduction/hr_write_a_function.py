import calendar

def is_leap_method_one(year):
    leap = False
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        leap = True
    return leap


def is_leap_method_two(year):
    return(year % 400 == 0) or (year % 100 != 0 and year % 4 == 0)


def is_leap_method_three(year):
    return calendar.isleap(year) 

year = int(input())
print(is_leap_method_one(year))
print(is_leap_method_two(year))
print(is_lea_method_three(year))
