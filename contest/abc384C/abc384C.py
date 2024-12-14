A = list(map(int, input().split()))
S = "ABCDE"

ans = []
# bit全探索
N = 5
for i in range(1, 2**N):
    score = 0
    name = []
    for j in range(N):
        if not ((i >> j) & 1):
            continue
        score += A[j]
        name.append(S[j])
    ans.append((-score, "".join(name)))

ans.sort()
for score, name in ans:
    print(name)
