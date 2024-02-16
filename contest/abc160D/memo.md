
# [問題](https://atcoder.jp/contests/abc160/tasks/abc160_d)

1 から 
N までの番号がつけられた 
N 個の頂点を持つ無向グラフ 
G があります。 
G には、以下のように合計 
N 本の辺があります。

i=1,2,...,N−1 について、頂点 
i と頂点 
i+1 の間に辺があります
頂点 
X と頂点 
Y の間に辺があります
k=1,2,...,N−1 について、以下の問題を解いてください。

整数の組 
(i,j)(1≤i<j≤N) であって、 
G において頂点 
i と頂点 
j の最短距離が 
k であるようなものの数を求めてください

## 制約
3≤N≤2×10^3
 
1≤X,Y≤N

X+1<Y

入力はすべて整数である。



## MY SOLUTION
距離kでループして、

* ```i -> i+k (i=0, ..., N-k-1)```
* ```(X-i or X+i) -> X -> Y -> (Y-k+i or Y+k-i) (i=0, ..., k-1)```

を調べて、それが最短距離のときにans(set)に追加していって、
最後に```print(len(ans))```する。

## [解説](https://blog.hamayanhamayan.com/entry/2020/03/29/000745)

距離をindexにするlist ansを用意して、
```python
# (i<j in [0, ..., N-k])
ans[min(j-i、abs(X-i)+1+abs(Y-j))] += 1
```

とすればよい。

```c++
int N, X, Y;
int ans[2010];

void _main() {
    cin >> N >> X >> Y;
    X--; Y--;

    rep(i, 0, N) rep(j, i + 1, N) {
        int k = inf;

        // not use X -> Y
        chmin(k, j - i);

        // use X -> Y
        chmin(k, abs(X - i) + abs(Y - j) + 1);

        ans[k]++;
    }

    rep(k, 1, N) cout << ans[k] << endl;
}
```