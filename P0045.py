# Triangular, pentagonal, and hexagonal
# https://projecteuler.net/problem=45

from math import fmod, sqrt
from time import time

def isPenta(n):
    # Inverse of n(3n + 1) / 2 is (1 + sqrt(1 + 24n)) / 6
    return fmod(sqrt(1 + 24 * n), 6) == 5
def isHexa(n):
    # Inverse of n(2n - 1) is (1 + sqrt(1 + 8n)) / 4
    return fmod(sqrt(1 + 8*n), 4) == 3

start = time()
for i in range(286, 100000):
    check = i * (i+1) // 2
    if isPenta(check) and isHexa(check):
        print(check)
        print(time() - start, "seconds")
        quit()