no_stamps = int(input())
result = set()
for i in range(no_stamps):
    country_stamp = input()
    result.add(country_stamp)
print(len(result))