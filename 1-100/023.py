from math import sqrt

abundant_numbers = []
total = 0


def proper_divisor_diff(n):
    total = 1
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            d = n / i
            total += i
            if d != i:
                total += d
    return total - n


def is_sum(n):
    if len(abundant_numbers) < 2:
        return False

    for x in abundant_numbers:
        c = n - x
        left = 0
        right = len(abundant_numbers) - 1

        while left <= right:
            mid = (left + right) // 2
            item = abundant_numbers[mid]
            if c == item:
                return True
            elif c > item:
                left = mid + 1
            else:
                right = mid - 1

    return False


for i in range(1, 28124):
    if proper_divisor_diff(i) > 0:
        abundant_numbers.append(i)
    if not is_sum(i):
        total += i

print(total)
