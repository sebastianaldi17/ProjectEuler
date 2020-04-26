# Reciprocal cycles
# https://projecteuler.net/problem=26
from collections import defaultdict
def sieve(n):
    L = []
    prime = [True for i in range(n+1)]
    p = 2
    while p <= n:
        if prime[p]:
            for i in range(p*2, n+1, p):
                prime[i] = False
        p += 1
    # If a number's prime factorization is only 2 and 5,
    # it is a terminating decimal
    prime[2] = prime[5] = False
    for i in range(2, n+1):
        if prime[i]: L.append(i)
    return L

primes = sieve(1000)
ans = (3, 1)
d = defaultdict(int)
for i in range(1, 1000):
    for x in primes:
        if i%x == 0: break
    else: continue
    dec = 1
    j = 1
    while True:
        if d[dec] > 0:
            if j - d[dec] > ans[1]:
                ans = (i, j - d[dec])
            break
        d[dec] = j
        dec *= 10
        dec = dec%i
        j += 1
    d = defaultdict(int)
print(ans)