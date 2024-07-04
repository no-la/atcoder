N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))


for i in range(M):
    # 階差数列と復元
    # A[i]<=10^9なので区間の重複を考慮する
    temp = [0]*(N+1)
    
    sl = (B[i]+1)%N
    sr = N if B[i]+A[B[i]]>=N else B[i]+A[B[i]]+1
    temp[sl] += 1
    temp[sr] -= 1
    
    loop_n = B[i]+A[B[i]]//N - 1
    temp[0] += loop_n
    
    el = 0
    er = (B[i]+A[B[i]])%N + 1
    temp[el] += 1
    temp[er] -= 1
    
    
