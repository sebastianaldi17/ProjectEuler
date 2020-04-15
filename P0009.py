# Special Pythagorean Triplet
# https://projecteuler.net/problem=9

from math import floor, ceil, sqrt

triples = []
for i in range(1, 1000):
    for j in range(i+1, 1000):
        res = i*i + j*j
        root = int(sqrt(res))
        if root*root == res:
            triples.append([i, j, root])
for x in triples:
    if x[0] + x[1] + x[2] == 1000:
        print(x[0] * x[1] * x[2])