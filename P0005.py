# Smallest multiple
# https://projecteuler.net/problem=5
from math import gcd
a = [i for i in range(2, 21)]
lcm = 1
for i in a:
  lcm = lcm*i//gcd(lcm, i)
print(lcm)