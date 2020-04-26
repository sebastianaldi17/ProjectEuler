# Coin sums
# https://projecteuler.net/problem=31

currency = [1, 2, 5, 10, 20, 50, 100, 200]
dp = [[0 for i in range(201)] for i in range(201)]

def solve(n, i):
    if i > len(currency) - 1: return 0
    if n < 0: return 0
    if dp[n][i] > 0: return dp[n][i]
    if n == 0: return 1
    dp[n][i] = solve(n - currency[i], i) + solve(n, i+1)
    return dp[n][i]

solve(200, 0)
print(dp[200][0])
