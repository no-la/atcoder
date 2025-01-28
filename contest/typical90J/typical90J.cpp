#include <bits/stdc++.h>
using namespace std;
int main() {
    int N, Q;
    cin >> N;
    vector<int> sumA(N+1, 0), sumB(N+1, 0);

    // A, Bそれぞれに累積和を計算する
    for (int i = 0; i < N; i++) {
        int c, p;
        cin >> c >> p;
        sumA[i+1] = sumA[i] + (c==1? p : 0);
        sumB[i+1] = sumB[i] + (c==2? p : 0);
    }


    cin >> Q;
    for (int i = 0; i < Q; i++) {
        int L, R;
        cin >> L >> R;
        L--; R--;

        cout << sumA[R+1] - sumA[L] << " " << sumB[R+1] - sumB[L] << endl;
    }

    return 0;
}