#include <bits/stdc++.h>
#include <atcoder/lazysegtree>
using namespace std;
using namespace atcoder;

using ll = long long;
int W, N;

struct S {
    int a;
    int size;
};

struct F {
    int a;
};

S op(S l, S r) { return S{max(l.a, r.a), l.size + r.size}; }

S e() { return S{0, 1}; }

S mapping(F f, S s) { return S{f.a + s.a, s.size}; }

F composition(F l, F r) { return F{l.a + r.a}; }

F id() { return F{0}; }

int main(){
    cin >> W >> N;
    vector<S> a(W);
    lazy_segtree<S, op, e, F, mapping, composition, id> seg(a);

    for (int i=0; i<N; i++) {
        int l, r;
        cin >> l >> r;
        l--; r--;
        seg.apply(l, r+1, F{1});
        
        cout << seg.prod(l, r+1).a << endl;
    }

    return 0;
}