N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

# iを選らぶ -> +sum(A[i])
# iを選ばない -> -A[i][0]


# 全部選ばないとする
now = sum([-A[i][0] for i in range(N)])

# iを選んだときの増分
delta = [2*A[i][0]+A[i][1] for i in range(N)]
delta.sort()
for i in range(N):
    now += delta[-1-i]
    if now>0:
        print(i+1)
        exit()    

