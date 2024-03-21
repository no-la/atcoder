N = int(input())
A = list(map(int, input().split()))
Q = int(input())

from collections import defaultdict
d = defaultdict(int)
for a in A:
    d[a] += 1

ans = sum(A)
for _ in range(Q):
    b, c = map(int, input().split())
    ans -= b*d[b]
    ans += c*d[b]
    
    print(ans)
    
    d[c] += d[b]
    d[b] = 0