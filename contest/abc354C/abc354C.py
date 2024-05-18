N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
B = A.copy()

d = set()
A.sort(reverse=True)
# print(*A, sep="\n")
min_c = 10**9 + 100
for i in range(N): # aについて降順
    a, c = A[i]
    if min_c < c:
        d.add((a, c))
        
    min_c = min(min_c, c)

# print(d)
print(N-len(d))
print(*[i+1 for i in range(N) if tuple(B[i]) not in d])
        
