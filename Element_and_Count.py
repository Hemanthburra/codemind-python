n=int(input())
g=list(map(int,input().split()))
f=[]
for i in range(len(g)):
    a=g.count(g[i])
    if g[i] not in f:
        f.append(g[i])
        print(g[i],a,end=' ')