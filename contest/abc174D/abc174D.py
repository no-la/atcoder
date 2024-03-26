N = int(input())
C = input()

# RR...RWW...W にするための最小コストを出す
R = []
W = []
for i in range(N):
    if C[i]=="R":
        R.append(i)
    else:
        W.append(i)

# 各wについて、自分より右側にrがある場合、最も右側にあるものと入れ替える
# 無ければ終わり
c = 0
for i in W:
    if not R:
        break
    if R[-1]>i:
        R.pop()
    else:
        break
    c += 1
print(c)