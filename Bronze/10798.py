# 10798번 : 세로 읽기
arr = []
for i in range(5):
    arr.append(input().split())
# print(list(arr))
arr = [list(word[0]) for word in arr]
max_len = max([len(l) for l in arr])
new_arr = [l + ['']*(max_len-len(l)) for l in arr]
result = ""
for col in zip(*new_arr):
    result += "".join(col)
    
    
print(result)