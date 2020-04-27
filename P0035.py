# Circular primes
# https://projecteuler.net/problem=35

prime = [True for i in range(1000010)]
prime[0] = prime[1] = False
p = 2
while p <= 1000000:
    if prime[p]:
        for i in range(p * 2, 1000001, p):
            prime[i] = False
    p += 1
circ = []
for i in range(2, 1000000):
    if prime[i]:
        temp = i
        digits = len(str(i))
        for j in range(digits):
            if not prime[temp]: break
            temp = temp // 10 + (temp % 10)*(10**(digits-1))
        else: circ.append(i)
        # circle time
print(len(circ))