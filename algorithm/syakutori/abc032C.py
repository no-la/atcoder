#https://atcoder.jp/contests/abc032/submissions/49587904
N, K = map(int, input().split())
S = [int(input()) for _ in range(N)]

# 0があるときは例外として扱う
if 0 in S:
    print(N)
    exit()


ans = 0
#「条件を満たす部分列」の部分列は条件を満たす
right = 0
temp = 1
for left in range(N):
    while right<N and temp*S[right]<=K: #条件の判定
        temp *= S[right]
        right += 1
    ans = max(ans, right-left)
    if left == right: #[left, right)が空集合なのでtemp=1になっているはず
        right += 1
    else: #このあと、leftを++するので、その分の情報を削る
        temp /= S[left]
print(ans)