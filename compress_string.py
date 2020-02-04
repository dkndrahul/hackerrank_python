from itertools import groupby

A = input()
print(*[(len(list(value)), int(key)) for key, value in groupby(A)])
