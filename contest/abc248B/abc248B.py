A, B, K = map(int, input().split())

now = A
count = 0
while now<B:
    now *= K
    count += 1
print(count)
