# Summation of primes
# https://projecteuler.net/problem=10

N = 2000000
def solve(n):
    ans = 0
    prime = [True for i in range(n+1)]
    prime[0] = prime[1] = False
    p = 2
    while p < n+1:
        if prime[p]:
            for i in range(p * 2, n+1, p):
                prime[i] = False
        p += 1
    for i in range(n+1):
        if prime[i]: ans += i
    print(ans)
solve(N)