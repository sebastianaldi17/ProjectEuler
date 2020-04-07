# Sum square difference
# https://projecteuler.net/problem=6

def solve(n):
    sn = (n*(n+1)//2) * (n*(n+1)//2)
    sn2 = n*(n+1)*(2*n+1)//6 # sum of first n squared natural numbers
    return abs(sn - sn2)

print(solve(100))