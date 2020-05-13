# Permuted multiples
# https://projecteuler.net/problem=52

from collections import defaultdict
from copy import deepcopy
from itertools import permutations
from math import fmod, sqrt
from time import time

start = time()

ans = 1
while True:
    if sorted(str(ans)) == sorted(str(ans*2)) == sorted(str(ans*3)) == sorted(str(ans*4)) == sorted(str(ans*5)) == sorted(str(ans*6)):
        print(ans)
        print(time() - start, "seconds")
        break
    ans += 1