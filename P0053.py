# Combinatoric selections
# https://projecteuler.net/problem=53

from collections import defaultdict
from copy import deepcopy
from itertools import permutations
from math import fmod, sqrt, factorial
from time import time

start = time()

f = [factorial(i) for i in range(101)]
ans = 0
for n in range(1, 101):
    for r in range(1, n+1):
        if f[n] / (f[r] * f[n-r]) >= 1000000: ans += 1
print(ans)
print(time() - start, "seconds")