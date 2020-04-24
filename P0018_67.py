# Maximum path sum
# https://projecteuler.net/problem=18  [Easy version]
# https://projecteuler.net/problem=67  [Hard version]

f = open("P0018.txt", "r")
arr = []
for x in f:
    arr.append(list(map(int, x.split())))
arr.reverse()
for i in range(1, len(arr)):
    for j in range(len(arr[i])):
        arr[i][j] = max(arr[i][j] + arr[i-1][j], arr[i][j] + arr[i-1][j+1])
arr.reverse()
print(arr[0])