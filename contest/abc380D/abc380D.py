S = input()
Q = int(input())
K = list(map(int, input().split()))
N = len(S)

ans = []
for k in K:
    r = (k - 1) % N  # S[r]をどうするかって問題
    q = (k - 1) // N + 1

    a = q
    count = 0
    while a > 1:
        b = 1 << (a.bit_length() - 1)
        if a == b:
            b //= 2
        # print(q, a, b, parity)
        # print(k, a, b)
        count += 1
        a -= b

    if count % 2:
        ans.append(S[r].swapcase())
    else:
        ans.append(S[r])

print(*ans)
