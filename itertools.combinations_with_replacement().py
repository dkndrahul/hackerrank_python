from itertools import combinations_with_replacement

A, B = input().split()
for i in combinations_with_replacement(sorted(A), int(B)):
    print("".join(i))
