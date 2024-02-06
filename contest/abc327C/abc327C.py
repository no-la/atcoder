L = [list(map(int, input().split())) for _ in range(9)]

#行
for l in L:
    if len(set(l))<9:
        print("No")
        exit()

#列
for i in range(9):
    if len(set([l[i] for l in L]))<9:
        print("No")
        exit()

#3x3
for t in range(9):
    i, j = t//3, t%3
    nums = []
    for k in range(3):
        for l in range(3):
            nums.append(L[3*i+k][3*j+l])
    if len(set(nums))<9:
        print("No")
        exit()
print("Yes")