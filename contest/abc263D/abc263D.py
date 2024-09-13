N, L, R = map(int, input().split())
A = list(map(int, input().split()))

d = [0]*(N+1)
# d[i]: sum(A[:i])
for i in range(N):
    d[i+1] = d[i]+A[i]


# 全探索
ans = d[-1]
ans_x = 0
# L
for x in range(N+1):
    # print(A[:x], "to", L, "->", d[-1]-d[x]+i*L)
    if ans>d[-1]-d[x]+x*L:
        ans = d[-1]-d[x]+x*L
        ans_x = x

B = [L if i<ans_x else A[i] for i in range(N)]
# print(ans, A)

e = [0]*(N+1)
for i in range(N):
    e[i+1] = e[i]+B[i]

ans_y = 0
# R
for y in range(N+1):
    if ans>e[N-y]+y*R:
        ans = e[N-y]+y*R
        ans_y = y
# print(f"{ans_x=}, {ans_y=}", e[N-ans_y], ans_y*R)

# Lを使わないパターン
for y in range(N+1):
    ans = min(ans, d[N-y]+y*R)

print(ans)
