import functools

nums = {}


def fib(n):
    if n <= 1:
        return n

    if n in nums:
        return nums[n]

    val = fib(n - 1) + fib(n - 2)
    nums[n] = val
    return val


i = 1
max_d = 0
while True:
    n = fib(i)
    if len(str(n)) == 1000:
        print(i)
        break
    i += 1
