#include <bits/stdc++.h>
#include <atcoder/segtree>

using namespace std;
using namespace atcoder;

using ll = long long;

int op(int a, int b) { return a + b; };
int e() { return 0; };

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

    segtree<int, op, e> st(M);
    int r = 0;
    int ans = 1;
    for (int l = 0; l < N; l++) {
        while (r < N && AB[r][0] - AB[l][0] <= K) {
            st.set(AB[r][1], st.get(AB[r][1]) + 1);
            r++;
        }
        
        for (int i = 0; i < M; i++) {
            int temp = st.prod(i, min(M, i + K + 1));
            ans = max(ans, temp);
        }
        st.set(AB[l][1], st.get(AB[l][1]) - 1);
    }

    cout << ans << endl;

    return 0;
}
