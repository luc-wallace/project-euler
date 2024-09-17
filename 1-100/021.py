def d(n):
    divisors = []
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            divisors.append(i)
    return sum(divisors)


numbers = set()

for a in range(1, 10000):
    if a in numbers:
        continue
    b = d(a)
    if d(b) == a and b != a:
        numbers.add(a)
        numbers.add(b)

print(sum(numbers))
