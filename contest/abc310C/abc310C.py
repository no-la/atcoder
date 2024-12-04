N = int(input())
S = [input() for _ in range(N)]

ans = set()
for s in S:
    if s not in ans and s[::-1] not in ans:
        ans.add(s)

print(len(ans))
