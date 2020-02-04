from itertools import permutations

test, number = input().split()
print(*["".join(i) for i in permutations(sorted(test), int(number))], sep="\n")
