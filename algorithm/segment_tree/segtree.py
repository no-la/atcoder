class SegTree:
    def __init__(self, num, e, operand=max):
        """
        parameter
            num : 要素数
            e : 単位元(初期値)
            operand : 子ノードの値から親ノードの値を作る関数
        """
        #self.tree[i+self.offset]:要素iのみの区間の値
        self.offset = 1 << (num-1).bit_length()
        self.tree = [e]*(self.offset<<1)
        self.e = e
        self.operand = operand
    
    def update(self, i, value): #O(logN)
        """i番目の要素をvalueにする
        """
        i += self.offset
        self.tree[i] = value
        #親ノードを順に変更していく
        while i>1:
            v1, v2 = self.tree[i], self.tree[i^1] #子ノード
            i >>= 1 #iを親ノードへずらす
            self.tree[i] = self.operand(v1, v2)
        
    def get_range(self, l, r): #O(logN)
        """区間[l, r)の値を取得する
        """
        l += self.offset
        r += self.offset
        
        ans = self.e
        while l<r:
            if r&1:
                ans = self.operand(ans, self.tree[r-1])
                r -= 1
            if l&1:
                ans = self.operand(ans, self.tree[l])
                l += 1
            l >>= 1
            r >>= 1
        return ans