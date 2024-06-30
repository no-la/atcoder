N = int(input())
A = list(map(int, input().split()))
W = list(map(int, input().split()))


from collections import defaultdict
d = defaultdict(list)
for i in range(N):
    d[A[i]].append(W[i])

ans = 0
for k in d:
    d[k].sort()
    ans += sum(d[k][:-1])

print(ans)
