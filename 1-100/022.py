from string import ascii_uppercase

with open("0022_names.txt", "r") as f:
    names = sorted([name.strip('"') for name in f.read().split(",")])

total = 0

for i, name in enumerate(names):
    score = sum([ascii_uppercase.index(c) + 1 for c in name])
    total += (i + 1) * score

print(total)
