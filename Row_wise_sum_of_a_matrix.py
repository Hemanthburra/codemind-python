n,m=map(int,input().split())
f=[]
s=[]
for _ in range(n):
    a=list(map(int,input().split()))
    f.append(a)
for i in range(len(f)):
    s=f[i]
    print(sum(s),end=" ")