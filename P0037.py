# Truncatable primes
# https://projecteuler.net/problem=37

prime = [True for i in range(1000001)]
prime[0] = prime[1] = False
p = 2
while p <= 1000000:
    if prime[p]:
        for i in range(p * 2, 1000001, p):
            prime[i] = False
    p += 1

cnt, ans = 0, 0
check = 23
while cnt < 11:
    temp = check
    include = True
    while temp > 0:
        if prime[temp] == False:
            include = False
            break
        temp //= 10
    temp = check
    while temp > 0:
        if prime[temp] == False:
            include = False
            break
        if len(str(temp)[1:]) > 0: temp = int(str(temp)[1:])
        else: break
    if include:
        cnt += 1
        ans += check
    check += 2
print(ans)