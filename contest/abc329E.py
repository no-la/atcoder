N, M = map(int, input().split())
S = list(input())
T = input()
R = set()
for i in range(M):
    for j in range(M-i):
        R.add("#"*i+T[i:M-j]+"#"*(j))
P = ["#"]*M

def judge(id):
    b = "".join(S[id:id+M]) in R
    return b
def replace(id):
    S[id:id+M] = P

i = 0
while i<N-M+1:
    if judge(i):
        replace(i)
        todo = [i]
        while todo:
            v = todo.pop()
            for j in range(1, M+1):
                nv = v-j
                if nv<0:
                    break
                if judge(nv):
                    replace(nv)
                    todo.append(nv)
    i += 1
for s in S:
    if s!="#":
        ans = "No"
        break
else:
    ans = "Yes"
print(ans)