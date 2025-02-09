#include <iostream>
#include <vector>
#include <iomanip>  // setprecisionのために必要
#include <cmath>    // powのために必要

using namespace std;

int main() {
    int N;
    cin >> N;

    const int M = 100000;
    vector<vector<double>> d(N, vector<double>(M + 1, 0.0));

    // サイコロの目の情報を読み込み
    for (int i = 0; i < N; ++i) {
        int k;
        cin >> k;  // サイコロの面の数
        vector<int> A(k);
        for (int j = 0; j < k; ++j) {
            cin >> A[j];
        }
        for (int a : A) {
            d[i][a] += 1.0 / k;
        }
    }

    double ans = 0.0;

    // 2つのサイコロの目が一致する確率を計算
    for (int i = 0; i < N; ++i) {
        for (int j = i + 1; j < N; ++j) {
            double temp = 0.0;
            for (int a = 1; a <= M; ++a) {
                temp += d[i][a] * d[j][a];
            }
            ans = max(ans, temp);
        }
    }

    // 精度を保つために小数点以下10桁で表示
    cout << fixed << setprecision(15) << ans << endl;

    return 0;
}
