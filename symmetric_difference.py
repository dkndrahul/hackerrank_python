first_number = int(input())
first_set = set(list(map(int, input().split())))
second_number = int(input())
second_set = set(list(map(int, input().split())))
final_sorted = sorted(set((first_set.difference(second_set).union(second_set.difference(first_set)))))
for i in final_sorted:
    print(i)
