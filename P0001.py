# Lower than N (exclusive)
# https://projecteuler.net/problem=1

# Naive solution
def solve_naive(n):
    ans = 0
    for i in range(n):
        if i % 3 == 0 or i % 5 == 0:
            ans += i
    return ans

# Arithmetic Series solution
def solve_arith(n):
    n -= 1
    n_3 = n//3
    n_5 = n//5
    n_15 = n//15
    sn_3 = n_3/2 * (2*3 + (n_3 - 1)*3)
    sn_5 = n_5/2 * (2*5 + (n_5 - 1)*5)
    sn_15 = n_15/2 * (2*15 + (n_15 - 1)*15)
    ans2 = sn_3 + sn_5 - sn_15
    return int(ans2)

print(solve_naive(1000), solve_arith(1000))