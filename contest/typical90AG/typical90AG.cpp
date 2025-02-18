#include <bits/stdc++.h>
using namespace std;

using ll = long long;

int main(){
    int H, W;
    cin >> H >> W;
    int ans = 0;
    for (int i=0; i<H; i+=2) {
        for (int j=0; j<W; j+=2) {
            ans += 1;
        }
    }
    if (H<2 || W<2) ans = H*W;
    cout << ans << endl;
    return 0;
}