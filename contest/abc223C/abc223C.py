N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

left = [0]*(N+1) #d[i]:i番目の導火線の左端に着くまでの時間
right = [0]*(N+1) #d[i]:i番目の導火線の左端に着くまでの時間

for i in range(1, N+1):
    li, ri = i-1, N-i+1
    left[i] = left[li]+A[li][0]/A[li][1]
    right[N-i] = right[ri]+A[N-i][0]/A[N-i][1]

l, r = 0, N
while l<r:
    if left[l]<=right[r]:
        l += 1
    else:
        r -= 1

if left[l]<right[r]:
    r = l+1
else:
    l = r-1
#l番目の導火線で火がぶつかる
offset = sum([a[0] for a in A[:l]])
print(offset+(A[l][0]+A[l][1]*(right[r]-left[l]))/2)