# 1000 digit Fibonacci number
# https://projecteuler.net/problem=25

# Again, using pyhon feels like cheating... But what the hey

i, a, b = 2, 1, 1
while True:
    i += 1
    if len(str(a+b)) == 1000:
        print(i)
        break
    a, b = b, a+b