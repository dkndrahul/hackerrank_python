import itertools

length_of_N = int(input())
N = input().split()
K = input()

result = ()
if length_of_N == len(N):
    for i in itertools.combinations(N, int(K)):
        # print(*itertools.product(i, i))
        result.append(i)
print(result)