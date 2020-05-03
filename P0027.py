# Quadratic primes
# https://projecteuler.net/problem=27
from math import sqrt
from time import time

def check(n):
    if n < 0: n *= -1
    limit = int(sqrt(n)) + 1
    for i in range(2, limit + 1):
        if n%i == 0: return False
    return True

start = time()
ans = (0, 0, 0)
for a in range(-999, 1000):
    for b in range(-1000, 1001):
        n = 0
        while check(n*n + a*n + b):
            n += 1
        if n > ans[0]:
            ans = (n, a, b)
print(ans[1]*ans[2])
print(time() - start, "Seconds")