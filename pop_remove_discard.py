n = int(input())
s = set(map(int, input().split()))
no_commands = int(input())
for i in range(no_commands):
    try:
        command = list(map(str, input().split()))
        if command[0] == 'pop':
            s.pop()
        elif command[0] == 'remove':
            s.remove(int(command[1]))
        elif command[0] == 'discard':
            s.discard(int(command[1]))
    except KeyError:
        continue
print(sum(s))