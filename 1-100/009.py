import math


def find_product_triplet_sum(s):
    for a in range(2, s + 1):
        for b in range(2, s + 1):
            c = math.sqrt(a**2 + b**2)
            if not c.is_integer():
                continue
            if a + b + c == s:
                return int(a * b * c)
    return None


print(find_product_triplet_sum(1000))
