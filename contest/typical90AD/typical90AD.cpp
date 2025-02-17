#include <bits/stdc++.h>
using namespace std;

using ll = long long;

ll MAXN = 10000010;
ll sieve[10000010];
ll N, K;

void osaK(){
    for (ll p=2; p*p<MAXN; p++){
        if (sieve[p]!=p) continue;

        for (ll q=p*p; q<MAXN; q+=p){
            if (sieve[q]!=q) continue;

            sieve[q] = p;
        }
    }
}

map<ll, int> primeFactors(ll n){
    if (n==0) return {};
    if (n==1) return {{1, 1}};
    map<ll, int> rev;
    while (n>1)
    {
        rev[sieve[n]]++;
        n /= sieve[n];
    }
    return rev;
}

int main(){
    cin >> N >> K;
    for (ll i=0; i<MAXN; i++) sieve[i] = i;
    osaK();
    ll ans = 0;
    for (ll i=2; i<=N; i++){
        if (primeFactors(i).size()>=K) ans++;
    }
    cout << ans << endl;
    return 0;
}