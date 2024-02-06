#例1
a = [1, 2, 3]
b = a
b[0] = 0
print(a) #[0, 2, 3]


#例2
a = [1, 2, 3]
b = a.copy()
b[0] = 0
print(a) #[1, 2, 3]


#例3
a = [[1, 2], 3]
b = a.copy()
b[0][0] = 0
print(a) #[[0, 2], 3]

#例4
from copy import deepcopy
a = [[1, 2], 3]
b = deepcopy(a)
b[0][0] = 0
print(a) #[[1, 2], 3]