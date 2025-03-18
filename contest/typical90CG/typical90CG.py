import sys

input = lambda: sys.stdin.readline().rstrip()
K = int(input())
INF = 100000000

ans = 0
for a in range(1, INF):
    if a * a * a > K:
        break
    for b in range(a, INF):
        if a * b * b > K:
            break
        ab = a * b

        if K % ab != 0:
            continue
        if K // ab < b:
            continue

        ans += 1

print(ans)
