N, K = map(int, input().split())
A = list(map(int, input().split())) + [0]

# (1, 2, ..., A[0], 1, 2, ..., A[1], ..., A[N-1])
# からK個以下選ぶとき、その和の最大値はいくつか

l, r = 1, max(A)+1
while l+1<r: # l: l以上の要素がK個以下であるような最小のl
    c = (l+r)//2
    temp = 0
    for i in range(N):
        temp += max(0, A[i]-c+1)
        if temp>K:
            l = c+1
            break
    else:
        r = c

# print(A, l, r)
ans = 0
count = 0
for a in A:
    if a<l:
        continue
    ans += (a-l+1)*(a+l)//2
    count += a-l+1
print(ans+(K-count)*(l-1))
