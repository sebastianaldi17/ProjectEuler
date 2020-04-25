# Lexicographic permutations
# https://projecteuler.net/problem=24

from itertools import permutations

# This only takes about a second, so I guess the point of the problem is to generate your own permutation method?
print(''.join(map(str, list(permutations([i for i in range(10)]))[999999])))