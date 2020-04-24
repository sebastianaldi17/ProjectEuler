# Factorial digit sum
# https://projecteuler.net/problem=20

# LAUGHS IN PYTHON
n, ans = 1, 0
for i in range(1, 101): n *= i
while n > 0:
    ans += n%10
    n //= 10
print(ans)
