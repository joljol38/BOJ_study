# 11866번 : 요세푸스 문제 0
from collections import deque

N, K = map(int, input().split())
queue = deque()
answer = []

for i in range(N):
    queue.append(i+1)
# print(queue)

print("<", end = "")

while True:
    if (len(queue) == 0):
        break
    
    for i in range(K-1):
        queue.append(queue.popleft())
    answer.append(queue.popleft())
    
for i in range(len(answer)):
    if (i == len(answer)-1):
        print(answer[i], end = ">")
    else :
        print(answer[i], end = ", ")
    