N, Q = map(int, input().split())
lr = [0, 1]

ans = 0
for _ in range(Q):
    h, t = input().split()
    t = int(t) - 1
    if h == "L":
        i = 0
    else:
        i = 1
    j = (i + 1) % 2

    temp = 100000
    if lr[i] < t < lr[j]:
        temp = min(temp, t - lr[i])
    elif t < lr[i] < lr[j]:
        temp = min(temp, lr[i] - t)
    elif lr[i] < lr[j] < t:
        temp = min(temp, lr[i] - (t - N))
    elif lr[j] < t < lr[i]:
        temp = min(temp, lr[i] - t)
    elif t < lr[j] < lr[i]:
        temp = min(temp, t + N - lr[i])
    elif lr[j] < lr[i] < t:
        temp = min(temp, t - lr[i])
    else:
        temp = 0
    ans += temp
    lr[i] = t

print(ans)
