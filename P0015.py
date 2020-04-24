# Lattice paths
# https://projecteuler.net/problem=15
lim = 20
dp = [[0 for i in range(lim+1)] for i in range(lim+1)]
def rec(x, y):
    global dp
    if x > lim or y > lim: return 0
    if dp[x][y] > 0: return dp[x][y]
    if x == lim and y == lim:
        return 1
    dp[x][y] = rec(x+1, y) + rec(x, y+1)
    return dp[x][y]

rec(0, 0)
print(dp[0][0])