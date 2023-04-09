# 2164번 : 카드2

from collections import deque
N = int(input())
queue = deque()
for i in range(N):
    queue.append(i+1)
# print(queue)

for i in range(N-1):
    queue.popleft()
    queue.append(queue.popleft())

print(*queue)