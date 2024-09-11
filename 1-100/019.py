weekday = 1
year = 1900
total = 1

for _ in range(100):
    month = 1
    for _ in range(12):
        days = 31
        if month == 2:
            days = 28
            if year % 4 == 0 and year % 100 != 0:
                days = 29
            elif year % 400 == 0:
                days = 29
        elif month in (4, 6, 9, 11):
            days = 30

        for i in range(1, days + 1):
            if year >= 1901 and i == 1 and weekday == 7:
                total += 1
            weekday = 1 if weekday == 7 else weekday + 1

        month += 1
    year += 1

print(total)
