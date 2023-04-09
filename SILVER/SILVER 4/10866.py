# 10866 덱
import sys

N = int(sys.stdin.readline())
from collections import deque
queue = deque()

for i in range(N):
    a = sys.stdin.readline().split()
    
    if (a[0] == "push_front"):
        queue.appendleft(a[1])
    
    elif (a[0] == "push_back"):
        queue.append(a[1])
    
    elif (a[0] == "pop_front"):
        if len(queue) == 0:
            print(-1)
        else :
            print(queue.popleft())
    
    elif (a[0] == "pop_back"):
        if len(queue) == 0:
            print(-1)
        else :
            print(queue.pop())
    
    elif (a[0] == "size"):
        print(len(queue))
        
    elif (a[0] == "empty"):
        if (len(queue) == 0):
            print(1)
        else :
            print(0)
    
    elif (a[0] == "front") :
        if (len(queue) == 0):
            print(-1)
        else : 
            print(queue[0])
            
    elif (a[0] == "back") :
        if (len(queue) == 0):
            print(-1)
        else :
            print(queue[-1])