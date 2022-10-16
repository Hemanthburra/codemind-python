n,m=map(int,input().split())
f=[]
s=0
for _ in range(n):
    a=list(map(int,input().split()))
    f.append(a)
for i in range(len(f)):
    s+=sum(f[i])
print(s)