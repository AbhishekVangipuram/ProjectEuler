from datetime import date, timedelta

d = date(1901, 1, 1)
new_day = timedelta(days=1)
tot_sundays = 0

while d.isoformat() != "2000-12-31":
    if d.weekday() == 6 and d.day == 1:
        tot_sundays += 1
    d = d+new_day
print(tot_sundays)
