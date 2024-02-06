B = int(input())

# 10^18 <= 16^16
for i in range(1, 17):
    if i**i == B:
        print(i)
        break
else:
    print(-1)