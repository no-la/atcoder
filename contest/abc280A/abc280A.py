H, W = map(int, input().split())
S = [input() for _ in range(H)]
print(sum([sum(s.count("#") for s in S)]))
