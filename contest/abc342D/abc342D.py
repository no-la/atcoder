N = int(input())
A = list(map(int, input().split()))


from collections import defaultdict
d = defaultdict(int)

zeros = 0
sqrs = 0
# O(N*450)<9*10^7
for a in A:
    if a==0: # 0と平方数は別
        zeros += 1
        continue
    v = a
    for n in range(1, 450):
        n2 = n*n
        if a%n2==0:
            v = a//n2
    if v==1:
        sqrs += 1
        continue
    d[v] += 1

# [0, 0以外], [0, 0], [平方数, 平方数], その他
print(zeros*(N-zeros) + zeros*(zeros-1)//2 + sqrs*(sqrs-1)//2
      + sum([v*(v-1)//2 for v in d.values()]))
    