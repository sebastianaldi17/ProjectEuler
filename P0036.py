# Double-base palindromes
# https://projecteuler.net/problem=36

ans = 0
for i in range(1000000):
    if str(i) == str(i)[::-1] and bin(i)[2:] == bin(i)[2:][::-1]:
        print(i)
        ans += i
print("Answer:",ans)