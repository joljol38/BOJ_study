# 2577번 : 숫자의 개수

a = int(input())
b = int(input())
c = int(input())

# print(a*b*c)
# print(str(a*b*c))
# print(len(str(a*b*c)))
num = str(a*b*c)

lst = [0 for i in range(10)]

for i in range(len(num)):
    if (num[i] == "0"):
        lst[0] += 1
    elif (num[i] == "1"):
        lst[1] += 1
    elif (num[i] == "2"):
        lst[2] += 1
    elif (num[i] == "3"):
        lst[3] += 1
    elif (num[i] == "4"):
        lst[4] += 1
    elif (num[i] == "5"):
        lst[5] += 1
    elif (num[i] == "6"):
        lst[6] += 1
    elif (num[i] == "7"):
        lst[7] += 1
    elif (num[i] == "8"):
        lst[8] += 1
    else :
        lst[9] += 1
print(*lst, sep = "\n")