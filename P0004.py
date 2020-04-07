# Largest palindrome product
# https://projecteuler.net/problem=4

ans = 0
for i in range(100, 1000):
    for j in range(100, 1000):
        p = i*j
        if p == int(str(p)[::-1]):
            ans = max(ans, p)
print(ans)