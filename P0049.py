# Prime permutations
# https://projecteuler.net/problem=49

from collections import defaultdict
from itertools import permutations
from math import fmod, sqrt
from time import time

def listToInt(n):
    return int(''.join(list(map(str, n))))

start = time()

prime = [True for i in range(10001)]
p = 2
while p <= 10000:
    if prime[p]:
        for i in range(p * 2, 10001, p):
            prime[i] = False
    p += 1

print("Sieve finished in", time() - start, "seconds")

for i in range(1023, 3341):
    permutes = set(filter(lambda x : len(str(x)) == 4, map(listToInt, permutations(map(int, list(str(i)))))))
    a, b = i + 3330, i + 3330*2
    if prime[i] and prime[a] and prime[b] and a in permutes and b in permutes: print(i, a, b)
print(time() - start, "seconds")