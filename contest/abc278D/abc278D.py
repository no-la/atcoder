N = int(input())
A = list(map(int, input().split()))
Q = int(input())

count = [0] * N
init_count = 0
init_value = 0

for _ in range(Q):
    t, *x = map(int, input().split())
    if t == 1:
        init_count += 1
        init_value = x[0]
    elif t == 2:
        i, x = x
        i -= 1
        if init_count > count[i]:
            A[i] = init_value
            count[i] = init_count
        A[i] += x
    else:
        i = x[0] - 1
        if init_count > count[i]:
            A[i] = init_value
            count[i] = init_count
        print(A[i])
