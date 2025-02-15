#include <bits/stdc++.h>
using namespace std;

using ll = long long;

int N, M = 1000;
vector<vector<int>> imos(M+2, vector<int>(M+2, 0));

int main(){
    cin >> N;
    for (int i=0; i<N; i++) {
        int lx, ly, rx, ry;
        cin >> lx >> ly >> rx >> ry;

        // 点ではなく面を数えることに注意
        for (int j=ly; j<ry; j++) {
            imos[j][lx] += 1;
            imos[j][rx] -= 1;
        }
    }

    // 復元
    for (int i=0; i<=M; i++) {
        for (int j=0; j<=M; j++) {
            imos[i][j+1] += imos[i][j];
        }
    }
    
    int ans[N+1] = {};
    for (int i=0; i<=M; i++) {
        for (int j=0; j<=M; j++) {
            ans[imos[i][j]] += 1;
        }
    }

    for (int i=1; i<=N; i++) cout << ans[i] << endl;
    return 0;
}