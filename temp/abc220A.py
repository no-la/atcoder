A, B, C = map(int, input().split())

for i in range(1001):
    if A<=C*i<=B:
        print(C*i)
        break
else:
    print(-1)