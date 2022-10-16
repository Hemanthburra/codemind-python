n,m=map(int,input().split())
#print(n,m)
f=[]
s=0
for _ in range(n):
    a=list(map(int,input().split()))
    f.append(a)
for i in range(len(f)):
    if s<sum(f[i]):
        s=sum(f[i])
print(s)