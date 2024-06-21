square_of_sum = sum([n for n in range(1, 101)]) ** 2
sum_of_squares = 0

for i in range(1, 101):
    sum_of_squares += i ** 2

print(abs(sum_of_squares - square_of_sum))
