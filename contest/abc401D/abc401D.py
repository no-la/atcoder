import sys

input = lambda: sys.stdin.readline().rstrip()
N, K = map(int, input().split())
S = input()

ans = [None] * N

# o の両端は .
# ??????? は偶数個ならそのまま
# 奇数個ならそのままか、ちょうど良ければきまる

for i in range(N):
    if ans[i] is not None:
        continue
    if S[i] == "?":
        continue

    ans[i] = S[i]
    if S[i] == "o":
        if i - 1 > 0 and S[i - 1] == "?":
            ans[i - 1] = "."
        if i + 1 < N and S[i + 1] == "?":
            ans[i + 1] = "."

        K -= 1

# print(*ans, sep="")

d = []  # 連続する ? の長さのlist
count = 0  # 自由度の和
i = 0
while i < N:
    if ans[i] is not None:
        i += 1
        continue
    d.append(0)
    while i < N and ans[i] is None:
        d[-1] += 1
        i += 1

    count += (d[-1] + 1) // 2

# print(d)

if count > K:
    to = "?" if K > 0 else "."
    print(*[a if a is not None else to for a in ans], sep="")
    exit()

di = 0
i = 0
while i < N:
    if ans[i] is not None:
        i += 1
        continue
    l = 0
    while i < N and ans[i] is None:
        if d[di] % 2 == 0:
            ans[i] = "?"
        else:
            if l % 2 == 0:
                ans[i] = "o"
            else:
                ans[i] = "."
        l += 1
        i += 1
    di += 1

print(*ans, sep="")
# print(d, count, K)
