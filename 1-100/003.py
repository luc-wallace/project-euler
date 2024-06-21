import math

num = 600851475143
factor = 0


def is_prime(n):
    for i in range(2, math.floor(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


for i in range(2, round(math.sqrt(num))):
    if num % i == 0 and is_prime(i):
        factor = i


print(factor)
