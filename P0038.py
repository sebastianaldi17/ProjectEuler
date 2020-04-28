# Pandigital multiples
# https://projecteuler.net/problem=38

ans = 918273645

def is_19_pandigital(n):
    if '0' in str(n) or len(str(n)) != 9 or len(set(str(n))) != 9: return False
    else: return True

for i in range(11, 10000):
    s = ''
    for j in range(1, 10):
        s += str(i*j)
        if len(s) >= 9: break
    if is_19_pandigital(int(s)):
        ans = max(ans, int(s))
print(ans)