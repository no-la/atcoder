N, K = map(int, input().split())
A = list(map(int, input().split()))
print(*[a//K for a in A if a%K==0])