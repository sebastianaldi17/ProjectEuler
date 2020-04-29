# Sub-string divisibility
# https://projecteuler.net/problem=43

# Permuting the solution space (10! = 36.278.800) is faster,
# Compared to doing a complete search from 1.023.456.789 => 9.876.543.210

from itertools import permutations
from time import time

def listToInt(n):
    return int(''.join(list(map(str, n))))

start = time()
p = [-1, 2, 3, 5, 7, 11, 13, 17]
ans = 0
for i in permutations([0,1,2,3,4,5,6,7,8,9]):
    if i[0] == 0: continue # First digit must not be 0
    if i[3]%2 == 1: continue # d2d3d4 divisible by 2 = d4 must be even
    if (i[2] + i[3] + i[4])%3 != 0: continue # d3d4d5 divisible by 3 = digit sum must be divisible by 3
    if i[5]%5 != 0: continue #d4d5d6 divisible by 5 = d6 must be 0 or 5
    special = True
    num = str(listToInt(i))
    for j in range(1, 8):
        if int(num[j:j+3]) % p[j]:
            special = False
            break
    if special: ans += int(num)
print(ans)
print(time() - start, "seconds") # ~ 1.5 seconds