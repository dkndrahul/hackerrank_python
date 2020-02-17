group_size = int(input())
room_number_list = list(map(int, input().split()))
room_set = set(room_number_list)
print(((sum(room_set)*group_size)-(sum(room_number_list)))//(group_size-1))
