#include <bits/stdc++.h>
using namespace std;

using ll = long long;

int main(){
    ll N, A, B, C;
    cin >> N >> A >> B >> C;
    int LIMIT = 10000;

    ll ans = LIMIT;
    for (int a=0; a<LIMIT; a++) {
        for (int b=0; b<LIMIT; b++) {
            ll need = N - a*A - b*B;
            if (need<0) break;
            if (need%C == 0) ans = min(ans, a + b + need/C);
        }
    }
    cout << ans << endl;

    return 0;
}