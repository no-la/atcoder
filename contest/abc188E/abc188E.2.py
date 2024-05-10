N, M = map(int, input().split())
A = list(map(int, input().split()))


from collections import defaultdict
d = defaultdict(list)
for _ in range(M):
    x, y = map(lambda a: int(a)-1, input().split())
    d[x].append(y)

# 各町の、「そこにたどり着くまでの最安値」が分かればいい
mins = [a for a in A]
changed = [False]*N
for i in range(N): # X<Y という制約があるので、iを昇順に調べて行けばいい
    m = min(mins[i], A[i])
    for j in d[i]:
        if mins[j]>m or not changed[j]:
            changed[j] = True
            mins[j] = m
# print(A)
# print(mins)
# print(changed)
print(max([A[i]-mins[i] for i in range(N) if changed[i]]))
