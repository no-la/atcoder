#include <bits/stdc++.h>
using namespace std;

int main() {
    int N;
    int M = 5000; // M = max(D)
    vector<tuple<int, int, long long>> jobs;

    cin >> N;
    for (int i=0; i<N; i++){
        int D, C; long long S;
        cin >> D >> C >> S;
        jobs.push_back(make_tuple(D, C, S));
    }

    sort(jobs.begin(), jobs.end());


    vector<vector<long long>> dp(N+1, vector<long long>(M+1, 0));
    // dp[i][j]: jobs[:i]を見て、j日目の最大値

    for (int i=0; i<N; i++){
        for (int j=0; j<=M; j++){
            int D, C; long long S;
            tie(D, C, S) = jobs[i];

            // 仕事iをしないとき
            dp[i+1][j] = max(dp[i+1][j], dp[i][j]);

            // 仕事iをするとき
            if (j+C <= D){
                dp[i+1][j+C] = max(dp[i+1][j+C], dp[i][j] + S);
            }
        }
    }

    long long ans = 0;
    for (int j=0; j<=M; j++) ans = max(ans, dp[N][j]);
    cout << ans << endl;

    return 0;
}