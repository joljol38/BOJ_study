# 10250번 : ACM 호텔

T = int(input())

for i in range(T):
    H, W, N = map(int, input().split())
    floor = (N % H)
    room = (N // H) + 1
    if (floor == 0) :
        floor = H
        room -= 1
        
    print(floor*100 + room)
    