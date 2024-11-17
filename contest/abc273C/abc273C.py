N = int(input())
A = list(map(int, input().split()))

B = sorted(set(A))
import bisect

ans = [0] * N
for a in A:
    ans[len(B) - bisect.bisect_right(B, a)] += 1

print(*ans, sep="\n")
