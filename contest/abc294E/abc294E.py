from collections import deque

L, N, M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(M)]

q = []
count = 0
for v, l in A:
    q.append((count, count + l, 0, v))
    count += l
count = 0
for v, l in B:
    q.append((count, count + l, 1, v))
    count += l


q.sort()
q = deque(q)

ans = 0
right, left, value = [[0, 0] for _ in range(3)]
while q:
    r, l, i, v = q.popleft()
    right[i] = r
    left[i] = l
    value[i] = v

    j = i ^ 1
    if value[0] == value[1]:
        ans += max(0, min(*left) - max(*right))

print(ans)
