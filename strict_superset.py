a_set = set(map(int, input().split()))
test_cases = int(input())

for i in range(test_cases):
    other_sets = set(map(int, input().split()))
    j = 0
    if a_set.issuperset(other_sets) != True or len(a_set) == len(other_sets):
        print(False)
        break
else:
    print(True)
