# 11050번 : 이항 계수1

def factorial(n):
    ans = 1
    for i in range(2, n+1):
        ans *= i
    return ans

N, k = map(int, input().split())

print(factorial(N)//(factorial(N-k)*factorial(k)))