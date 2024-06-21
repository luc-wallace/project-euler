import math


def is_prime(n):
    for i in range(2, math.floor(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


i = 2
n = 0
prime = 0
while True:
    if is_prime(i):
        prime = i
        n += 1
    i += 1
    if n == 10001:
        break

print(prime)
