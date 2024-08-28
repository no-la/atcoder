import sys
input = sys.stdin.readline

Q = int(input())
MOD = 998244353

from collections import deque
S = deque([1])
ans = 1
for _ in range(Q):
    l = list(map(int, input().split()))
    if l[0]==1:
        x = l[1]
        S.append(x)
        ans *= 10
        ans += x
        ans %= MOD
    elif l[0]==2:
        x = S.popleft()
        ans -= x*pow(10, len(S), MOD)
        ans %= MOD
    else:
        print(ans)
