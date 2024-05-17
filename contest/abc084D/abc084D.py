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


Q = int(input())
N = 10**5


# osa_k法
MAXN = N+10
sieve = [i for i in range(MAXN)] # sieve[i]: iの最も小さい素因数
p = 2
while p*p<=MAXN: # O(MAXN * loglog MAXN)
    if sieve[p]==p:
        for q in range(p*p, MAXN, p):
            if sieve[q]==q:
                sieve[q] = p
    p += 1

from collections import defaultdict
def is_prime(n):
    """n(2<=n<=MAXN)の素因数を返す"""
    return sieve[n]==n


st = SegTree(N+2, 0, lambda x, y: x+y)
for i in range(3, N+1):
    if is_prime(i) and is_prime((i+1)//2):
        # print(i)
        st.update(i, 1)

for _ in range(Q):
    l, r = map(int, input().split())
    print(st.get_range(l, r+1))
