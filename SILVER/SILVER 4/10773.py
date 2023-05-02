N = int(input())
lst = []
for i in range(N):
    a = int(input())
    if (a != 0):
        lst.append(a)
    elif (a == 0):
        lst.pop()
print(sum(lst))