# Nth Prime Number (10001)
# https://projecteuler.net/problem=7 
from math import log
n = 10001
def solve(n):
    smallPrimes = [-1, 2, 3, 5, 7, 11, 13]
    if n < len(smallPrimes): return smallPrimes[n]
    index = 0
    approx = int(n * log(n) + n * log(log(n))) + 1
    prime = [True for i in range(approx)]
    prime[0] = prime[1] = False
    p = 2
    while p < approx:
        if prime[p]:
            for i in range(p * 2, approx, p):
                prime[i] = False
        p += 1
    for i in range(approx):
        if prime[i]:
            index += 1
            if index == n: return i
    return "Not found (Bug?)"
print(solve(n))