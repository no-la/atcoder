class SegTree:
    def __init__(self, num, e_factory, operator=max):
        self.offset = 1 << (num - 1).bit_length()
        self.tree = [e_factory()] * (self.offset << 1)
        self.e_factory = e_factory
        self.operator = operator

    def update(self, i, value):
        i += self.offset
        self.tree[i] = value
        while i > 1:
            i >>= 1
            self.tree[i] = self.operator(self.tree[i << 1], self.tree[i << 1 | 1])

    def get_point(self, p):
        return self.tree[p + self.offset]

    def get_range(self, l, r):
        l += self.offset
        r += self.offset
        ans_l = self.e_factory()
        ans_r = self.e_factory()
        while l < r:
            if l & 1:
                ans_l = self.operator(ans_l, self.tree[l])
                l += 1
            if r & 1:
                r -= 1
                ans_r = self.operator(self.tree[r], ans_r)
            l >>= 1
            r >>= 1
        return self.operator(ans_l, ans_r)


N = int(input())
A = list(input())
Q = int(input())

st_is_ascending = SegTree(
    N,
    lambda: [True, "", ""],
    lambda x, y: [
        x[0] and y[0] and (x[2] == "" or y[1] == "" or x[2] <= y[1]),
        x[1],
        y[2],
    ],
)
st_char_counts = {
    s: SegTree(N, lambda: 0, lambda x, y: x + y) for s in "abcdefghijklmnopqrstuvwxyz"
}
entire_char_count = {s: 0 for s in "abcdefghijklmnopqrstuvwxyz"}

for i, a in enumerate(A):
    st_is_ascending.update(i, [True, a, a])
    st_char_counts[a].update(i, 1)
    entire_char_count[a] += 1

for _ in range(Q):
    t, *others = input().split()
    if t == "1":
        x, c = others
        x = int(x) - 1
        before_c = st_is_ascending.get_point(x)[1]
        st_is_ascending.update(x, [True, c, c])
        st_char_counts[c].update(x, st_char_counts[c].get_point(x) + 1)
        st_char_counts[before_c].update(x, st_char_counts[before_c].get_point(x) - 1)
        entire_char_count[c] += 1
        entire_char_count[before_c] -= 1
    else:
        l, r = map(lambda x: int(x) - 1, others)
        r += 1
        val = st_is_ascending.get_range(l, r)
        is_ascending = val[0]

        if not is_ascending:
            print("No")
            continue

        is_started = False
        is_finished = False
        for s in "abcdefghijklmnopqrstuvwxyz":
            if not is_started:
                is_started = st_char_counts[s].get_range(l, r) > 0
            elif not is_finished:
                is_finished = st_char_counts[s].get_range(l, r) < entire_char_count[s]
            elif st_char_counts[s].get_range(l, r) > 0:
                break
        else:
            print("Yes")
            continue
        print("No")
