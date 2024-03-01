A = [list(map(int, input().split())) for _ in range(3)]
N = int(input())

D = [[False]*3 for _ in range(3)]
for _ in range(N):
    a = int(input())
    for i in range(3):
        for j in range(3):
            if A[i][j]==a:
                D[i][j] = True

for i in range(3):
    if all([D[i][j] for j in range(3)]):
        print("Yes")
        exit()
    if all([D[j][i] for j in range(3)]):
        print("Yes")
        exit()
        
for i in range(3):
    if D[i][i]==False:
        break
else:
    print("Yes")
    exit()
for i in range(3):
    if D[2-i][i]==False:
        break
else:
    print("Yes")
    exit()
print("No")