# Counting Sundays
# https://projecteuler.net/problem=19

from datetime import datetime, timedelta
# 365 mod 7 = 1, 366 mod 7 = 1
ans = 0
x = datetime(1901, 1, 6)
while x.year <= 2000:
    x += timedelta(days=7)
    if x.day == 1: ans += 1
print(ans)