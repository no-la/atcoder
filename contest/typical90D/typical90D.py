H, W = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(H)]

sum_column = [sum([A[i][j] for i in range(H)]) for j in range(W)]
sum_line = [sum(A[i]) for i in range(H)]

for i in range(H):
    print(*[sum_column[j] + sum_line[i] - A[i][j] for j in range(W)])
