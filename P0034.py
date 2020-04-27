# Digit factorials
# https://projecteuler.net/problem=34

def fac(n):
    if n == 0: return 1
    res = 1
    for i in range(1, n+1):
        res *= i
    return res

arr = [fac(i) for i in range(10)]
ans = 0

# Is there a more valid lower bound? 2 million is just a wild guess
# Since 9! = 362.880, and 7 * 9! = 2.540.160, which is way smaller than 9.999.999
for i in range(10, 2000000):
    temp = i
    digsum = 0
    while temp > 0:
        digsum += arr[temp%10]
        temp //= 10
    if digsum == i:
        ans += i
print(ans)