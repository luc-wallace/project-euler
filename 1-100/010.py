import math

total = 0


def is_prime(n):
    for i in range(2, round(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


for i in range(2, 2_000_001):
    if is_prime(i):
        total += i

print(total)
