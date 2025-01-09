N, L = map(int, input().split())
K = int(input())
A = [0] + list(map(int, input().split())) + [L]

# print(A)

# 決め打ち二分探索っぽい
l, r = 0, L
while l < r - 1:  # [l, r)は答えになり得る
    c = (l + r) // 2
    cutpos = [0]
    for i in range(1, len(A)):
        if A[i] - A[cutpos[-1]] >= c:
            cutpos.append(i)
    # print(l, c, r, cutpos)
    if len(cutpos) >= K + 2:
        l = c
    else:
        r = c

print(l)
