#include <bits/stdc++.h>
using namespace std;

using ll = long long;

int N;
map<string, bool> exists;
vector<int> ans;

int main(){
    cin >> N;
    for (int i=0; i<N; i++) {
        string s;
        cin >> s;
        if (exists.count(s)) continue;
        ans.push_back(i+1);
        exists[s] = true;
    }
    for (int i : ans) {
        cout << i << endl;
    }
    return 0;
}