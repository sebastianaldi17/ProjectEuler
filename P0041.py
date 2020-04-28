# Pandigital prime
# https://projecteuler.net/problem=41

# Lets recycle Sieve of Erasthotenes, a very handy tool for primes
# 1-n pandigital means the highest pandigital prime is at best 9 digits long
# but 1-9 pandigital is impossible because the sum of digits would always be 45
# 1-8 is also not possible
# 1-7 looks acceptable (results in 28)
# https://en.wikipedia.org/wiki/Divisibility_rule

from math import sqrt
from itertools import permutations

def isPrime(n):
    if n%2 == 0 or n%3 == 0: return False
    for i in range(5, int(sqrt(n)) + 1, 2):
        if n%i == 0: return False
    return True

def listToInt(n):
    return int(''.join(list(map(str, n))))

ans = 0
for i in permutations([1,2,3,4,5,6,7]):
    if isPrime(listToInt(i)): ans = max(ans, listToInt(i))
print(ans)