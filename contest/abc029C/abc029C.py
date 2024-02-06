N = int(input())
n = 3
option = ["a", "b", "c"]
# #自分のやり方
# for i in range(n**N):
#     t = i
#     s = ""
#     for j in range(N-1, -1, -1):
#         a = n**j
#         u = t // a
#         s += option[u]
#         t = t % a
#     print(s)

#DFS
ans = []
seen = [False]*(n**N)
todo = []
for i in range(n):
    todo.append(i)
    seen[i] = True
while(len(todo)!=0):
    v = todo.pop(0) #辞書順にするために0
    for w in option:
        if seen[v] == True:
            continue
        seen[v] = True
        todo.append(v)
        
        