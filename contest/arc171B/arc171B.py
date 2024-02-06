N = int(input())
A = list(map(int, input().split()))

mod = 998244353

#必要条件 A[i]>=i
for i, a in enumerate(A):
    if a<i:
        print(0)
        exit()
        
