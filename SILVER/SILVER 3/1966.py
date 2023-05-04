from collections import deque

T = int(input())

for i in range(T):
    N, M = map(int, input().split())
    Q = deque(list(map(int, input().split())))
    cnt = 0
    
    while Q:
        mx = max(Q)
        front = Q.popleft()
        M -= 1
        
        if mx == front:
            cnt += 1
            if M < 0:
                print(cnt)
                break
        else:
            Q.append(front)
            if M < 0:
                M = len(Q)-1