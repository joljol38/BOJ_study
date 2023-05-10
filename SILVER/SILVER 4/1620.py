import sys
N, M = map(int, input().split())

dict_name = {}
dict_num = {}

for i in range(N):
    name = sys.stdin.readline().strip()
    dict_num[i] = name
    dict_name[name] = i

for x in range(M):
    command = sys.stdin.readline().strip()
    if command.isdigit() == True:
        print(dict_num[int(command)-1])
    else:
        print(dict_name[command]+1)