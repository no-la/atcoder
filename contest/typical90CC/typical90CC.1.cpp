#include <bits/stdc++.h>
using namespace std;

using ll = long long;

int N, K;
int M;

int main(){
    cin >> N >> K;
    vector<vector<int>> AB(N, vector<int>(2));
    for(int i = 0; i < N; i++){
        cin >> AB[i][0] >> AB[i][1];
        M = max(M, AB[i][1])+1;
    }
    sort(AB.begin(), AB.end());

    vector<int> imos(M+1);
    int r = 0;
    int ans = 1;
    for (int l = 0; l < N; l++) {
        while (r < N && AB[r][0] - AB[l][0] <= K) {
            imos[AB[r][1]] += 1;
            if (AB[r][1]+K+1 <= M) imos[AB[r][1]+K+1] -= 1;
            r++;
        }
        
        vector<int> restored_imos(M+1);
        
        for (int i = 0; i < M; i++) {
            restored_imos[i+1] = restored_imos[i] + imos[i+1];
        }
        for (int i = 0; i <= M; i++) ans = max(ans, restored_imos[i]);

        imos[AB[l][1]] -= 1;
        if (AB[l][1]+K+1 <= M) imos[AB[l][1]+K+1] += 1;
    }

    cout << ans << endl;

    return 0;
}
