#include <bits/stdc++.h>
using namespace std;

using ll = long long;

class UnionFind {
    public:
        vector<int> parent;
        
        void init(int size) {
            parent.resize(size, -1);
        }
        int find(int pos) {
            if (parent[pos] == -1) return pos;
            parent[pos] = find(parent[pos]);
            return parent[pos];
        }
        void unio(int u, int v) { // unionって予約語なの？
            u = find(u); v = find(v);
            if (u == v) return;
            parent[u] = v;
        }
};

int main(){
    int H, W, Q;
    UnionFind uf;
    cin >> H >> W >> Q;
    vector<bool> is_red(H*W, false);

    uf.init(H*W);

    vector<tuple<int, int>> delta = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
    for (int i=0; i<Q; i++) {
        int t;
        cin >> t;
        if (t==1) {
            int r, c;
            cin >> r >> c;
            r--; c--;

            int tar_i = r*W+c;
            is_red[tar_i] = true;
            for (tuple<int, int> d: delta) {
                int j, k;
                tie(j, k) = d;

                if (r+j<0 || H<=r+j || c+k<0 || W<=c+k) continue;
                
                int tar_next_i = (r+j)*W + (c+k);
                if (is_red[tar_next_i]) {
                    uf.unio(tar_i, tar_next_i);
                }
            }
        }
        else {
            int ra, ca, rb, cb;
            cin >> ra >> ca >> rb >> cb;
            ra--; ca--; rb--; cb--;
            int ai = ra*W+ca, bi = rb*W+cb;

            if (uf.find(ai) == uf.find(bi) && is_red[ai] && is_red[bi]) cout << "Yes" << endl;
            else cout << "No" << endl;
        }
    }

    return 0;
}