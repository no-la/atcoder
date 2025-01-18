class LazySegTree_RAQ:
    """遅延評価セグ木(区間加算)"""

    def __init__(
        self,
        num,
        e_factory=lambda: 0,
        operand=lambda x, y: x + y,
        lazy_operand=lambda x, y: x + y,
        action=lambda x, a: x + a,
    ):
        """
        Parameters
        ----------
            num : 要素数
            e_factory : 単位元を生成する関数
            lazy_operand : lazyにおける演算
            action: lazyとtreeの演算(遅延評価のためのもの)
        """
        # self.tree[i+self.offset]:要素iのみの区間の値
        self.offset = 1 << (num - 1).bit_length()
        self.tree = [e_factory() for _ in range(self.offset << 1)]
        self.e_factory = e_factory
        self.operand = operand
        self.lazy_operand = lazy_operand
        self.action = action

        self.lazy = [e_factory() for _ in range(self.offset << 1)]

    def update_range(self, l, r, value):  # O(logN)
        """[l, r)の要素にvalueを作用させるためにlazyを更新する"""
        l += self.offset
        r += self.offset

        while l < r:
            if r & 1:
                self.lazy_eval(r - 1)
                self.lazy[r - 1] = self.lazy_operand(value, self.lazy[r - 1])
                r -= 1
            if l & 1:
                self.lazy_eval(l)
                self.lazy[l] = self.lazy_operand(value, self.lazy[l])
                l += 1
            l >>= 1
            r >>= 1

    def lazy_eval(self, segment_i):
        """segment_iのノードの遅延評価と子への伝播を行う"""

        length = segment_i.bit_length()  # このノードの要素数
        if self.lazy[segment_i] == self.e_factory():
            return
        if segment_i < self.offset:  # 葉でなければlazyを子ノードに伝播
            l, r = segment_i << 1, (segment_i << 1) + 1
            self.lazy[l] = self.lazy_operand(self.lazy[l], self.lazy[segment_i])
            self.lazy[r] = self.lazy_operand(self.lazy[r], self.lazy[segment_i])

        self.tree[segment_i] = self.action(
            self.tree[segment_i], self.lazy[segment_i] * length
        )
        self.lazy[segment_i] = self.e_factory()

    def get_range(self, l, r):  # O(logN)
        """区間[l, r)の値を取得する"""
        # [l, r)と一部でも重なっているすべての区間に対応するノードは
        # 親から順に、lazy_evalをする必要がある
        # 各階層につき高々2回のlazy_evalなので、O(logN)程度になる
        need_lazy_eval = set()

        l += self.offset
        r += self.offset

        # [l, r)を構成するノードのlist
        target_left_segments = []
        target_right_segments = []
        while l < r:
            # 親もneed_lazy_evalに追加する
            temp = len(need_lazy_eval)
            for segment_i in range(temp):
                need_lazy_eval.add(need_lazy_eval[segment_i] >> 1)

            if r & 1:
                need_lazy_eval.add(r - 1)
                target_right_segments.append(r - 1)
                r -= 1
            if l & 1:
                need_lazy_eval.add(l)
                target_left_segments.append(l)
                l += 1
            l >>= 1
            r >>= 1

        # lazy_evalする
        need_lazy_eval = sorted(need_lazy_eval, reverse=True)
        while need_lazy_eval:
            segment_i = need_lazy_eval.pop()
            self.lazy_eval(segment_i)

        # 区間の値を取得する
        ans = self.e_factory()
        while target_left_segments:
            segment_i = target_left_segments.pop()
            ans = self.operand(self.tree[segment_i], ans)
        while target_right_segments:
            segment_i = target_right_segments.pop()
            ans = self.operand(ans, self.tree[segment_i])
        return ans


N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

lst = LazySegTree_RAQ(N)

for i, a in enumerate(A):
    lst.update_range(i, i + 1, a)

for b in B:
    a = A[b]
    entire, remain = divmod(a, N)
    first = min(N - 1 - b, remain)
    end = remain - first
    lst.update_range(b, b + 1, -a)
    lst.update_range(b + 1, b + 1 + first, 1)
    lst.update_range(0, N, entire)
    lst.update_range(0, end, 1)
    print(b, a, first, entire, end)

print(*[lst.get_range(i, i + 1) for i in range(N)])
