N, K, A = map(int, input().split())

ans = (A+K-2)%N+1
print(ans)