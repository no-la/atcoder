N = int(input())

# 二分探索で行、列をそれぞれ絞る
ans = [None] * 2
for i in range(2):
    l, r = 1, N + 1
    while l < r - 1:  # [l, r]行（列）のどこかに置ける
        c = (l + r) // 2
        print(f"? {c} {r-1} 1 {N}" if i == 0 else f"? 1 {N} {c} {r-1}")
        count = int(input())
        if count < r - c:
            l = c
        else:
            r = c
    ans[i] = l

print("!", *ans)
