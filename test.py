# # Python program to print all permutations with
# # duplicates allowed
#
# def toString(List):
#     return ''.join(List)
#
#
# # Function to print permutations of string
# # This function takes three parameters:
# # 1. String
# # 2. Starting index of the string
# # 3. Ending index of the string.
# def permute(a, l, r):
#     if l == r:
#         print
#         toString(a)
#     else:
#         print(l)
#         print(r)
#         for i in range(l, r + 1):
#             a[l], a[i] = a[i], a[l]
#             permute(a, l + 1, r)
#             a[l], a[i] = a[i], a[l]  # backtrack
#
#
# # Driver program to test the above function
# string = "ABC"
# n = len(string)
# a = list(string)
#
# # results = permute(a, 0, n - 1)
# print(permute(a, 0, n - 1))


# def permutations(string, step = 0):
#     if step == len(string):
#         # we've gotten to the end, print the permutation
#         print("".join(string))
#         for i in range(step, len(string)):
#             # copy the string (store as array)
#             string_copy = [c for c in string]
#             string_copy[step], string_copy[i] =string_copy[i], string_copy[step]
#             permutations(string_copy, step + 1)
#
# print (permutations ('one'))


from itertools import permutations
print([''.join(p) for p in permutations('Aabb')])
