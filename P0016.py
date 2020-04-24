# Power digit sum
# https://projecteuler.net/problem=16

# 2^1000? LAUGHS IN PYTHON
q = 2**1000
ans = 0
while q > 0:
    ans += q%10
    q //= 10
print(ans)

# Solving without utilization of bigint
n = [1]
for i in range(1000):
    carry = 0
    for j in range(len(n)):
        n[j] *= 2
        n[j] += carry
        if n[j] >= 10:
            carry = int(str(n[j])[0])
            n[j] = int(str(n[j])[1])
        else: carry = 0
        if j == len(n) - 1 and carry > 0:
            n.append(carry)
print(sum(n))

# Python one liner time :v
print(sum(map(int, list(str(2**1000)))))
        