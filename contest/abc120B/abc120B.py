A, B, K = map(int, input().split())

count = 0
for i in range(100, 0, -1):
    count += (A%i==0 and B%i==0)
    if count==K:
        print(i)
        exit()