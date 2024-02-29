A, B, C, K = map(int, input().split())


ans = min(A, K)
K -= A
if K>0:
    K -= B
if K>0:
    ans -= min(C, K)

print(ans)
    