
#include <bits/stdc++.h>
#include <atcoder/segtree>
using namespace std;
using namespace atcoder;

using ll = long long;
ll W, N;

struct S {
    ll a;
};

S op(S l, S r) { return S{max(l.a, r.a)}; }

S e() { return S{-1}; }


int main(){
    cin >> W >> N;
    vector<S> a(W+1, e());
    a[0] = S{0};
    vector<segtree<S, op, e>> dp(N+1, segtree<S, op, e>(a));

    for (int i=1; i<=N; i++) {
        ll l, r, v;
        cin >> l >> r >> v;
        for (int j=1; j<=W; j++) {
            ll pv = dp[i-1].prod(max(0LL, j-r), max(0LL, j-l+1)).a;
            ll now = dp[i].get(j).a;
            ll nex = max(now, dp[i-1].get(j).a);
            if (pv != -1) nex = max(nex, pv + v);
            dp[i].set(j, S{nex});
        }
    }
    cout << dp[N].get(W).a << endl;

    return 0;
}