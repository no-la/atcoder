A, B = map(int, input().split())
ans = set([1, 2, 3]) - set([A, B])
print(ans.pop() if len(ans)==1 else -1)