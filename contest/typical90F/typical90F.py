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


N, K = map(int, input().split())
S = input()

# Sを左から見て、一番小さい文字のうち、一番左にあるものを採用する
# ただし、残りの文字が足りなくならないように注意する
# これをK個選ぶまで繰り返せばいい

st = SegTree(N, lambda: ("z", N + 1), operand=min)
for i, s in enumerate(S):
    st.update(i, (s, i))

# stは(区間内の最小の文字, そのindex)をもつ

ans = []
bi = -1
while len(ans) < K:
    # print(ans, bi + 1, N - (K - len(ans)) + 1)
    s, i = st.get_range(bi + 1, N - (K - len(ans)) + 1)
    ans.append(s)
    bi = i
print(*ans, sep="")
