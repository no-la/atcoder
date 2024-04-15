import sys
sys.setrecursionlimit(100000)

S = input()
Q = int(input())


def f(i):
    if i==0:
        return 0
    else:
        pre = f(i//2)
        return ((pre+1)%3, (pre+2)%3)[(i+1)%2]

# 全部の文字が、1->2->4->8->...と増えていく
for _ in range(Q):
    t, k = map(int, input().split())
    k -= 1
    if t==0:
        print(S[k])
        continue
    elif t>59: # 2^60>10^18
        first = 0
        tar = k
    else:
        tt = 2**t
        first = k//tt
        tar = k%tt
    # print(first, tar)
    s = ord(S[first])-ord("A")+1
    print("ABC"[(f(tar)+s)%3])
        