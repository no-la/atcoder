N = int(input())
A = list(map(int, input().split()))
MOD = 10**8

# 2<= x+y < 10^8 + 10^8
s = sum(A)
A.sort()
ans = 0
j = N
for i in range(N-1):
    a = A[i]
    s -= a
    j = max(i+1, j)
    while i<j-1 and a+A[j-1]>=MOD:
        j -= 1
    
    # print(a, A[i+1:j], A[j:], i, j)
    
    ans += (N-i-1)*a+s - MOD*(N-j)

print(ans)
