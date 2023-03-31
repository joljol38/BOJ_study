# 2740번 : 행렬 곱셈

# numpy 사용
import numpy as np

N, M = map(int, input().split())
A = [] 
B = []
for i in range(N):
    A.append(list(map(int, input().split())))
M, K = map(int, input().split())
for j in range(M) :
    B.append(list(map(int, input().split())))
print(A)
print(B)
a = np.array(A)
b = np.array(B)
for x in (a@b):
    print(*x, sep = ' ')
    
# numpy 사용 x
N, M = map(int, input().split())
A = [] 
B = []
for i in range(N):
    A.append(list(map(int, input().split())))
M, K = map(int, input().split())
for j in range(M):
    B.append(list(map(int, input().split())))

# numpy를 사용하지 않고 행렬 곱 구하기
result = [[0] * K for _ in range(N)]
for i in range(N):
    for j in range(K):
        for k in range(M):
            result[i][j] += A[i][k] * B[k][j]

# 결과 출력
for i in range(N):
    print(' '.join(map(str, result[i])))