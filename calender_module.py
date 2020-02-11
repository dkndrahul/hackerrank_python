import calendar

mm, dd, yyyy = input().split()
result = calendar.weekday(int(yyyy), int(mm), int(dd))
resultweek = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY", "SUNDAY"]
print(resultweek[result])

