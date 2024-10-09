N, Q = map(int, input().split())
S = input()

offset = 0
for _ in range(Q):
    t, x = map(int, input().split())
    if t == 1:
        offset += x
        offset %= N
    elif t == 2:
        x -= 1
        i = -offset + x if x <= offset else x - offset
        # print(offset, x, i)
        print(S[i])
