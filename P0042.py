# Coded Triangle Numbers
# https://projecteuler.net/problem=42

f = open("P0042.txt", "r")
a = []
for x in f:
    a.append(x.replace('"', '').split(","))
a = a[0]

# print(max(a, key=len))
# Longest word is ADMINISTRATION
# Let's assume the biggest value is Z*len('ADMINISTRATION') [14 Z's]

tri = [False for i in range(14*26 + 1)]
n = 1
while 0.5 * n * (n+1) <= 14*26:
    tri[int(0.5 * n * (n+1))] = True
    n += 1
ans = 0
for x in a:
    temp = 0
    for letter in x:
        temp += ord(letter) - 64
    if tri[temp]:
        ans += 1
print(ans)