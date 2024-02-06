N = int(input())
seen = [False]*(N+1)
start = -1
temp = []
for _ in range(N-1):
    a, b = map(int, input().split())
    if start==-1:
        if not temp:
            temp.append(a)
            temp.append(b)
            continue

        if a in temp:
            start = a
            p = b
        elif b in temp:
            start = b
            p = a
        else:
            break
        seen[start] = True
        if seen[p]:
            break
    else:
        if a==start:
            p = b
        elif b==start:
            p=a
        else:
            break
        if seen[p]:
            break
else:
    print("Yes")
    exit()
print("No")