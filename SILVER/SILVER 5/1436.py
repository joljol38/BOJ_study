N = int(input())
count = 0
i = 0
while count != N:
    i += 1
    if str(i).count("666") > 0:
        count += 1
print(i) 