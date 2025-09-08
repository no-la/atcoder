A, B = map(int, input().split())

if A == B:
    print(-1)
else:
    print((set([1, 2, 3]) - set([A, B])).pop())
