# 9012번 : 괄호

N = int(input())

for i in range(N):
    s = input()
    string = list(s)
    # print(string)
    count = 0
    for p in string:
        if (p == "("):
            count += 1
        elif (p == ")"):
            count -= 1
        if count < 0:
            print("NO")
            break
    # print(count)
    if (count == 0):
        print("YES")
    elif (count > 0) :
        print("NO")