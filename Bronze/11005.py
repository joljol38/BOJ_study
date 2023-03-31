# 11005번 : 진법 변환 2
import sys

system = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
N, B = map(int, input().split())
answer = ''

while N != 0:
    answer += str(system[N % B])
    N //= B

print(answer[::-1]) 

num = {
    'A' : 10,
    'B' : 11,
    'C' : 12,
    'D' : 13,
    'E' : 14,
    'F' : 15,
    'G' : 16,
    'H' : 17,
    'I' : 18,
    'J' : 19,
    'K' : 20,
    'L' : 21,
    'M' : 22,
    'N' : 23,
    'O' : 24,
    'P' : 25,
    'Q' : 26,
    'R' : 27,
    'S' : 28,
    'T' : 29,
    'U' : 30,
    'V' : 31,
    'W' : 32,
    'X' : 33,
    'Y' : 34,
    'Z' : 35}
reverse_num = dict(map(reversed, num.items()))

def change(N, B):
    number = ''
    while N:
        number = str(N % B) + number
        N //= B
    return number

N, B = map(int, input().split())
nn = change(N, B)
# print(nn)

result = []
for i in range(0, len(nn), 2):
    result.append(nn[i:i+2]) 
# print(result)

result2 = []
for key, value in reverse_num.items():
    for i in range(len(result)):
        if key == int(result[i]):
            result2.append(value)

print(*result2, sep = '')