N = int(input())
A = [input() for _ in range(N)]


for i in range(N):
    for j in range(N):
        if i==j:
            continue
        if A[i][j]==A[j][i] and A[i][j]=="D":
            continue
        if (A[i][j], A[j][i]) in [("W", "L"), ("L", "W")]:
            continue
        
        print("incorrect")
        exit()

print("correct")
