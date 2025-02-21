#include <bits/stdc++.h>
using namespace std;

using ll = long long;
ll A, B;
ll INF = 1000000000000000000;

int main(){
    cin >> A >> B;
    ll g = gcd(A, B);
    // ans = A*B/g >= 1
    // if (INF / (A*B/g) < 1) cout << "Large" << endl;
    if (INF/B < A/g) cout << "Large" << endl;
    else cout << (A/g)*B << endl;
    return 0;
}