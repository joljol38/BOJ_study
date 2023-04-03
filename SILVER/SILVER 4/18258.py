import sys
input = sys.stdin.readlines()
q = []
count = 0

for i in input:
    c = i.split()
    if c[0] == "push":
        q.append(c[1])
    elif c[0] == 'pop':
        if len(q) > count:
            print(q[count])
            count += 1
        else: print(-1)
    elif c[0] == 'size':
        print(len(q)-count)
    elif c[0] == 'empty':
        if len(q) == count :
            print(1)
            count = 0
            q = []
        else: print(0)
    elif c[0] == 'front':
        if len(q) > count: print(q[count])
        else: print(-1)
    elif c[0] == 'back':
        if len(q) > count: print(q[-1])
        else: print(-1)

    
