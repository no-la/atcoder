N = int(input())
A = []
B = []
sa = 0
for _ in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)
    sa += a

# N-1人の肩の高さの総和 + 残り1人の頭の高さ

ans = 0
for i in range(N):
    ans = max(ans, sa - A[i] + B[i])

print(ans)
