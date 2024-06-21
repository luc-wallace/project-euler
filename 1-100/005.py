import math


def is_prime(n):
    for i in range(2, math.floor(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def prime_factorisation(n):
    factors = []
    while n != 1:
        for i in range(2, n + 1):
            if n % i == 0 and is_prime(i):
                factors.append(i)
                n //= i
                break
    return factors


final_factors = []

for i in range(1, 21):
    temp = final_factors.copy()
    for factor in prime_factorisation(i):
        if factor in temp:
            temp.remove(factor)
        else:
            final_factors.append(factor)

total = 1
for factor in final_factors:
    total *= factor

print(total)
