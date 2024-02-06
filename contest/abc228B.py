N, X = map(int, input().split())
A = list(map(int, input().split()))

d = set()
i = X
while i not in d:
    d.add(i)
    i = A[i-1]
print(len(d))