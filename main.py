import datetime

print(" 🌟 Event Countdown Timer 🌟 ")
print()

event = input("Input the event > ")
print()
year = int(input("Input the year > "))
print()
month = int(input("Input the month > "))
print()
day = int(input("Input the day > "))
print()
today = datetime.date.today()
eventDate = datetime.date(year, month, day)
if eventDate > today:
  difference = eventDate - today
  difference = difference.days
  print(f"{event} is coming up in {difference} days!")
  print()
elif eventDate < today:
  difference = today - eventDate
  difference = difference.days
  print(f"😭😭😭😭" + event + " has passed!")
  print()
else:
  print(f"{event} is today!")
  print()
