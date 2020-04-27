# Pandigital products
# https://projecteuler.net/problem=32

ans = set()

for a in range(1, 10000):
    b = 0
    res = str(a) + str(b) + str(a*b)
    while(len(res)) <= 9:
        b += 1
        res = str(a) + str(b) + str(a*b)
        if '0' in res: continue
        if len(set(res)) == 9 and len(res) == 9:
            ans.add(a*b)

print(sum(ans))
