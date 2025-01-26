import math

T = int(input())

for _ in range(T):
    N, D, K = map(int, input().split())
    g = math.lcm(N, D) // D

    offset, remain = divmod(K - 1, g)
    # loop + (remian回分の移動) が答え
    print(offset + (remain * D) % N)
