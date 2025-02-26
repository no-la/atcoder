import sys

input = lambda: sys.stdin.readline().rstrip()


class SegTree:
    def __init__(self, num, e_factory, operand=max):
        """
        parameter
            num : 要素数
            e_factory : 単位元を生成する関数
            operand : 子ノードの値から親ノードの値を作る関数
        """
        # self.tree[i+self.offset]:要素iのみの区間の値
        self.offset = 1 << (num - 1).bit_length()
        self.tree = [e_factory() for _ in range(self.offset << 1)]
        self.e_factory = e_factory
        self.operand = operand

    def update(self, i, value):  # O(logN)
        """i番目の要素をvalueにする"""
        i += self.offset
        self.tree[i] = value
        # 親ノードを順に変更していく
        while i > 1:
            v1, v2 = self.tree[i], self.tree[i ^ 1]  # 子ノード
            i >>= 1  # iを親ノードへずらす
            self.tree[i] = self.operand(v1, v2)

    def get_range(self, l, r):  # O(logN)
        """区間[l, r)の値を取得する"""
        l += self.offset
        r += self.offset

        ans = self.e_factory()
        while l < r:
            if r & 1:
                ans = self.operand(ans, self.tree[r - 1])
                r -= 1
            if l & 1:
                ans = self.operand(self.tree[l], ans)
                l += 1
            l >>= 1
            r >>= 1
        return ans


W, N = map(int, input().split())

dp = [SegTree(W + 1, e_factory=lambda: -1, operand=max) for _ in range(N + 1)]
for i in range(N + 1):
    dp[i].update(0, 0)
# dp[i][j]: i番目まで見て、香辛料をちょうどj使った時の価値の最大値
for i in range(1, N + 1):
    l, r, v = map(int, input().split())
    for j in range(1, W + 1):
        pv = dp[i - 1].get_range(max(0, j - r), max(0, j - l + 1))
        now = dp[i].get_range(j, j + 1)
        nex = max(now, dp[i - 1].get_range(j, j + 1))
        if pv != -1:
            nex = max(nex, pv + v)
        dp[i].update(j, nex)
    # print(dp[i].tree[dp[i].offset :])

ans = dp[N].get_range(W, W + 1)
print(ans)
