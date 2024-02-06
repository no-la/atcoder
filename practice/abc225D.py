N, Q = map(int, input().split())

anss = []
front = [-1]*(N+1) #front[i]:電車iの前部に連結されている電車
back = [-1]*(N+1) #back[i]:電車iの後部に連結されている電車
for _ in range(Q):
    query = input().split()
    if query[0]=="1":
        x, y = map(int, query[1:])
        back[x] = y
        front[y] = x
    elif query[0]=="2":
        x, y = map(int, query[1:])
        back[x] = -1
        front[y] = -1
    else:
        x = int(query[1])
        ans = [x] #逆向き
        i = front[x]
        while i!=-1:
            ans.append(i)
            i = front[i]
        ans.reverse()
        i = back[x]
        while i!=-1:
            ans.append(i)
            i = back[i]
        anss.append(f"{len(ans)} {' '.join(map(str, ans))}")
        print(anss[-1])