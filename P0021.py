# Amicable numbers
# https://projecteuler.net/problem=21

from collections import defaultdict
from math import sqrt

def divisors(n):
    div = 0
    for i in range(1, int(sqrt(n)) + 1):
        if n%i == 0:
            if i*i == n or n//i == n: div += i
            else: div += i + n//i
    return div

ami = defaultdict(int)
for i in range(1, 10000):
    ami[i] = divisors(i)
ans = 0
for i in range(1, 10000):
    if i == ami[ami[i]] and i != ami[i]:
        print(i, ami[i])
        ans += i + ami[i]
print(ans//2)