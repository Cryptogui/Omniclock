import time
from datetime import date

now = date.today()
birthday = date(now.year, 1, 8)
if birthday < now:
    birthday = birthday.replace(year=now.year + 1)
print (birthday)
time_to_birthday = abs(birthday - now)
days_to_birthday = time_to_birthday.days

print (str(days_to_birthday) + " days to birthday")
