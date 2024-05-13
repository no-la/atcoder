N, K, X = map(int, input().split())
A = list(map(int, input().split()))

A.sort()

remain = []
ans = 0
k = K
for a in A[::-1]:
    c = min(k, a//X)
    k -= c
    v = a-c*X
    remain.append(v)
    ans += v

remain.sort(reverse=True)

print(ans-sum(remain[:k]))

