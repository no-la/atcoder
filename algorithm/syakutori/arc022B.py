#https://atcoder.jp/contests/arc022/submissions/49588502
N = int(input())
A = list(map(int, input().split()))

#尺取り法
ans = 0
right = 0
temp = [False]*(100001)
for left in range(N):
    while right<N and not temp[A[right]]: #条件の判定
        temp[A[right]] = True
        right += 1
    ans = max(ans, right-left)
    if left == right: #[left, right)が空集合なので'temp=初期値'になっているはず
        right += 1
    else: #このあと、leftを+1するので、その分の情報を削る
        temp[A[left]] = False
print(ans)