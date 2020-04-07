# Largest prime factor
# https://projecteuler.net/problem=3

# Sieve of erasthotenes apporach
# But still slow due to iteration to sqrt(n)
from math import sqrt
question = 600851475143
def solve(n):
    ans = 1
    limit = int(sqrt(n))
    prime = [True for i in range(limit+1)]
    p = 2
    while p <= limit:
        if prime[p]:
            for i in range(p*2, limit+1, p):
                prime[i] = False
        p += 1
    for i in range(2, limit+1):
        if n%i==0 and prime[i]: ans = i
    return ans
print(solve(question))