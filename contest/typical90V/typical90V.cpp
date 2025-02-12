#include <bits/stdc++.h>
using namespace std;

using ll = long long;

ll A, B, C;
ll ans;

int main(){
    cin >> A >> B >> C;
    ll g = gcd(A, gcd(B, C));
    ans = A/g - 1 + B/g - 1 + C/g - 1;
    cout << ans << endl;
    return 0;
}