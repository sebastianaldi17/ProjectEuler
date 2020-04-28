# Integer right triangles
# https://projecteuler.net/problem=39

from math import sqrt

ans = (0, 0)
for p in range(3, 1001):
    solutions = 0
    for b in range(1, p):
        a = (p*p + 2*b*p)/(2*(b+p))
        if a == int(a): solutions += 1
    if solutions > ans[1]:
        ans = (p, solutions)
print(ans)