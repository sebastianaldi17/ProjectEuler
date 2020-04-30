# Pentagon numbers
# https://projecteuler.net/problem=44

from math import fmod, sqrt
from time import time

def isPenta(n):
    # Inverse of n(3n + 1) / 2 is (1 + sqrt(1 + 24n)) / 6
    return fmod(sqrt(1 + 24 * n), 6) == 5
def penta(n):
    return n*(3*n-1)//2

start = time()
for i in range(1, 100000):
    for j in range(1, i):
        a, b = penta(i), penta(j)
        if isPenta(a-b) and isPenta(a+b):
            print(a-b)
            print(time() - start, "seconds")
            quit()

            # Almost 3 seconds... Very slow but still "under a minute"