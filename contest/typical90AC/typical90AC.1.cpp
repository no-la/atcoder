#include <bits/stdc++.h>
#include <atcoder/lazysegtree>
using namespace std;
using namespace atcoder;

using ll = long long;
int W, N;

struct S {
    int a;
};

struct F {
    int a;
};

S op(S l, S r) { return S{max(l.a, r.a)}; }

S e() { return S{0}; }

F id() { return F{0}; }

S mapping(F f, S s) { return f.a==id().a? s : S{f.a}; }

F composition(F f, F g) { return F{max(f.a, g.a)}; }


int main(){
    cin >> W >> N;
    vector<S> a(W);
    lazy_segtree<S, op, e, F, mapping, composition, id> seg(a);

    for (int i=0; i<N; i++) {
        int l, r;
        cin >> l >> r;
        l--; r--;
        int height = seg.prod(l, r+1).a + 1;
        seg.apply(l, r+1, F{height});
        
        cout << height << endl;
    }

    return 0;
}