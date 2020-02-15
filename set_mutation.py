num_a_elements = int(input())
a_elements = set(map(int, input().split()))
no_other_sets = int(input())
for i in range(no_other_sets):
    mutation, number = input().split()
    other_set = set(map(int, input().split()))
    if mutation == 'update':
        a_elements.update(other_set)
    elif mutation == 'intersection_update':
        a_elements.intersection_update(other_set)
    elif mutation == 'difference_update':
        a_elements.difference_update(other_set)
    elif mutation == 'symmetric_difference_update':
        a_elements.symmetric_difference_update(other_set)
print(sum(a_elements))
