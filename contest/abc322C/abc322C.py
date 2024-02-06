N, M = map(int, input().split())
A = list(map(int, input().split()))

count = 1
for a in A:
    while(count <= a):
        print(a-count)
        count += 1

print()
