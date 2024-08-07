known_values: dict[int, int] = {}


def collatz(n):
    if n == 1:
        return 1

    if n in known_values:
        return known_values[n]

    if n % 2 == 0:
        terms = collatz(n / 2)
    else:
        terms = collatz(3 * n + 1)
    known_values[n] = terms + 1
    return terms + 1


num = 0
most_terms = 0

for n in range(1, 1_000_001):
    terms = collatz(n)
    if terms > most_terms:
        num = n
        most_terms = terms

print(f"{num} has the most terms, with {most_terms}")
