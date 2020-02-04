from itertools import combinations

A, B = input().split()
for i in range(1, int(B) + 1):
    for j in combinations(sorted(A), i):
        print("".join(j))
