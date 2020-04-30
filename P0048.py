# Self powers
# https://projecteuler.net/problem=48

# Actually from this point forth I will just import what I usually use
from collections import defaultdict
from math import fmod, sqrt
from time import time

start = time()

# Python limitless int approach
print(sum([i**i for i in range(1, 1001)])%10000000000)
print(time() - start, "Seconds")

# Modular exponentation approach
mod_time = time()
ans = 0
for i in range(1, 1001):
    temp = i % 10000000000
    for j in range(i-1):
        temp *= i % 10000000000
    ans += temp
print(ans%10000000000)
print("Modular exponentation time:", time() - start, "Seconds")