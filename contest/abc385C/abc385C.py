N = int(input())
H = list(map(int, input().split()))
M = max(H)

# 高さごとに、
# 幅の全探索＋尺取り

# 高さごとの尺取りで O(N)
# 幅の全探索で O(N)

towers = [[] for _ in range(M + 1)]
for i, h in enumerate(H):
    towers[h].append(i)

ans = 1
for l in towers:
    if not l:
        continue
    if len(l) == 1:
        ans = max(ans, 1)
        continue
    for delta in range(1, N):
        # 尺取り法
        right = 0
        for left in range(len(l)):
            while right < len(l) and l[right] - l[left] == delta * (right - left):
                right += 1
            # [left, right) が条件を満たす
            print(l, delta, left, right)
            ans = max(ans, right - left)
            if left == right:
                right += 1

print(ans)
