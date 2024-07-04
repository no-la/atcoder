N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))


# 階差数列のまま更新していって、最後に復元する
ans = [0]*(N+1)
a = A[B[0]] # 次のA[B[_]]だけ別で持っておく
for i in range(M):
    ans[B[i]] -= a
    # A[i]<=10^9なので区間の重複を考慮する
    sl = (B[i]+1)%N
    sr = N if B[i]+a>=N else B[i]+a+1
    ans[sl] += 1
    ans[sr] -= 1
    
    loop_n = B[i]+a//N - 1
    ans[0] += loop_n
    
    el = 0
    er = (B[i]+a)%N + 1
    ans[el] += 1
    ans[er] -= 1
    
    if i<M-1:
        a = ...
    
