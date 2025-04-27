import sys, bisect

input = lambda: sys.stdin.readline().rstrip()
N, D = map(int, input().split())
A = list(map(int, input().split()))

A.sort()
seen = [False] * N
count = [0] * N

for i in range(N):
    if seen[i]:
        continue
    count[i] = 1

    pi = i
    seen[pi] = True
    ni = bisect.bisect_left(A, A[pi] + D)
    while ni < N and A[ni] - A[pi] == D and not seen[ni]:
        count[i] += 1
        pi = ni
        seen[pi] = True
        ni = bisect.bisect_left(A, A[pi] + D)


# print(count)
print(sum([c // 2 for c in count]))
