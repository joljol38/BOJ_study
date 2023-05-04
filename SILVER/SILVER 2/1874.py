N = int(input())

stack = []
ans = []
find = True
last = 1

for i in range(N):
    num = int(input())
    while (last <= num):
        stack.append(last)
        ans.append("+")
        last += 1
    if stack[-1] == num:
        stack.pop()
        ans.append("-")
    else:
        find = False
if not find:
    print("NO")
else:
    for i in ans:
        print(i)