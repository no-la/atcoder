K = int(input())
A, B = map(int, input().split())

for i in range(10000):
    if A<=K*i<=B:
        print("OK")
        break
else:
    print("NG")