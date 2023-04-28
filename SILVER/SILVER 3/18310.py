N = int(input())
dis = list(map(int, input().split()))
dis.sort()

print(dis[(N-1) // 2])