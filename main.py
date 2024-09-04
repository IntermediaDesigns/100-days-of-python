year = int(input("Enter a year: "))
days_in_year = 365

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
  days_in_year = 366

hours_in_day = 24
minutes_in_hour = 60
seconds_in_minute = 60
result = days_in_year * hours_in_day * minutes_in_hour

print(f"There are {result} seconds in the year {year}")