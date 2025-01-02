N = int(input())
ans = set()
for _ in range(N):
    a, b, c, d = map(int, input().split())
    for i in range(a, b):
        for j in range(c, d):
            ans.add((i, j))

print(len(ans))
