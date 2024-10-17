N = int(input())
A = list(map(int, input().split()))

ans = set()
for i in range(N // 2):
    if A[i] != A[-i - 1]:
        ans.add(tuple(sorted([A[i], A[-i - 1]])))

print(len(ans))
