def recurring_cycle(n):
    remainders = set()
    div = 1
    while True:
        while n > div:
            div *= 10
        r = div % n
        if r == 0:
            return 0
        elif r in remainders:
            return len(remainders)
        remainders.add(r)
        div = r


d = 0
max_cycle = 0

for i in range(1, 1001):
    c = recurring_cycle(i)
    if c > max_cycle:
        d = i
        max_cycle = c


print(d)
