# Number spiral diagonals
# https://projecteuler.net/problem=28

memo = [0 for i in range(1002)]
last = [0 for i in range(1002)]
memo[1] = 1
last[1] = 1
for i in range(3, 1002, 2):
    memo[i] = memo[i-2] + 2*(2*(last[i-2] + i-1) + 3*(i-1))
    last[i] = last[i-2] + i-1 + 3*(i-1)
print(memo[1001])