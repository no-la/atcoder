S = list(map(int, input().split()))
T = list(map(int, input().split()))

# xは小さい方に揃える
if (S[0]+S[1])%2==1:
    S[0] -= 1
if (T[0]+T[1])%2==1:
    T[0] -= 1

# print(S, T)
# 斜めに行ってから直進する
x, y = abs(T[0]-S[0]), abs(T[1]-S[1])
naname = min(x, y)
if naname==y:
    tyokusin = (x-naname)//2
else:
    tyokusin = y-naname
print(naname+tyokusin)
