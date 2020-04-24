# Longest Collatz sequence
# https://projecteuler.net/problem=14

# Memoization approach (When you reach N, it will always take dp[N] steps)
dp = [-1 for i in range(1000001)]
ans = (1, 0)
for i in range(1, 1000000):
    steps = 0
    temp = i
    while temp != 1:
        steps += 1
        if temp%2:
            temp = temp * 3 + 1
        else:
            temp //= 2
        if temp <= 1000000:
            if dp[temp] != -1:
                steps += dp[temp]
                break
    dp[i] = steps
    if steps > ans[1]:
        ans = (i, steps)
print(ans[0])