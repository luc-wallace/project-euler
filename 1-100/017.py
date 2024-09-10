nums = {
    1000: "thousand",
    100: "hundred",
    90: "ninety",
    80: "eighty",
    70: "seventy",
    60: "sixty",
    50: "fifty",
    40: "forty",
    30: "thirty",
    20: "twenty",
    19: "nineteen",
    18: "eighteen",
    17: "seventeen",
    16: "sixteen",
    15: "fifteen",
    14: "fourteen",
    13: "thirteen",
    12: "twelve",
    11: "eleven",
    10: "ten",
    9: "nine",
    8: "eight",
    7: "seven",
    6: "six",
    5: "five",
    4: "four",
    3: "three",
    2: "two",
    1: "one",
}

total = 0

for i in range(1, 1001):
    remaining = i
    text = ""
    while remaining > 0:
        for k, v in nums.items():
            if k > remaining:
                continue

            multiple = remaining // k
            remaining -= k * multiple

            if multiple == 1 and k < 100:
                text += v
            else:
                text += nums[multiple] + " " + v

            if remaining > 0:
                if k >= 100:
                    text += " and"
                text += " "

    total += len(list(filter(lambda c: c.isalpha(), text)))

print(total)
