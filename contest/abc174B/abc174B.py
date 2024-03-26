N, D = map(int, input().split())
print(sum([sum(map(lambda x: int(x)**2, input().split()))<=D**2 for _ in range(N)]))
