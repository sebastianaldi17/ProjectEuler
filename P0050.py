# Consecutive prime sum
# https://projecteuler.net/problem=50

from collections import defaultdict
from itertools import permutations
from math import fmod, sqrt
from time import time

def listToInt(n):
    return int(''.join(list(map(str, n))))

start = time()

primes = []
prime = [True for i in range(1000001)]
p = 2
while p <= 1000000:
    if prime[p]:
        for i in range(p * 2, 1000001, p):
            prime[i] = False
    p += 1
for i in range(2, 1000001):
    if prime[i]: primes.append(i)
print("Sieve finished in", time() - start, "seconds")

ans = (0, 0)
print(len(primes))
for i in range(len(primes) - 1):
    csc = primes[i]
    for j in range(i+1, len(primes)):
        if prime[csc] and ans[1] < j - i: ans = (csc, j-i)
        csc += primes[j]
        if csc >= 1000000: break
print(ans)