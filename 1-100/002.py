n1 = 1
n2 = 1
sum = 0
total = 0

while sum < 4_000_000:
    sum = n1 + n2
    if sum % 2 == 0:
        total += sum
    n1 = n2
    n2 = sum

print(total)
