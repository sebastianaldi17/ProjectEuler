# Non-abundant sums
# https://projecteuler.net/problem=23

# This actually took 5 seconds to process.
# Maybe a faster solution is present?

from math import sqrt
from collections import defaultdict

def divisors(n):
    div = 0
    for i in range(1, int(sqrt(n)) + 1):
        if n%i == 0:
            if i*i == n or n//i == n: div += i
            else: div += i + n//i
        if div > n: return True
    return div > n

ab = []
ans = 0
d = defaultdict(int)
for i in range(1, 28124):
    if divisors(i): ab.append(i)
print("Finished abundant number calculation")
for i in range(len(ab)):
    for j in range(i, len(ab)):
        d[ab[i] + ab[j]] = 1
print("Finished mapping numbers")
for i in range(1, 28124):
    if d[i] == 0: ans += i
print(ans)