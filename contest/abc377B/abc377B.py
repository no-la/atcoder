N = 8
S = [list(input()) for _ in range(N)]

can_line = [True] * N
can_column = [True] * N
for i in range(N):
    for j in range(N):
        if S[i][j] == "#":
            can_line[i] = False
            can_column[j] = False

ans = 0
for i in range(N):
    for j in range(N):
        ans += can_line[i] and can_column[j]
print(ans)
