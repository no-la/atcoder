#include <bits/stdc++.h>
using namespace std;

using ll = long long;

ll N, K, A[1000], B[1000];

int main(){
    cin >> N >> K;

    int count = 0;
    for (int i=0; i<N; i++) {
        cin >> A[i];
    }
    for (int i=0; i<N; i++) {
        cin >> B[i];
    }
    for (int i=0; i<N; i++) {
        count += abs(A[i] - B[i]);
    }

    if (K >= count && (K-count)%2LL == 0) cout << "Yes" << endl;
    else cout << "No" << endl;
    return 0;
}