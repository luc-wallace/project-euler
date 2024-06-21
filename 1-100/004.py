def is_palindrome(n):
    s = str(n)
    return s == s[::-1]


digits = 3
palindrome = 0

for i in range(100, 1000):
    for j in range(100, 1000):
        m = i * j
        if is_palindrome(m) and m > palindrome:
            palindrome = m

print(palindrome)
