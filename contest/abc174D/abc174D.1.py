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

N = int(input())
C = input()
st_r = SegTree(N, -1) # 各区間で一番右側にあるRのindex
# RR...RWW...W にするための最小コストを出す
# 各wについて、自分より右側にrがある場合、最も右側にあるものと入れ替える
# 無ければ終わり