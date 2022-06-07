a,b=map(int,input().split())
f=list(map(int,input().split()))
g=list(map(int,input().split()))
d=[]
for i in range(len(f)):
    if f[i] in g:
        if f[i] not in d:
            d.append(f[i])
print(*d)