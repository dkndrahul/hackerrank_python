import itertools

length_of_N = int(input())
N = input().split()
K = input()

if length_of_N == len(N):
    for i in itertools.combinations(N, int(K)):
        print((",".join(i)))