n,m=map(int,input().split())
#print(n,m)
f=[]
s=0
d=[]
for _ in range(n):
    a=list(map(int,input().split()))
    f.append(a)
for i in range(m):
    for j in range(n):
        s+=f[j][i]
    d.append(s)
    s=0
for k in range(len(f)):
    g=f[k]
    d.append(sum(g))
print(max(d))