N, M = map(int, input().split())
S = [input() for _ in range(N)]

ans = set()
for i in range(N):
    for j in range(i + 1, N):
        for k in range(M):
            if S[i][k] == "x" and S[j][k] == "x":
                break
        else:
            ans.add((i, j))

print(len(ans))
# print(ans)
