def factors(n):
    lower = 1
    upper = n
    total = 0
    while True:
        if n % lower == 0:
            div = n / lower
            if div == lower:
                total += 1
            else:
                total += 2
            upper = n / lower
        lower += 1
        if lower >= upper:
            return total


i = 1
while True:
    triangle = sum([j for j in range(i)])
    if factors(triangle) > 500:
        print(triangle)
        break
    i += 1

