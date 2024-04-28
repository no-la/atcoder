# https://atcoder.jp/contests/caddi2018b/tasks/caddi2018b_b
N, H, W = map(int, input().split())
A = [tuple(map(int, input().split())) for _ in range(N)]

print(sum([a>=H and b>=W for a, b in A]))



