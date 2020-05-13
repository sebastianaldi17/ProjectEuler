# Prime digit replacements
# https://projecteuler.net/problem=51

from collections import defaultdict
from copy import deepcopy
from itertools import permutations
from math import fmod, sqrt
from time import time

def listToInt(n):
    # Takes a list of numbers and combine it
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
for i in range(56003, 1000000):
    if prime[i]: primes.append(i)

# Take existing primes so that at least there is one
for x in primes:
    L = list(map(int, str(x)))
    for e in L:
        # Skip 1-2 and 4 repetitions because they won't result in an 8 prime family
        # https://math.stackexchange.com/questions/166800/primality-and-repeated-digits
        if L.count(e) < 3 or L.count(e) == 4: continue
        temp = deepcopy(L)
        index, family, prime_family = [], [], []
        for i in range(len(L)):
            if L[i] == e: index.append(i)
        for i in range(0, 10):
            for y in index:
                temp[y] = i
            if len(str(listToInt(temp))) == len(L): family.append(listToInt(temp))
        for y in family:
            if prime[y]: prime_family.append(y)
        if len(prime_family) == 8:
            print(prime_family[0])
            print(time() - start, "seconds")
            quit()