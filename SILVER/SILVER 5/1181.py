# 1181번 : 단어 정렬

N = int(input())
voca = []
word = {}

for i in range(N):
    v = str(input())
    voca.append(v)
# print(voca)

svoca = sorted(voca)

for x in svoca:
    word[x] = len(x)
# print(word)

val = sorted(word, key = lambda x:word[x])
print(*val, sep = "\n")