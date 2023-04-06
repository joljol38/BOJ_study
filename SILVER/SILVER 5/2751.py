# 2751번 : 수 정렬하기2 (PyPy3로 실행)

N = int(input())
n = []
for i in range(N):
    a = int(input())
    n.append(a)


print(*sorted(n), sep = '\n')