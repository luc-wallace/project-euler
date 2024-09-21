cache = {}


def combinations(digits):
    if len(digits) == 1:
        return [digits]

    if digits in cache:
        return cache[digits]

    combis = []
    for digit in digits:
        rest = tuple(filter(lambda n: n != digit, digits))
        for d in combinations(rest):
            combis.append([digit, *d])
            if len(combis) == 1_000_000:
                return combis

    cache[digits] = combis
    return combis


print("".join(combinations(("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"))[-1]))
