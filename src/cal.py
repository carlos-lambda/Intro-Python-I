"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `calendar.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
import datetime

current = datetime.datetime.now()
cal = calendar.TextCalendar()
arg = sys.argv


def toNum(arg):
    if arg.isdigit():
        return int(arg)
    else:
        return False


m = toNum(input("enter month: "))
if m == False:
    m = datetime.date.today().month
y = toNum(input("enter year: "))
if y == False:
    y = datetime.date.today().year

user = (m, y)
print(len(user))
if (len(user) == False):
    print('Expecting input in the form of month [year]')
    exit()

month = len(arg) > 1 and toNum(arg[1]) or datetime.date.today().month
year = len(arg) > 2 and toNum(arg[2]) or datetime.date.today().year

cal.prmonth(year, month)
