"""「連続するとは限らない」の見落とし"""

import sys

input = lambda: sys.stdin.readline().rstrip()
H, W = map(int, input().split())
P = [list(map(int, input().split())) for _ in range(H)]

# Hは全探索
# あとはしゃくとり


def f(t, b, j, x):
    """P[t:b][j] == x"""
    for i in range(t, b):
        if P[i][j] != x:
            return False
    return True


# 重複なし組み合わせ O(nCk)
import itertools

ans = 1
for l in itertools.combinations(range(H + 1), 2):
    t, b = sorted(l)
    # 尺取り法
    right = 0
    for left in range(W):
        while right < W and f(t, b, right, P[t][left]):
            right += 1
        ans = max(ans, (b - t) * (right - left))
        if left == right:  # [left, right)が空集合なので'temp=初期値'になっているはず
            right += 1

print(ans)
