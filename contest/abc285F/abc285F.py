class SegTree:
    def __init__(self, num, e_factory, operator=max):
        """
        parameter
            num : 要素数
            e : 単位元(初期値)
            operator : 2つの子ノードの値から親ノードの値を作る関数
        """
        # self.tree[i+self.offset]:要素iのみの区間の値
        self.offset = 1 << (num - 1).bit_length()
        self.tree = [e_factory()] * (self.offset << 1)
        self.e_factory = e_factory
        self.operator = operator

    def update(self, i, value):
        """i番目の要素をvalueにする"""
        i += self.offset
        self.tree[i] = value
        # 親ノードを順に変更していく
        while i > 1:
            l, r = sorted([i, i ^ 1])
            v1, v2 = self.tree[l], self.tree[r]  # 子ノード
            i >>= 1  # iを親ノードへずらす
            self.debug_operand(v2, v2)
            self.tree[i] = self.operator(v1, v2)

    def get_point(self, p):
        """p番目の要素を取得する"""
        return self.tree[p + self.offset]

    def get_range(self, l, r):
        """区間[l, r)の値を取得する"""
        l += self.offset
        r += self.offset

        ans = self.e_factory()
        while l < r:
            if r & 1:
                self.debug_operand(ans, self.tree[r - 1])
                ans = self.operator(ans, self.tree[r - 1])
                r -= 1
            if l & 1:
                self.debug_operand(self.tree[l], ans)
                ans = self.operator(self.tree[l], ans)
                l += 1
            l >>= 1
            r >>= 1
        return ans

    def debug_operand(self, v1, v2):
        print(v1, v2, "->", self.operator(v1, v2))


N = int(input())
A = list(input())
Q = int(input())

st = SegTree(
    N,
    lambda: [True, "", ""],
    lambda x, y: [
        x[0] and y[0] and (x[2] == "" or y[1] == "" or x[2] <= y[1]),
        x[1],
        y[2],
    ],
)

# init
for i, a in enumerate(A):
    st.update(i, [True, a, a])


for _ in range(Q):
    t, *others = input().split()
    if t == "1":
        x, c = others
        x = int(x) - 1
        st.update(x, [True, c, c])
    else:
        l, r = map(lambda x: int(x) - 1, others)
        r += 1
        print("-" * 20)
        val = st.get_range(l, r)
        is_ascending = val[0]
        print("Yes" if is_ascending else "No")
