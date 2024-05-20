Q = int(input())

from collections import deque
d = deque([])
for _ in range(Q):
    t, *a = map(int, input().split())
    if t==1:
        d.append(a)
    else:
        c = a[0]
        count = 0
        ans = 0
        while count<c:
            if count+d[0][1]<=c:
                temp = d.popleft()
                count += temp[1]
                ans += temp[0]*temp[1]
            else:
                delta = c-count
                d[0][1] -= delta
                count += delta
                ans += delta*d[0][0]
        print(ans)
