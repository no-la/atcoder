#include <bits/stdc++.h>
using namespace std;

using ll = long long;

int main(){
    // それぞれにソートして並列で見ていく感じ
    int N;
    cin >> N;
    vector<ll> A(N, 0), B(N, 0);
    for (int i=0; i<N; i++) {
        cin >> A[i];
    }
    for (int i=0; i<N; i++) {
        cin >> B[i];
    }
    sort(A.begin(), A.end());
    sort(B.begin(), B.end());

    ll ans = 0;
    for (int i=0; i<N; i++) {
        ans += abs(A[i]-B[i]);
    }
    cout << ans << endl;
    return 0;
}