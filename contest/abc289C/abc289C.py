N, M = map(int, input().split())
A = []
for _ in range(M):
    C = int(input())
    A.append(list(map(lambda x: int(x) - 1, input().split())))

ans = 0
# bit全探索
for i in range(2**M):
    has = set()
    for j in range(M):
        if not ((i >> j) & 1):
            continue
        # A[j]を選ぶとき
        for a in A[j]:
            has.add(a)
    ans += len(has) == N

print(ans)
