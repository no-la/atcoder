N = int(input())
S = [input() for _ in range(N)]

count = 0
ans = None
for s in S:
    temp = S.count(s)
    if count < temp:
        ans = s
        count = temp
print(ans)