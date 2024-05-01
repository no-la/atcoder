N = int(input())
A = [list(map(int, input().split())) for _ in range(N-1)]


for i in range(N-1):
    t = A[i][1]
    for j in range(i+1, N):
        # j-1からjへ
        # print("departure from", j-1, "to", j, "for", t, "~", t+A[j-1][0])
        t += A[j-1][0]
        if j==N-1:
            pass
        elif t<=A[j][1]:
            t = A[j][1]
        else:
            t = -(-(t-A[j][1])//A[j][2])*A[j][2] + A[j][1]
    print(t)

print(0)