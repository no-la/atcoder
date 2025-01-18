"""https://qiita.com/ether2420/items/7b67b2b35ad5f441d686"""


def segfunc(x, y):
    return x + y


class LazySegTree_RAQ:
    def __init__(self, init_val, segfunc, ide_ele):
        n = len(init_val)
        self.segfunc = segfunc
        self.ide_ele = ide_ele
        self.num = 1 << (n - 1).bit_length()
        self.tree = [ide_ele] * 2 * self.num
        self.lazy = [0] * 2 * self.num
        for i in range(n):
            self.tree[self.num + i] = init_val[i]
        for i in range(self.num - 1, 0, -1):
            self.tree[i] = self.segfunc(self.tree[2 * i], self.tree[2 * i + 1])

    def gindex(self, l, r):
        if l >= r:
            return []

        l += self.num
        r += self.num
        lm = l >> (l & -l).bit_length()
        rm = r >> (r & -r).bit_length()
        while r > l:
            if l <= lm:
                yield l
            if r <= rm:
                yield r
            r >>= 1
            l >>= 1
        while l:
            yield l
            l >>= 1

    def propagates(self, *ids):
        for i in reversed(ids):
            v = self.lazy[i]
            if v == 0:
                continue
            self.lazy[i] = 0
            self.lazy[2 * i] += v
            self.lazy[2 * i + 1] += v
            self.tree[2 * i] += v
            self.tree[2 * i + 1] += v

    def add(self, l, r, x):
        ids = self.gindex(l, r)
        l += self.num
        r += self.num
        while l < r:
            if l & 1:
                self.lazy[l] += x
                self.tree[l] += x
                l += 1
            if r & 1:
                self.lazy[r - 1] += x
                self.tree[r - 1] += x
            r >>= 1
            l >>= 1
        for i in ids:
            self.tree[i] = (
                self.segfunc(self.tree[2 * i], self.tree[2 * i + 1]) + self.lazy[i]
            )

    def query(self, l, r):
        self.propagates(*self.gindex(l, r))
        res = self.ide_ele
        l += self.num
        r += self.num
        while l < r:
            if l & 1:
                res = self.segfunc(res, self.tree[l])
                l += 1
            if r & 1:
                res = self.segfunc(res, self.tree[r - 1])
            l >>= 1
            r >>= 1
        return res


N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

lst = LazySegTree_RAQ(init_val=A, segfunc=segfunc, ide_ele=0)


for b in B:
    a = lst.query(b, b + 1)
    entire, remain = divmod(a, N)
    first = min(N - 1 - b, remain)
    end = remain - first
    lst.add(b, b + 1, -a)
    lst.add(b + 1, b + 1 + first, 1)
    lst.add(0, N, entire)
    lst.add(0, end, 1)

print(*[lst.query(i, i + 1) for i in range(N)])
