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


N, M = map(int, input().split())
d = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().split())
    d[a - 1].append(b - 1)
    d[b - 1].append(a - 1)


from heapq import heappop, heappush

todo = []
seen = [False] * N
seen[0] = True
for v in d[0]:
    heappush(todo, v)

count = SegTree(N, lambda: 0, lambda x, y: x + y)
count.update(0, 1)
for t in d[0]:
    count.update(t, 1)

for i in range(N):
    while todo and todo[0] <= i:
        v = heappop(todo)
        if seen[v]:
            continue
        seen[v] = True
        for w in d[v]:
            if seen[w]:
                continue
            heappush(todo, w)
            count.update(w, 1)

    # print(seen, todo, count.tree[count.offset :])
    if count.get_range(0, i + 1) == i + 1:
        print(count.get_range(i + 1, N))
    else:
        print(-1)
