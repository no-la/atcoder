S = [input() for _ in range(12)]
print(sum([i + 1 == len(S[i]) for i in range(12)]))
