S = list(input())
a, b = map(lambda x: int(x)-1, input().split())

S[a], S[b] = S[b], S[a]
print("".join(S))