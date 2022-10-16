n,m=map(int,input().split())
#print(n,m)
f=[]
s=0
for _ in range(n):
    a=list(map(int,input().split()))
    f.append(a)
for i in range(m):
    for j in range(n):
        s+=f[j][i]
    print(s,end=" ")
    s=0