N = int(input())
A = list(map(int, input().split()))
A.sort()

# 被りを後ろに回す
count = 0
for i in range(N - 1):
    count += A[i] == A[i + 1]


from collections import deque

d = deque(sorted(set(A)) + [N + 1] * count)
ans = 0
while d:
    if ans + 1 == d[0]:
        d.popleft()
        ans += 1
    else:
        if len(d) == 1:
            break
        while len(d) >= 2 and ans + 1 < d[0]:
            d.pop()
            d.pop()
            ans += 1

print(ans)
