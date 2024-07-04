class SegTree:
    def __init__(self, n, func, e, v=None):
        self.n=n
        self.func=func
        self.size=n.bit_length()
        self.m=pow(2,self.size)
        self.data=[e]*2*self.m
        self.e=e
        if v is not None:
            for i in range(self.n):
                self.data[self.m+i]=v[i]

    def set(self, l, r, x):
        assert 0<=l<=r<=self.n
        l+=self.m
        r+=self.m
        while l<r:
            if l&1:
                self.data[l]=self.func(self.data[l],x)
                l+=1
            if r&1:
                self.data[r-1]=self.func(self.data[r-1],x)
            l>>=1
            r>>=1

    def get(self, i):
        assert 0<=i<self.n
        i+=self.m
        for j in range(self.size,0,-1):
            node=i>>j
            self.data[2*node]=self.func(self.data[2*node],self.data[node])
            self.data[2*node+1]=self.func(self.data[2*node+1],self.data[node])
            self.data[node]=self.e
        return self.data[i]

    def print(self):
        a=1
        while a<=self.m:
            print(*self.data[a:2*a])
            a<<=1

    def printall(self):
        for node in range(1,self.m):
            self.data[2*node]=self.func(self.data[2*node],self.data[node])
            self.data[2*node+1]=self.func(self.data[2*node+1],self.data[node])
        print(*self.data[self.m:self.m+self.n])

n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
def f(a,b): return a+b
t=SegTree(n,f,0,a)
for x in b:
    ball=t.get(x)
    t.set(x,x+1,-ball)
    t.set(0,n,ball//n)
    if x+ball%n<n:
        t.set(x+1,x+ball%n+1,1)
    else:
        t.set(x+1,n,1)
        t.set(0,x+ball%n+1-n,1)
    
t.printall()

