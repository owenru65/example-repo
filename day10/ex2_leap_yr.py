
def is_leap(year):
  
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        isLeapYr = True
      else:
        isLeapYr = False
    else:
      isLeapYr = True
  else:
    isLeapYr = False

  return isLeapYr

  
# TODO: Add more code here 👇
def days_in_month(yr, mon):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
  leapYear = False
  leapYear = is_leap(yr)
  if leapYear == True:
    month_days[1] = 29

  return month_days[mon-1]
  
#🚨 Do NOT change any of the code below 
year = int(input()) # Enter a year
month = int(input()) # Enter a month
days = days_in_month(year, month)
print(days)


