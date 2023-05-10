import sys
input = sys.stdin.readline
N, M = map(int, input().split())
psw = {}

for _ in range(N):
    site, pswd = input().split()
    psw[site] = pswd
    
for _ in range(M):
    print(psw[input().rstrip()])