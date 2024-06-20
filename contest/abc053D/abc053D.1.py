N = int(input())
A = list(map(lambda x: int(x)-1, input().split()))
M = max(A)+1

count = [0]*M
for a in A:
    count[a] += 1

# print(count)

# 同じ数字のカードで完結する操作
# n枚から3枚選んで2枚食べる -> 1(n:奇数), 2(n:偶数)
# 4枚から3枚選んで2枚食べる -> 2
# 3枚から3枚選んで2枚食べる -> 1
# そのあと残ったものを見て
# 2枚の数字が
# 偶数個なら余らずにペアを作れる
# 奇数個なら1枚あまってペアを作る

for i in range(M):
    if count[i]>2:
        count[i] = 1 if count[i]&1 else 2

# print(count)
c1, c2 = 0, 0
for c in count:
    if c==1:
        c1 += 1
    elif c==2:
        c2 += 1
ans = c1+c2 - c2%2
print(ans)
