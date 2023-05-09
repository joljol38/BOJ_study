import sys

M = int(input())
s = set()

for i in range(M):
    com = sys.stdin.readline().strip().split()
    if len(com) == 1:
        if (com[0] == "all"):
            s = set([i for i in range(1, 21)])
        else:
            s = set()
    else:
        x = int(com[1])
        
        if (com[0] == "add"):
            s.add(x)
        elif (com[0] == "remove"):
            s.discard(x)
        elif (com[0] == "check"):
            if (x in s):
                print(1)
            else:
                print(0)
        elif (com[0] == "toggle"):
            if (x in s):
                s.discard(x)
            else:
                s.add(x)