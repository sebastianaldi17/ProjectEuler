f = open("P0022.txt", "r")
a = []
for x in f:
    a.append(x.replace('"', '').split(","))
a = a[0]
a.sort()
ans = 0
for i in range(len(a)):
    temp = 0
    for x in a[i]:
        temp += ord(x) - 64
    ans += temp * (i+1)
print(ans)