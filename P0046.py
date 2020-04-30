# Goldbach's other conjecture
# https://projecteuler.net/problem=46

# Actually from this point forth I will just import what I usually use
from collections import defaultdict
from math import fmod, sqrt
from time import time
start = time()

prime = [True for i in range(1000001)]
prime[0] = prime[1] = False
p = 2
while p <= 1000000:
    if prime[p]:
        for i in range(p * 2, 1000001, p):
            prime[i] = False
    p += 1
print("Sieve finished in", time() - start, "seconds")
ans = 9
while True:
    ans += 2
    if prime[ans]:
        continue
    t = 1
    while 2*t*t < ans:
        if prime[ans - 2*t*t]: break
        t += 1
    else:
        print(ans)
        print(time() - start, "seconds")
        break