n, m = input().split()
arr = list(map(int, input().split()))
seta = set(list(map(int, input().split())))
setb = set(list(map(int, input().split())))
happiness = 0
for i in arr:
    if i in seta:
        happiness += 1
    elif i in setb:
        happiness -= 1
print(happiness)