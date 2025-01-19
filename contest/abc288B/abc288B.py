N, K = map(int, input().split())
print(*sorted(list([input() for _ in range(N)][:K])), sep="\n")
