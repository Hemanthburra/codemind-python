a,b=map(int,input().split())
f=list(map(int,input().split()))
g=list(map(int,input().split()))
d=[]

for i in range(len(f)):
    if f[i] not in g:
        d.append(f[i])
for i in range(len(g)):
    if g[i] not in f:
        d.append(g[i])
    

print(*d)