# Digit fifth powers
# https://projecteuler.net/problem=30

ans = 0
for i in range(2, 9**6):
  temp = i
  digsum = 0
  while temp > 0:
    digsum += (temp%10)**5
    temp //= 10
  if i == digsum: ans += i
print(ans)