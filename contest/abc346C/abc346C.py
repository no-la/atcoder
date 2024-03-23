N, K = map(int, input().split())
A = list(map(int, input().split()))

print((K*(1+K))//2 - sum(set([a for a in A if a<=K])))