#include <bits/stdc++.h>
using namespace std;

using ll = long long;
int N, A[100000], B[100000], deg[100000];
vector<vector<int>> E(10000);

bool seen[100000];

vector<int> ans;

void dfs(int v, int a){
    if (ans.size()==N/2) return;
    if (seen[v]) return;
    seen[v] = true;
    
    if (a==0) ans.push_back(v+1);
    for (int w : E[v]) {
        if (seen[w]) continue;
        dfs(w, a^1);
    }
}

int main(){
    // 葉から全探索してパリティを見るだけ
    cin >> N;
    for (int i=0; i<N-1; i++) {
        int a, b;
        cin >> a >> b;
        a--; b--;
        E[a].push_back(b);
        E[b].push_back(a);
        deg[a]++; deg[b]++;
    }
    
    int leaf;
    for (int i=0; i<N; i++) {
        if (deg[i]==1) {
            leaf = i;
            break;
        }
    }

    dfs(leaf, 0);

    for (int i=0; i<ans.size(); i++){
        cout << ans[i];
        if (i!=ans.size()-1) cout << " ";
        else cout << endl;
    }
    
    return 0;
}