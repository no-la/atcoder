sx, sy, gx, gy = map(int, input().split())

print(sx+(sy*(gx-sx))/(gy+sy))