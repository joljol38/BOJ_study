# 25206번 : 너의 평점은

score = {
    'A+' : 4.5,
    'A0' : 4.0,
    'B+' : 3.5,
    'B0' : 3.0,
    'C+' : 2.5,
    'C0' : 2.0,
    'D+' : 1.5,
    'D0' : 1.0,
    'F' : 0.0
}

grade = 0
count = 0
for i in range(20):
    sj, sr, gr = input().split()
    if (gr == 'P'):
        count += 0
        grade += 0
    else :
        count += float(sr)
        grade += (float(sr) * score[gr])
    # print(sj)
    # print(sr)
    # print(gr)
    
    # print(count)
    # print(grade)
print('%.6f' % (grade / count))