V, *A = list(map(int, input().split()))

i = 0
while True:
    V -= A[i%3]
    if V<0:
        print("FMT"[i%3])
        exit()
    i += 1
