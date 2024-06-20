N = int(input())
A = list(map(lambda x: int(x)-1, input().split()))
M = max(A)+1

count = [0]*M
for a in A:
    count[a] += 1

# print(count)

# 尺取り法
right = 0
temp = A[right] #部分列による値（条件の判定に必要なときに使う）
for left in range(M):
    while count[left]>1:
        while temp<3 and right<N: # 条件の判定
            temp += count[right]
            right += 1
        count[left] -= 1
        count[right-1] -= 1
        temp -= 2
    
    if left == right: # [left, right)が空集合なので'temp=初期値'になっているはず
        right += 1
    else: #このあとleftを+1するので、その分の情報を削る
        temp -= count[left]

# print(count)
print(sum([c for c in count]))
