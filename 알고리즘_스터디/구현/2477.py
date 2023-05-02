N = int(input())

height = []
width = []
tot = []

for i in range(6):
    size = list(map(int, input().split()))
    if size[0] == 1 or size[0] == 2:  
        width.append(size[1])
        tot.append(size[1])
    else:
        height.append(size[1])
        tot.append(size[1])

bigsize = max(height) * max(width)

maxhidx = tot.index(max(height))
maxwidx = tot.index(max(width))

box1 = abs(tot[maxhidx-1] - tot[(maxhidx-5 if maxhidx == 5 else maxhidx +1)])
box2 = abs(tot[maxwidx-1] - tot[(maxwidx-5 if maxwidx == 5 else maxwidx +1)])
total = bigsize - (box1 * box2)

print(total * N)