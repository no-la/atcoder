T = int(input())

# x=aとしてよい
# y=s-x(=s-a)が必要
for _ in range(T):
    a, s = map(int, input().split())
    print("Yes" if a<=s and a&(s-a)==a else "No")