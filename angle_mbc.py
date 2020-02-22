from math import degrees, atan2
length_ab = int(input())
length_bc = int(input())
print(str(int(round(degrees(atan2(length_ab, length_bc))))) + "°")
