from itertools import combinations
test, number = input().split()
for i in range(int(number)):
    # # print(*combinations(sorted(test), int(number)))
    # print(*["".join(combinations(i, int(number)))])
    print(*["".join(combinations(sorted(test), i))])

