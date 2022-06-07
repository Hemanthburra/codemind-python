r=int(input())
d=list(map(int,input().split()))
g=[]
f=[]
for i in range(len(d)):
    if i%2:
        f.append(d[i])
    else:
        g.append(d[i])
g1=[]
for j in range(len(g)):
    for k in range(f[j]):
        g1.append(g[j])
print(*g1)
        
