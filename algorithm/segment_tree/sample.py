# https://ikatakos.com/pot/programming_algorithm/data_structure/segment_tree
class SegTreeMin:
    """
    以下のクエリを処理する
    1.update:  i番目の値をxに更新する
    2.get_min: 区間[l, r)の最小値を得る
    """
 
    def __init__(self, n, INF):
        """
        :param n: 要素数
        :param INF: 初期値（入りうる要素より十分に大きな数）
        """
        n2 = 1 << (n - 1).bit_length() #n以上で最小の2の累乗 +n2で二分木の一番下の段のidになる
        self.offset = n2
        self.tree = [INF] * (n2 << 1) #n2<<1=2n*2(1-indexed(分割数は2n*2-1))
        self.INF = INF
 
    def update(self, i, x):
        """
        i番目の値をxに更新
        :param i: index(0-indexed)
        :param x: update value
        """
        i += self.offset
        self.tree[i] = x
        #i番目の値を変えたことによる、それを含む区間の値の変更
        while i > 1: #i=1が最後
            y = self.tree[i ^ 1] #兄弟ノード i^1=i+1(i:even) or i-1(i:odd)なので、下一桁だけ変える
            if y <= x: #兄弟ノードがxより小さければ、それ以上親を調べる必要はない
                break
            i >>= 1 #親ノードのid
            self.tree[i] = x
 
    def get_min(self, a, b):
        """
        [a, b)の最小値を得る
        :param a: index(0-indexed)
        :param b: index(0-indexed)
        """
        result = self.INF
 
        l = a + self.offset
        r = b + self.offset
        # l, rを親ノードへ移しつつ、適宜lを内側に進めて、各段階でl, rそれぞれを端点にする区間の値を調べる
        while l < r:
            #親ノードに移るときに余計な区間を含まないようにする
            if r & 1: #r-1:even r-1が左側の子ノードのとき
                result = min(result, self.tree[r - 1])
                r -= 1 #左へ
            if l & 1: #l:odd lが右側の子ノードのとき
                result = min(result, self.tree[l])
                l += 1 #右へ
            l >>= 1
            r >>= 1
 
        return result