# Highly divisible triangular number
# https://projecteuler.net/problem=12

from math import sqrt

def divisors(n):
    div = 0
    for i in range(1, int(sqrt(n)) + 1):
        if n%i == 0:
            if i*i == n: div += 1
            else: div += 2
    return div

# PURE NAIVE SOLUTION [~5 seconds]
# init, add = 1, 2
# while True:
#     if divisors(init) > 500:
#         print(init)
#         break
#     init += add
#     add += 1

# Number-of-Divisors function
# If a, b is relative prime,
# then number of divisors of a*b is n_divisors(a) * n_divisors(b)
# If i is odd, i and (i+1)/2 is relative prime
# If i is even, i/2 and i+1 is relative prime
i = 1
while True:
    if divisors((i + 1) // 2) * divisors(i) > 500:
        print((i+1)//2 * i)
        break
    i += 1
    if divisors(i+1) * divisors(i//2) > 500:
        print((i+1) * i//2)
        break
    i += 1