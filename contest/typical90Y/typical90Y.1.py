import sys

input = lambda: sys.stdin.readline().rstrip()
N, B = map(int, input().split())

# f(x)の全探索
# O(10H12) = O(23C12) ~ 10^6

ans = 0

# 重複あり組み合わせ O(nHk)=O(n+k-1Ck)
import itertools

for l in itertools.combinations_with_replacement(range(10), 12):
    target = [a for a in l if a != 0]
    fx = 1
    for k in target:
        fx *= k

    x = B + fx

    # l と x が一致すればOK
    if 1 <= x <= N and sorted(target) == sorted(map(int, str(x))):
        ans += 1

ans += B <= N and "0" in str(B)

print(ans)
