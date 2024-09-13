import math
import itertools


# Get nth (d) digit of a number (n)
def digit(n, d):
    return (n / (10 ** (d - 1))) % 10 // 1


# Arbitrary length multiplication
def multiply(n1, n2):
    sums = []
    for x, i in enumerate(n2):
        carry = 0
        digits = []
        for y, j in enumerate(n1):
            product = i * j + carry
            carry = 0 if product < 10 else digit(product, 2)
            digits.append(digit(product, 1))
            if product > 9 and y + 1 == len(n1):
                digits.append(digit(product, 2))
        sums.append([0 for _ in range(x)] + digits)
    carry = 0
    digits = []

    columns = list(enumerate(itertools.zip_longest(*sums, fillvalue=0)))
    for count, nums in columns:
        total = sum(nums) + carry
        carry = 0 if total < 10 else digit(total, 2)
        digits.append(digit(total, 1))
        if total > 9 and count + 1 == len(columns):
            digits.append(digit(total, 2))

    return digits


# 100 represented in digits (backwards)
product = [0, 0, 1]

for i in range(99, 0, -1):
    num = [digit(i, j + 1) for j in range(math.ceil(math.log(i + 1, 10)))]
    product = multiply(product, num)

# Sum all digits together
print(sum(product))
