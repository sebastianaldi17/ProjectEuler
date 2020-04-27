# Digit cancelling fractions
# https://projecteuler.net/problem=33

from math import gcd

frac = []

for a in range(10, 100):
    for b in range(a+1, 100):
        if a%10 == 0 and b%10 == 0: continue
        g = gcd(a, b)
        sa, sb = a//g, b//g
        ca, cb = str(a), str(b)
        # THIS IS VERY LONG, NOT IN COMPLIANCE WITH DRY
        if ca[0] == cb[0]:
            ta = int(ca[1])
            tb = int(cb[1])
            g2 = gcd(ta, tb)
            if ta//g2 == sa and tb//g2 == sb:
                frac.append([a, b])
        elif ca[0] == cb[1]:
            ta = int(ca[1])
            tb = int(cb[0])
            g2 = gcd(ta, tb)
            if ta//g2 == sa and tb//g2 == sb:
                frac.append([a, b])
        elif ca[1] == cb[0]:
            ta = int(ca[0])
            tb = int(cb[1])
            g2 = gcd(ta, tb)
            if ta//g2 == sa and tb//g2 == sb:
                frac.append([a, b])
        elif ca[1] == cb[1]:
            ta = int(ca[0])
            tb = int(cb[0])
            g2 = gcd(ta, tb)
            if ta//g2 == sa and tb//g2 == sb:
                frac.append([a, b])
top, bot = 1, 1
for x in frac:
    top *= x[0]
    bot *= x[1]
print(bot // gcd(top, bot))