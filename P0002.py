# Even Fibonacci Sum (inclusive)
# https://projecteuler.net/problem=2

def solve(n):
    a, b = 1, 2
    ans = 2
    add = False
    while a + b <= n:
        if (a+b)%2==0: ans += a+b
        a, b = b, a+b
    return ans
print(solve(4000000))

# Is there a mathematical approach to this?