# Champernowne's Constant
# https://projecteuler.net/problem=40

from time import time

start = time()
s = ""
# 1.000.000 characters divided into _ digit numbers...
# 1 = 9
# 2 = 99
# 3 = 999
# 4 = 9999
# 5 = 99999
# 6 = give or take 90000 6 digit numbers
for i in range(1, 190000):
    s += str(i)
print(eval(s[0]+"*"+s[9]+"*"+s[99]+"*"+s[999]+"*"+s[9999]+"*"+s[99999]+"*"+s[999999]))
print("Calculated in", time() - start, "seconds")