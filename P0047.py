# Distinct primes factors
# https://projecteuler.net/problem=47

# Actually from this point forth I will just import what I usually use
from collections import defaultdict
from math import fmod, sqrt
from time import time

start = time()

prime = [0 for i in range(1000001)]
p = 2
while p <= 1000000:
    if prime[p] == 0:
        for i in range(p * 2, 1000001, p):
            prime[i] += 1
    p += 1

print("Sieve finished in", time() - start, "seconds")
# print(primeList)
ans = 2*3*5*7
while True:
    if prime[ans] == prime[ans+1] == prime[ans+2] == prime[ans+3] == 4:
        print(ans)
        print(time() - start, "seconds")
        break
    ans += 1