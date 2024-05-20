N = int(input())
A = [input().split() for _ in range(N)]


from collections import defaultdict
d = defaultdict(int)
for i in range(N):
    s, t = A[i]
    d[s] += 1
    d[t] += 1

for s, t in A:
    if d[s]>1 and d[t]>1:
        if d[s]==2 and s==t:
            continue
        print("No")
        exit()

print("Yes")
