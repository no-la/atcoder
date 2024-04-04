class SegTree:
    def __init__(self, num, e, operator=max):
        """
        parameter
            num : 要素数
            e : 単位元(初期値)
            operator : 2つの子ノードの値から親ノードの値を作る関数
        """
        #self.tree[i+self.offset]:要素iのみの区間の値
        self.offset = 1 << (num-1).bit_length()
        self.tree = [e]*(self.offset<<1)
        self.e = e
        self.operator = operator
    
    def update(self, i, value):
        """i番目の要素をvalueにする
        """
        i += self.offset
        self.tree[i] = value
        #親ノードを順に変更していく
        while i>1:
            v1, v2 = self.tree[i], self.tree[i^1] #子ノード
            i >>= 1 #iを親ノードへずらす
            self.tree[i] = self.operator(v1, v2)
            
    def get_point(self, p):
        """p番目の要素を取得する
        """
        return self.tree[p+self.offset]
    
    def get_range(self, l, r):
        """区間[l, r)の値を取得する
        """
        l += self.offset
        r += self.offset
        
        ans = self.e
        while l<r:
            if r&1:
                ans = self.operator(ans, self.tree[r-1])
                r -= 1
            if l&1:
                ans = self.operator(ans, self.tree[l])
                l += 1
            l >>= 1
            r >>= 1
        return ans


N, K = map(int, input().split())
LR = [tuple(map(int, input().split())) for _ in range(K)]
MOD = 998244353

st = SegTree(N+1, 0, lambda l, r: (l+r)%MOD) # st.tree[i]: マスiに行く方法の個数
st.update(0, 1)
for i in range(1, N):
    for l, r in LR:
        b = [max(i-r, 0), min(N-1, i-l)+1]
        if b[0]>=b[1]:
            continue
        # print("from", b, "to", i)
        st.update(i, (st.get_point(i)+st.get_range(*b))%MOD)
    # print("point", i, *[(j, st.get_point(j)) for j in range(N)])
print(st.get_point(N-1))