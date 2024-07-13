a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))

x = (b[0]-a[0])**2 + (b[1]-a[1])**2
y = (c[0]-a[0])**2 + (c[1]-a[1])**2
z = (c[0]-b[0])**2 + (c[1]-b[1])**2

print("Yes" if x+y==z or x+z==y or y+z==x else "No")
